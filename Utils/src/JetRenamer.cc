// system include files
#include <memory>
#include <string>
#include <vector>
#include <algorithm>
#include <utility>
#include <array>
#include <iterator>
#include <sstream>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/global/EDProducer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/PluginManager/interface/PluginFactory.h"
#include "FWCore/Utilities/interface/Exception.h"
#include "DataFormats/PatCandidates/interface/Jet.h"

// monkey-patching C++ for fun and profit
class MutableJet : public pat::Jet {
	public:
		//provide access to protected member variables
		std::vector<std::string>& userFloatLabels() { return userFloatLabels_; }
		std::vector<std::string>& userIntLabels() { return userIntLabels_; }
		std::vector<std::string>& userCandLabels() { return userCandLabels_; }
		std::vector<std::string>& subjetLabels() { return subjetLabels_; }

		//for re-sorting
		template <typename Vec>
		void reorder(Vec& vec, const std::vector<size_t>& order) {
			std::vector<bool> done(vec.size());
			for(unsigned i = 0; i < size; ++i){
				if(done[i]) continue;
				done[i] = true;
				unsigned prev_j = i;
				unsigned j = order[i];
				while(i != j){
					std::swap(vec[prev_j],vec[j]);
					done[j] = true;
					prev_j = j;
					j = order[j];
				}
			}
		}
		void reorderFloat(const std::vector<size_t>& order) { reorder(userFloatLabels_, order); reorder(userFloats_, order); }
		void reorderInt(const std::vector<size_t>& order) { reorder(userIntLabels_, order); reorder(userInts_, order); }
		void reorderCand(const std::vector<size_t>& order) { reorder(userCandLabels_, order); reorder(userCands_, order); }
		void reorderSubjet(const std::vector<size_t>& order) { reorder(subjetLabels_, order); reorder(subjetCollections_, order); }

		//userData and pairDiscriVector not handled here: could be done w/ more involved templating
};

//to store member function pointers more easily
typedef std::vector<std::string>& (MutableJet::*LabelGetter)();
typedef void (MutableJet::*Reorder)(const std::vector<size_t>& order);

class JetRenamer : public edm::global::EDProducer<> {
public:
	explicit JetRenamer(const edm::ParameterSet&);
	~JetRenamer() override {}

	static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);

private:
	void produce(edm::StreamID, edm::Event&, const edm::EventSetup&) const override;

	edm::InputTag JetTag_;
	edm::EDGetTokenT<edm::View<pat::Jet>> JetTok_;
	static const size_t nLabelTypes_ = 4;
	static const std::array<std::string, nLabelTypes_> labelTypes_;
	static const std::array<LabelGetter, nLabelTypes_> labelGetters_;
	static const std::array<Reorder, nLabelTypes_> reorders_;
	std::array<std::vector<std::string>, nLabelTypes_> oldLabels_;
	std::array<std::vector<std::string>, nLabelTypes_> newLabels_;
};

const std::array<std::string, JetRenamer::nLabelTypes_> JetRenamer::labelTypes_ = {{"userFloat","userInt","userCand","subjet"}};
const std::array<LabelGetter, JetRenamer::nLabelTypes_> JetRenamer::labelGetters_ = {{&MutableJet::userFloatLabels, &MutableJet::userIntLabels, &MutableJet::userCandLabels, &MutableJet::subjetLabels}};
const std::array<Reorder, JetRenamer::nLabelTypes_> JetRenamer::reorders_ = {{&MutableJet::reorderFloat, &MutableJet::reorderInt, &MutableJet::reorderCand, &MutableJet::reorderSubjet}};

JetRenamer::JetRenamer(const edm::ParameterSet& iConfig) :
	JetTag_(iConfig.getParameter<edm::InputTag>("JetTag")),
	JetTok_(consumes<edm::View<pat::Jet>>(JetTag_))
{
	for(unsigned i = 0; i < nLabelTypes_; ++i){
		oldLabels_[i] = iConfig.getParameter<std::vector<std::string>>(labelTypes_[i] + "Old");
		newLabels_[i] = iConfig.getParameter<std::vector<std::string>>(labelTypes_[i] + "New");
		if(oldLabels_[i].size() != newLabels_[i].size()) throw cms::Exception("VectorSizeMismatch") << "Inconsistent sizes for old and new " << labelTypes_[i] << " labels";
	}

	produces<std::vector<pat::Jet>>();
}

void JetRenamer::produce(edm::StreamID, edm::Event& iEvent, const edm::EventSetup& iSetup) const {
	edm::Handle<edm::View<pat::Jet>> h_jets;
	iEvent.getByToken(JetTok_, h_jets);
	auto renamed = std::make_unique<std::vector<pat::Jet>>();

	//assume indices are the same for all jets in an event
	std::array<std::vector<size_t>, nLabelTypes_> oldIndices, newIndices;
	for(unsigned j = 0; j < h_jets->size(); ++j){
		renamed->push_back((*h_jets)[j]);
		auto jet = static_cast<MutableJet*>(&renamed->back());
		for(unsigned i = 0; i < nLabelTypes_; ++i){
			auto& labels = ((*jet).*labelGetters_[i])();
			if(j==0) oldIndices[i].reserve(oldLabels_[i].size());
			for(unsigned k = 0; k < oldLabels_[i].size(); ++k){
				const auto& oldLabel = oldLabels_[i][k];
				//get indices
				if(j==0){
					//can't binary search here because it might not be in sorted order
					auto it = std::find(labels.begin(), labels.end(), oldLabel);
					if(it == labels.end()) {
						cms::Exception ex("UnknownLabel");
						ex << "Could not find index of old label (type " << labelTypes_[i] << "): " << oldLabel;
						std::stringstream ss;
						std::copy(labels.begin(), labels.end(), std::ostream_iterator<std::string>(ss, " "));
						ex << "\nAvailable labels:\n" << ss.str();
						throw ex;
					}
					oldIndices[i].push_back(std::distance(labels.begin(), it));
				}
				labels[oldIndices[i][k]] = newLabels_[i][k];
			}
			//re-sort so lower_bound checks in PAT still work (if necessary)
			if(j==0 and !std::is_sorted(labels.begin(),labels.end())){
				newIndices[i] = std::vector<size_t>(labels.size());
				std::iota(newIndices[i].begin(),newIndices[i].end(),0);
				std::sort(newIndices[i].begin(),newIndices[i].end(), [&](size_t i, size_t j){ return labels[i] < labels[j]; });
			}
			if(!newIndices[i].empty()) ((*jet).*reorders_[i])(newIndices[i]);
		}
	}

	iEvent.put(std::move(renamed));
}

void JetRenamer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
	edm::ParameterSetDescription desc;

	desc.add<edm::InputTag>("JetTag");
	for(unsigned i = 0; i < nLabelTypes_; ++i){
		desc.add<std::vector<std::string>>(labelTypes_[i] + "Old", {});
		desc.add<std::vector<std::string>>(labelTypes_[i] + "New", {});
	}

	descriptions.add("JetRenamer",desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(JetRenamer);
