import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/user/pedrok/SVJ2017/ProductionV3/2017/MINIAOD/step4_MINIAOD_SVJ_BFKKM_modelA_13TeV-pythia8_n-2000_part-1.root',
       '/store/user/pedrok/SVJ2017/ProductionV3/2017/MINIAOD/step4_MINIAOD_SVJ_BFKKM_modelA_13TeV-pythia8_n-2000_part-2.root',
       '/store/user/pedrok/SVJ2017/ProductionV3/2017/MINIAOD/step4_MINIAOD_SVJ_BFKKM_modelA_13TeV-pythia8_n-2000_part-3.root',
       '/store/user/pedrok/SVJ2017/ProductionV3/2017/MINIAOD/step4_MINIAOD_SVJ_BFKKM_modelA_13TeV-pythia8_n-2000_part-4.root',
       '/store/user/pedrok/SVJ2017/ProductionV3/2017/MINIAOD/step4_MINIAOD_SVJ_BFKKM_modelA_13TeV-pythia8_n-2000_part-5.root',
       '/store/user/pedrok/SVJ2017/ProductionV3/2017/MINIAOD/step4_MINIAOD_SVJ_BFKKM_modelA_13TeV-pythia8_n-2000_part-6.root',
       '/store/user/pedrok/SVJ2017/ProductionV3/2017/MINIAOD/step4_MINIAOD_SVJ_BFKKM_modelA_13TeV-pythia8_n-2000_part-7.root',
       '/store/user/pedrok/SVJ2017/ProductionV3/2017/MINIAOD/step4_MINIAOD_SVJ_BFKKM_modelA_13TeV-pythia8_n-2000_part-8.root',
       '/store/user/pedrok/SVJ2017/ProductionV3/2017/MINIAOD/step4_MINIAOD_SVJ_BFKKM_modelA_13TeV-pythia8_n-2000_part-9.root',
       '/store/user/pedrok/SVJ2017/ProductionV3/2017/MINIAOD/step4_MINIAOD_SVJ_BFKKM_modelA_13TeV-pythia8_n-2000_part-10.root',
       '/store/user/pedrok/SVJ2017/ProductionV3/2017/MINIAOD/step4_MINIAOD_SVJ_BFKKM_modelA_13TeV-pythia8_n-2000_part-11.root',
       '/store/user/pedrok/SVJ2017/ProductionV3/2017/MINIAOD/step4_MINIAOD_SVJ_BFKKM_modelA_13TeV-pythia8_n-2000_part-12.root',
       '/store/user/pedrok/SVJ2017/ProductionV3/2017/MINIAOD/step4_MINIAOD_SVJ_BFKKM_modelA_13TeV-pythia8_n-2000_part-13.root',
       '/store/user/pedrok/SVJ2017/ProductionV3/2017/MINIAOD/step4_MINIAOD_SVJ_BFKKM_modelA_13TeV-pythia8_n-2000_part-14.root',
       '/store/user/pedrok/SVJ2017/ProductionV3/2017/MINIAOD/step4_MINIAOD_SVJ_BFKKM_modelA_13TeV-pythia8_n-2000_part-15.root',
       '/store/user/pedrok/SVJ2017/ProductionV3/2017/MINIAOD/step4_MINIAOD_SVJ_BFKKM_modelA_13TeV-pythia8_n-2000_part-16.root',
       '/store/user/pedrok/SVJ2017/ProductionV3/2017/MINIAOD/step4_MINIAOD_SVJ_BFKKM_modelA_13TeV-pythia8_n-2000_part-17.root',
       '/store/user/pedrok/SVJ2017/ProductionV3/2017/MINIAOD/step4_MINIAOD_SVJ_BFKKM_modelA_13TeV-pythia8_n-2000_part-18.root',
       '/store/user/pedrok/SVJ2017/ProductionV3/2017/MINIAOD/step4_MINIAOD_SVJ_BFKKM_modelA_13TeV-pythia8_n-2000_part-19.root',
       '/store/user/pedrok/SVJ2017/ProductionV3/2017/MINIAOD/step4_MINIAOD_SVJ_BFKKM_modelA_13TeV-pythia8_n-2000_part-20.root',
       '/store/user/pedrok/SVJ2017/ProductionV3/2017/MINIAOD/step4_MINIAOD_SVJ_BFKKM_modelA_13TeV-pythia8_n-2000_part-21.root',
       '/store/user/pedrok/SVJ2017/ProductionV3/2017/MINIAOD/step4_MINIAOD_SVJ_BFKKM_modelA_13TeV-pythia8_n-2000_part-22.root',
       '/store/user/pedrok/SVJ2017/ProductionV3/2017/MINIAOD/step4_MINIAOD_SVJ_BFKKM_modelA_13TeV-pythia8_n-2000_part-23.root',
       '/store/user/pedrok/SVJ2017/ProductionV3/2017/MINIAOD/step4_MINIAOD_SVJ_BFKKM_modelA_13TeV-pythia8_n-2000_part-24.root',
       '/store/user/pedrok/SVJ2017/ProductionV3/2017/MINIAOD/step4_MINIAOD_SVJ_BFKKM_modelA_13TeV-pythia8_n-2000_part-25.root',
] )
