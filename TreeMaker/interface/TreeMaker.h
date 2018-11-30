// CMSSW headers
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/one/EDAnalyzer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "FWCore/Utilities/interface/EDMException.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "DataFormats/Provenance/interface/EventAuxiliary.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "DataFormats/PatCandidates/interface/PackedGenParticle.h"
#include "DataFormats/Candidate/interface/Candidate.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
#include "DataFormats/PatCandidates/interface/PackedCandidate.h"
#include "FWCore/Framework/interface/ConsumesCollector.h"

//ROOT headers
#include "TString.h"
#include "TTree.h"
#include <TFile.h>
#include "TLorentzVector.h"
#include "Math/GenVector/LorentzVector.h"

//STL headers
#include <memory>
#include <vector>
#include <string>
#include <map>
#include <sstream>
#include <algorithm>

using namespace std;

//enum with known types
enum TreeTypes { 
	t_bool=0, t_int=1, t_double=2, t_string=3, t_lorentz=4,
	t_vbool=100, t_vint=101, t_vdouble=102, t_vstring=103, t_vlorentz=104,
	t_vvbool=200, t_vvint=201, t_vvdouble=202, t_vvstring=203, t_vvlorentz=204,
	t_recocand=1000
};

//forward declaration of helper class
class TreeObjectBase;

//
// class declaration
//

class TreeMaker : public edm::one::EDAnalyzer<edm::one::SharedResources> {
	public:
		explicit TreeMaker(const edm::ParameterSet&);
		~TreeMaker() override;
		static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);

	private:
		void beginJob() override;
		void analyze(const edm::Event&, const edm::EventSetup&) override;
		void endJob() override;
		// ----------member data ---------------------------
		edm::Service<TFileService> fs;
		string treeName;
		TTree* tree;	
		bool doLorentz, sortBranches;
		vector<string> VarTypeNames;
		vector<TreeTypes> VarTypes;
		map<string,unsigned> nameCache;
		// general event information
		UInt_t runNum{};
		UInt_t lumiBlockNum{};
		ULong64_t evtNum{};
		vector<TreeObjectBase*> variables;
};

//base class for tree objects
class TreeObjectBase {
	public:
		//constructor
		TreeObjectBase() : tempFull(""), branchType("") {}
		TreeObjectBase(string tempFull_) : tempFull(tempFull_), nameInTree(tempFull_), tagName(tempFull_), tree(nullptr) {}
		//destructor
		virtual ~TreeObjectBase() {}
		//functions
		virtual string GetNameInTree() const { return nameInTree; }
		virtual void Initialize(map<string,unsigned>& nameCache, edm::ConsumesCollector && iC, stringstream& message) {}
		virtual void SetTree(TTree* tree_) { tree = tree_; }
		virtual void AddBranch() {}
		virtual void SetDefault() {}
		virtual void FillTree(const edm::Event& iEvent) {}
		
		//common helper function
		virtual void FinalizeName(map<string,unsigned>& nameCache, stringstream& message){
			auto nameIt = nameCache.find(nameInTree);
			if(nameIt != nameCache.end()){
				stringstream ss;
				ss << nameInTree << "_" << nameIt->second;
				nameInTree = ss.str();
				message << "Warning: name in tree already defined, alternating name... " << nameInTree << "\n";
				//increment count for this name
				nameIt->second++;
			}
			else {
				//add this name to the cache
				nameCache[nameInTree] = 1;
			}
		}
		
	protected:
		//member variables
		string tempFull, nameInTree, tagName, branchType;
		TTree* tree{};
		edm::InputTag tag;
};

//comparator (case-insensitive sort)
class TreeObjectComp {
	public:
		bool operator() (TreeObjectBase* b1, TreeObjectBase* b2) const {
			string s1 = b1->GetNameInTree();
			transform(s1.begin(),s1.end(),s1.begin(),::tolower);
			string s2 = b2->GetNameInTree();
			transform(s2.begin(),s2.end(),s2.begin(),::tolower);
			
			return s1 < s2;
		}
};

