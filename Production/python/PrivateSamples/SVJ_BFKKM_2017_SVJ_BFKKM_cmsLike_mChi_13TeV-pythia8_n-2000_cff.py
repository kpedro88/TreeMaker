import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/user/pedrok/SVJ2017/ProductionV3/2017/MINIAOD/step4_MINIAOD_SVJ_BFKKM_cmsLike_mChi_13TeV-pythia8_n-2000_part-1.root',
       '/store/user/pedrok/SVJ2017/ProductionV3/2017/MINIAOD/step4_MINIAOD_SVJ_BFKKM_cmsLike_mChi_13TeV-pythia8_n-2000_part-2.root',
       '/store/user/pedrok/SVJ2017/ProductionV3/2017/MINIAOD/step4_MINIAOD_SVJ_BFKKM_cmsLike_mChi_13TeV-pythia8_n-2000_part-3.root',
       '/store/user/pedrok/SVJ2017/ProductionV3/2017/MINIAOD/step4_MINIAOD_SVJ_BFKKM_cmsLike_mChi_13TeV-pythia8_n-2000_part-4.root',
       '/store/user/pedrok/SVJ2017/ProductionV3/2017/MINIAOD/step4_MINIAOD_SVJ_BFKKM_cmsLike_mChi_13TeV-pythia8_n-2000_part-5.root',
] )
