import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/user/lpcsuep/Samples/WH/2018/MINIAOD/step_MINIAOD_WH-channel_mMed-125_mDark-2_temp-2_decay-generic_13TeV-pythia8_n-1000_part-1.root',
       '/store/user/lpcsuep/Samples/WH/2018/MINIAOD/step_MINIAOD_WH-channel_mMed-125_mDark-2_temp-2_decay-generic_13TeV-pythia8_n-1000_part-2.root',
       '/store/user/lpcsuep/Samples/WH/2018/MINIAOD/step_MINIAOD_WH-channel_mMed-125_mDark-2_temp-2_decay-generic_13TeV-pythia8_n-1000_part-3.root',
       '/store/user/lpcsuep/Samples/WH/2018/MINIAOD/step_MINIAOD_WH-channel_mMed-125_mDark-2_temp-2_decay-generic_13TeV-pythia8_n-1000_part-4.root',
       '/store/user/lpcsuep/Samples/WH/2018/MINIAOD/step_MINIAOD_WH-channel_mMed-125_mDark-2_temp-2_decay-generic_13TeV-pythia8_n-1000_part-5.root',
       '/store/user/lpcsuep/Samples/WH/2018/MINIAOD/step_MINIAOD_WH-channel_mMed-125_mDark-2_temp-2_decay-generic_13TeV-pythia8_n-1000_part-6.root',
       '/store/user/lpcsuep/Samples/WH/2018/MINIAOD/step_MINIAOD_WH-channel_mMed-125_mDark-2_temp-2_decay-generic_13TeV-pythia8_n-1000_part-7.root',
       '/store/user/lpcsuep/Samples/WH/2018/MINIAOD/step_MINIAOD_WH-channel_mMed-125_mDark-2_temp-2_decay-generic_13TeV-pythia8_n-1000_part-8.root',
       '/store/user/lpcsuep/Samples/WH/2018/MINIAOD/step_MINIAOD_WH-channel_mMed-125_mDark-2_temp-2_decay-generic_13TeV-pythia8_n-1000_part-9.root',
       '/store/user/lpcsuep/Samples/WH/2018/MINIAOD/step_MINIAOD_WH-channel_mMed-125_mDark-2_temp-2_decay-generic_13TeV-pythia8_n-1000_part-10.root',
       '/store/user/lpcsuep/Samples/WH/2018/MINIAOD/step_MINIAOD_WH-channel_mMed-125_mDark-2_temp-2_decay-generic_13TeV-pythia8_n-1000_part-11.root',
       '/store/user/lpcsuep/Samples/WH/2018/MINIAOD/step_MINIAOD_WH-channel_mMed-125_mDark-2_temp-2_decay-generic_13TeV-pythia8_n-1000_part-12.root',
       '/store/user/lpcsuep/Samples/WH/2018/MINIAOD/step_MINIAOD_WH-channel_mMed-125_mDark-2_temp-2_decay-generic_13TeV-pythia8_n-1000_part-13.root',
       '/store/user/lpcsuep/Samples/WH/2018/MINIAOD/step_MINIAOD_WH-channel_mMed-125_mDark-2_temp-2_decay-generic_13TeV-pythia8_n-1000_part-14.root',
       '/store/user/lpcsuep/Samples/WH/2018/MINIAOD/step_MINIAOD_WH-channel_mMed-125_mDark-2_temp-2_decay-generic_13TeV-pythia8_n-1000_part-15.root',
       '/store/user/lpcsuep/Samples/WH/2018/MINIAOD/step_MINIAOD_WH-channel_mMed-125_mDark-2_temp-2_decay-generic_13TeV-pythia8_n-1000_part-16.root',
       '/store/user/lpcsuep/Samples/WH/2018/MINIAOD/step_MINIAOD_WH-channel_mMed-125_mDark-2_temp-2_decay-generic_13TeV-pythia8_n-1000_part-17.root',
       '/store/user/lpcsuep/Samples/WH/2018/MINIAOD/step_MINIAOD_WH-channel_mMed-125_mDark-2_temp-2_decay-generic_13TeV-pythia8_n-1000_part-18.root',
       '/store/user/lpcsuep/Samples/WH/2018/MINIAOD/step_MINIAOD_WH-channel_mMed-125_mDark-2_temp-2_decay-generic_13TeV-pythia8_n-1000_part-19.root',
       '/store/user/lpcsuep/Samples/WH/2018/MINIAOD/step_MINIAOD_WH-channel_mMed-125_mDark-2_temp-2_decay-generic_13TeV-pythia8_n-1000_part-20.root',
] )