//class template for tree objects
template <class Tin, class Tout=Tin>
class TreeObject : public TreeObjectBase {
	public:
		//constructor
		TreeObject() : TreeObjectBase() {}
		TreeObject(string tempFull_) : TreeObjectBase(tempFull_) {}
		//destructor
		~TreeObject() override {}
		//functions
		void Initialize(map<string,unsigned>& nameCache, edm::ConsumesCollector && iC, stringstream& message) override {
			//case 1: x      -> tag = x,   name = x
			//case 2: x:y    -> tag = x:y, name = y
			//case 3: x(y)   -> tag = x,   name = y
			//case 4: x:y(z) -> tag = x:y, name = z
			
			size_t pos1 = tempFull.find('(');
			size_t pos2 = tempFull.find(')');
			size_t pos3 = tempFull.find(':');
			
			//case 3/4
			if(pos1!=string::npos && pos2!=string::npos){
				tagName = tempFull.substr(0,pos1);
				nameInTree = tempFull.substr(pos1+1,pos2-(pos1+1));
			}
			//case 2
			else if(pos3!=string::npos){
				nameInTree = tempFull.substr(pos3+1);
			}
			//case 1, nothing to do
			//(constructor assumes this case by default)
			else { }
			
			message << "full name: " << tempFull << " -> tag: " << tagName << " nameInTree: " << nameInTree << "\n";
			//make tag
			tag = edm::InputTag(tagName);
			SetConsumes(std::move(iC));
			
			//finalize name to avoid duplicates
			FinalizeName(nameCache,message);
		}
		virtual void SetConsumes(edm::ConsumesCollector && iC){
			tok = iC.consumes<Tin>(tag);
		}
		void GetValue(const edm::Handle<Tin>& var) {
			value = *var;
		}
		void FillTree(const edm::Event& iEvent) override {
			SetDefault();
			edm::Handle<Tin> var;
			iEvent.getByToken(tok,var);
			if( var.isValid() ) {
				GetValue(var);
			}
			else {
				edm::LogWarning("TreeMaker") << "WARNING ... " << tagName << " is NOT valid?!";
			}
		}
		//these will be implemented below for specializations
		void AddBranch() override {}
		void SetDefault() override {}
		
	protected:
		//member variables
		Tout value;
		edm::EDGetTokenT<Tin> tok;
};

//typedefs
typedef TreeObject<bool> TreeObjectBool;
typedef TreeObject<int> TreeObjectInt;
typedef TreeObject<double,float> TreeObjectDouble;
typedef TreeObject<string> TreeObjectString;
typedef TreeObject<TLorentzVector> TreeObjectTLV;
typedef TreeObject<vector<bool>> TreeObjectVBool;
typedef TreeObject<vector<int>> TreeObjectVInt;
typedef TreeObject<vector<double>,vector<float>> TreeObjectVDouble;
typedef TreeObject<vector<string>> TreeObjectVString;
typedef TreeObject<vector<TLorentzVector>> TreeObjectVTLV;
typedef TreeObject<vector<vector<bool>>> TreeObjectVVBool;
typedef TreeObject<vector<vector<int>>> TreeObjectVVInt;
typedef TreeObject<vector<vector<double>>,vector<vector<float>>> TreeObjectVVDouble;
typedef TreeObject<vector<vector<string>>> TreeObjectVVString;
typedef TreeObject<vector<vector<TLorentzVector>>> TreeObjectVVTLV;

//convert double to float
template<>
void TreeObjectVDouble::GetValue(const edm::Handle<vector<double>>& var) {
	value = vector<float>(var->begin(),var->end());
}
template<>
void TreeObjectVVDouble::GetValue(const edm::Handle<vector<vector<double>>>& var) {
	value.reserve(var->size());
	for(const auto& ivar: *var){
		value.emplace_back(ivar.begin(),ivar.end());
	}
}

//specialize!

template<>
void TreeObjectBool::AddBranch() { if(tree) tree->Branch(nameInTree.c_str(),&value,(nameInTree+"/O").c_str()); }
template<>
void TreeObjectInt::AddBranch() { if(tree) tree->Branch(nameInTree.c_str(),&value,(nameInTree+"/I").c_str()); }
template<>
void TreeObjectDouble::AddBranch() { if(tree) tree->Branch(nameInTree.c_str(),&value,(nameInTree+"/F").c_str()); }
template<>
void TreeObjectString::AddBranch() { if(tree) tree->Branch(nameInTree.c_str(),nameInTree.c_str(),&value); }
template<>
void TreeObjectTLV::AddBranch() { if(tree) tree->Branch(nameInTree.c_str(),nameInTree.c_str(),&value); }
template<>
void TreeObjectVBool::AddBranch() { if(tree) tree->Branch(nameInTree.c_str(),"vector<bool>",&value,32000,0); }
template<>
void TreeObjectVInt::AddBranch() { if(tree) tree->Branch(nameInTree.c_str(),"vector<int>",&value,32000,0); }
template<>
void TreeObjectVDouble::AddBranch() { if(tree) tree->Branch(nameInTree.c_str(),"vector<float>",&value,32000,0); }
template<>
void TreeObjectVString::AddBranch() { if(tree) tree->Branch(nameInTree.c_str(),"vector<string>",&value,32000,0); }
template<>
void TreeObjectVTLV::AddBranch() { if(tree) tree->Branch(nameInTree.c_str(),"vector<TLorentzVector>",&value,32000,0); }
template<>
void TreeObjectVVBool::AddBranch() { if(tree) tree->Branch(nameInTree.c_str(),"vector<vector<bool>>",&value,32000,0); }
template<>
void TreeObjectVVInt::AddBranch() { if(tree) tree->Branch(nameInTree.c_str(),"vector<vector<int>>",&value,32000,0); }
template<>
void TreeObjectVVDouble::AddBranch() { if(tree) tree->Branch(nameInTree.c_str(),"vector<vector<float>>",&value,32000,0); }
template<>
void TreeObjectVVString::AddBranch() { if(tree) tree->Branch(nameInTree.c_str(),"vector<vector<string>>",&value,32000,0); }
template<>
void TreeObjectVVTLV::AddBranch() { if(tree) tree->Branch(nameInTree.c_str(),"vector<vector<TLorentzVector>>",&value,32000,0); }

