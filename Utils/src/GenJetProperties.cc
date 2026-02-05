// -*- C++ -*-
//
// Package:    GenJetProperties
// Class:      GenJetProperties
// 


// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/global/EDProducer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "DataFormats/JetReco/interface/BasicJet.h"
#include "DataFormats/JetReco/interface/GenJet.h"
#include "DataFormats/Candidate/interface/Candidate.h"
#include "DataFormats/Math/interface/deltaR.h"
#include "DataFormats/Common/interface/getRef.h"
#include "DataFormats/Common/interface/ValueMap.h"

//
// class declaration
//

class GenJetProperties : public edm::global::EDProducer<> {
public:
  explicit GenJetProperties(const edm::ParameterSet&);
  ~GenJetProperties() override;

  static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);

private:
  bool hasHVAncestor(const reco::Candidate*) const;
  void produce(edm::StreamID, edm::Event&, const edm::EventSetup&) const override;

  edm::InputTag GenJetTag;
  edm::EDGetTokenT<edm::View<reco::GenJet>> GenJetTok;
  edm::InputTag SoftDropTag;
  edm::EDGetTokenT<std::vector<reco::BasicJet>> SoftDropTok;
  double distMax, jetPtFilter, doHV;
  std::vector<std::string> ecfNames;
  std::vector<edm::EDGetTokenT<edm::ValueMap<float>>> ecfTok;

  // ----------member data ---------------------------
};

//
// constants, enums and typedefs
//
enum particle_type
{
  //HV particles
  hvscalar=4900001,
  hvgluon=4900021,
  zprime=4900023,
  hvquark1=4900101,
  hvquark2=4900102,
  hvpion1=4900111,
  hvrho1=4900113,
  hvpion2=4900211,
  hvrho2=4900213,
};

//
// static data member definitions
//

//
// constructors and destructor
//
GenJetProperties::GenJetProperties(const edm::ParameterSet& iConfig) :
  GenJetTag(iConfig.getParameter<edm::InputTag>("GenJetTag")),
  GenJetTok(consumes<edm::View<reco::GenJet>>(GenJetTag)),
  SoftDropTag(iConfig.getParameter<edm::InputTag>("SoftDropGenJetTag")),
  distMax(iConfig.getParameter<double>("distMax")),
  jetPtFilter(iConfig.getParameter<double>("jetPtFilter")),
  doHV(iConfig.getParameter<bool>("doHV")),
  ecfNames(iConfig.getParameter<std::vector<std::string>>("ecfs"))
{
  // Create the tokens if the InputTags aren't empty strings
  if(!SoftDropTag.label().empty()) {
    SoftDropTok = consumes<std::vector<reco::BasicJet>>(SoftDropTag);
  }

  for (const auto& ecfName : ecfNames) {
    edm::InputTag ecfTag(GenJetTag.label(), ecfName);
    ecfTok.emplace_back(consumes<edm::ValueMap<float>>(ecfTag));
    produces<std::vector<float>>(ecfName);
  }

  //register your products
  produces<std::vector<reco::GenJet>>();
  produces<std::vector<double>>("invisibleEnergy");
  produces<std::vector<double>>("softDropMass");
  produces<std::vector<int>>("multiplicity");
  produces<std::vector<int>>("nHVAncestors");
}


GenJetProperties::~GenJetProperties()
{

  // do anything here that needs to be done at desctruction time
  // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called to determine ancestry  ------------
bool
GenJetProperties::hasHVAncestor(const reco::Candidate* genParticle) const
{
  auto absPdgId = std::abs(genParticle->pdgId());

  if(absPdgId>hvscalar && absPdgId<=hvrho2) {
    return true;
  }
  else if(genParticle->numberOfMothers() == 0) {
    return false;
  }
  else {
    bool compositeResult = false;
    for(unsigned int iMother = 0; iMother < genParticle->numberOfMothers(); iMother++) {
      compositeResult = compositeResult || hasHVAncestor(genParticle->mother(iMother));
    }
    return compositeResult;
  }
}

// ------------ method called to produce the data  ------------
void
GenJetProperties::produce(edm::StreamID, edm::Event& iEvent, const edm::EventSetup& iSetup) const
{
  using namespace edm;

  auto genJetsOut = std::make_unique<std::vector<reco::GenJet>>();
  auto invisibleEnergy = std::make_unique<std::vector<double>>();
  auto softDropMass = std::make_unique<std::vector<double>>();
  auto mult = std::make_unique<std::vector<int>>();
  auto nHVAncestors = std::make_unique<std::vector<int>>();
  std::vector<std::unique_ptr<std::vector<float>>> ecfOut;

  edm::Handle< edm::View<reco::GenJet> > GenJets;
  iEvent.getByToken(GenJetTok,GenJets);
  if( GenJets.isValid() ) {
    bool doSoftDrop(false);

    edm::Handle<std::vector<reco::BasicJet>> SoftDropJets;
    if(!SoftDropTok.isUninitialized()) {
      iEvent.getByToken(SoftDropTok,SoftDropJets);
      doSoftDrop = SoftDropJets.isValid();
    }
    else {
      doSoftDrop = false;
    }

    std::vector<edm::Handle<edm::ValueMap<float>>> ecfHandles;
    for (const auto& tok : ecfTok) {
      ecfHandles.emplace_back();
      iEvent.getByToken(tok, ecfHandles.back());
      ecfOut.emplace_back(std::make_unique<std::vector<float>>());
    }

    for(unsigned j = 0; j < GenJets->size(); ++j){
      const auto& GenJet = (*GenJets)[j];
      if(jetPtFilter>0. and GenJet.pt()<jetPtFilter) continue;
      genJetsOut->push_back(GenJet);

      invisibleEnergy->push_back( GenJet.invisibleEnergy() );
      double softdrop = 0.0;
      int hvConstituents = 0;

      if(doSoftDrop){
        for(const auto& SoftDropJet: *SoftDropJets){
          if(reco::deltaR(GenJet,SoftDropJet)<distMax){
            softdrop = SoftDropJet.mass();
            break;
          }
        }
      }
      if(doHV>0.0){
        auto constituents = GenJet.daughterPtrVector();
        for(auto constituent : constituents) {
          if(constituent.isNull()) continue;
          //get the pointer to the first survied ancestor of a given packed GenParticle in the prunedCollection
          auto motherInPrunedCollection = constituent->mother(0);
          if(motherInPrunedCollection != nullptr) {
            hvConstituents += hasHVAncestor(motherInPrunedCollection);
          }
        }
      }

      softDropMass->push_back(softdrop);
      mult->push_back(GenJet.numberOfDaughters());
      nHVAncestors->push_back(hvConstituents);

      auto jRef = edm::getRef(GenJets, j);
      for(unsigned i = 0; i < ecfHandles.size(); ++i){
        ecfOut[i]->push_back((*ecfHandles[i])[jRef]);
      }
    }
  }

  iEvent.put(std::move(genJetsOut));
  iEvent.put(std::move(invisibleEnergy),"invisibleEnergy");
  iEvent.put(std::move(softDropMass),"softDropMass");
  iEvent.put(std::move(mult),"multiplicity");
  iEvent.put(std::move(nHVAncestors),"nHVAncestors");
  for(unsigned i = 0; i < ecfNames.size(); ++i){
    iEvent.put(std::move(ecfOut[i]), ecfNames[i]);
  }
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
GenJetProperties::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(GenJetProperties);
