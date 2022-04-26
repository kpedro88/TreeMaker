#include "FWCore/Framework/interface/MakerMacros.h"
#include "CommonTools/UtilAlgos/interface/Merger.h"
#include "DataFormats/PatCandidates/interface/Jet.h"

typedef Merger<std::vector<pat::Jet>> PatJetMerger;

DEFINE_FWK_MODULE(PatJetMerger);