template<>
void TreeObjectBool::SetDefault() { value = false; }
template<>
void TreeObjectInt::SetDefault() { value = 9999; }
template<>
void TreeObjectDouble::SetDefault() { value = 9999.; }
template<>
void TreeObjectString::SetDefault() { value = ""; }
template<>
void TreeObjectTLV::SetDefault() { value.SetXYZT(0,0,0,0); }
template<>
void TreeObjectVBool::SetDefault() { value.clear(); }
template<>
void TreeObjectVInt::SetDefault() { value.clear(); }
template<>
void TreeObjectVDouble::SetDefault() { value.clear(); }
template<>
void TreeObjectVString::SetDefault() { value.clear(); }
template<>
void TreeObjectVTLV::SetDefault() { value.clear(); }
template<>
void TreeObjectVVBool::SetDefault() { value.clear(); }
template<>
void TreeObjectVVInt::SetDefault() { value.clear(); }
template<>
void TreeObjectVVDouble::SetDefault() { value.clear(); }
template<>
void TreeObjectVVString::SetDefault() { value.clear(); }
template<>
void TreeObjectVVTLV::SetDefault() { value.clear(); }

//derived version of vector<TLorentzVector> for RecoCand
//with switch for vector<double> pt, eta, phi, energy instead
class TreeRecoCand : public TreeObjectVTLV {
	public:
		//constructor
		TreeRecoCand() : TreeObjectVTLV() {}
		TreeRecoCand(string tempFull_, bool doLorentz_=true) : TreeObjectVTLV(tempFull_), doLorentz(doLorentz_) {}
		//destructor
		~TreeRecoCand() override {}
		
		//functions
		void SetConsumes(edm::ConsumesCollector && iC) override{
			candTok = iC.consumes<edm::View<reco::Candidate>>(tag);
		}
		void FillTree(const edm::Event& iEvent) override{
			SetDefault();
			edm::Handle<edm::View<reco::Candidate>> cands;
			iEvent.getByToken(candTok,cands);
			if( cands.isValid() ) {
				if(doLorentz){
					value.reserve(cands->size());
					for(auto iPart = cands->begin(); iPart != cands->end(); ++iPart){
						value.emplace_back(iPart->px(), iPart->py(), iPart->pz(), iPart->energy());
					}
				}
				else{
					pt.reserve(cands->size());
					eta.reserve(cands->size());
					phi.reserve(cands->size());
					energy.reserve(cands->size());
					for(auto iPart = cands->begin(); iPart != cands->end(); ++iPart){
						pt.emplace_back(iPart->pt());
						eta.emplace_back(iPart->eta());
						phi.emplace_back(iPart->phi());
						energy.emplace_back(iPart->energy());
					}
				}
			}
			else {
				edm::LogWarning("TreeMaker") << "WARNING ... " << tagName << " is NOT valid?!";
			}
		}
		void AddBranch() override {
			if(tree){
				if(doLorentz){
					tree->Branch(nameInTree.c_str(),"vector<TLorentzVector>",&value,32000,0);
				}
				else {
					tree->Branch((nameInTree+"Pt").c_str(),"vector<double>",&pt,32000,0);
					tree->Branch((nameInTree+"Eta").c_str(),"vector<double>",&eta,32000,0);
					tree->Branch((nameInTree+"Phi").c_str(),"vector<double>",&phi,32000,0);
					tree->Branch((nameInTree+"E").c_str(),"vector<double>",&energy,32000,0);
				}
			}
		}
		void SetDefault() override {
			if(doLorentz){
				value.clear();
			}
			else{
				pt.clear();
				eta.clear();
				phi.clear();
				energy.clear();
			}
		}
	
	protected:
		//member variables
		edm::EDGetTokenT<edm::View<reco::Candidate>> candTok;
		bool doLorentz{};
		vector<double> pt, eta, phi, energy;
};
