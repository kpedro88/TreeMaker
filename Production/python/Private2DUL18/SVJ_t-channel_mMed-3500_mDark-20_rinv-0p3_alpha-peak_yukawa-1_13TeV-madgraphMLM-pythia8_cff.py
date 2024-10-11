import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/user/lpcdarkqcd/tchannel_UL/signal_production_2Dscans/2018/MINIAOD/step_MINIAOD_t-channel_mMed-3500_mDark-20_rinv-0.3_alpha-peak_yukawa-1_13TeV-madgraphMLM-pythia8_n-2632/part-1.root',
       '/store/user/lpcdarkqcd/tchannel_UL/signal_production_2Dscans/2018/MINIAOD/step_MINIAOD_t-channel_mMed-3500_mDark-20_rinv-0.3_alpha-peak_yukawa-1_13TeV-madgraphMLM-pythia8_n-2632/part-2.root',
       '/store/user/lpcdarkqcd/tchannel_UL/signal_production_2Dscans/2018/MINIAOD/step_MINIAOD_t-channel_mMed-3500_mDark-20_rinv-0.3_alpha-peak_yukawa-1_13TeV-madgraphMLM-pythia8_n-2632/part-3.root',
       '/store/user/lpcdarkqcd/tchannel_UL/signal_production_2Dscans/2018/MINIAOD/step_MINIAOD_t-channel_mMed-3500_mDark-20_rinv-0.3_alpha-peak_yukawa-1_13TeV-madgraphMLM-pythia8_n-2632/part-4.root',
       '/store/user/lpcdarkqcd/tchannel_UL/signal_production_2Dscans/2018/MINIAOD/step_MINIAOD_t-channel_mMed-3500_mDark-20_rinv-0.3_alpha-peak_yukawa-1_13TeV-madgraphMLM-pythia8_n-2632/part-5.root',
       '/store/user/lpcdarkqcd/tchannel_UL/signal_production_2Dscans/2018/MINIAOD/step_MINIAOD_t-channel_mMed-3500_mDark-20_rinv-0.3_alpha-peak_yukawa-1_13TeV-madgraphMLM-pythia8_n-2632/part-6.root',
       '/store/user/lpcdarkqcd/tchannel_UL/signal_production_2Dscans/2018/MINIAOD/step_MINIAOD_t-channel_mMed-3500_mDark-20_rinv-0.3_alpha-peak_yukawa-1_13TeV-madgraphMLM-pythia8_n-2632/part-7.root',
       '/store/user/lpcdarkqcd/tchannel_UL/signal_production_2Dscans/2018/MINIAOD/step_MINIAOD_t-channel_mMed-3500_mDark-20_rinv-0.3_alpha-peak_yukawa-1_13TeV-madgraphMLM-pythia8_n-2632/part-8.root',
       '/store/user/lpcdarkqcd/tchannel_UL/signal_production_2Dscans/2018/MINIAOD/step_MINIAOD_t-channel_mMed-3500_mDark-20_rinv-0.3_alpha-peak_yukawa-1_13TeV-madgraphMLM-pythia8_n-2632/part-9.root',
       '/store/user/lpcdarkqcd/tchannel_UL/signal_production_2Dscans/2018/MINIAOD/step_MINIAOD_t-channel_mMed-3500_mDark-20_rinv-0.3_alpha-peak_yukawa-1_13TeV-madgraphMLM-pythia8_n-2632/part-10.root',
       '/store/user/lpcdarkqcd/tchannel_UL/signal_production_2Dscans/2018/MINIAOD/step_MINIAOD_t-channel_mMed-3500_mDark-20_rinv-0.3_alpha-peak_yukawa-1_13TeV-madgraphMLM-pythia8_n-2632/part-11.root',
       '/store/user/lpcdarkqcd/tchannel_UL/signal_production_2Dscans/2018/MINIAOD/step_MINIAOD_t-channel_mMed-3500_mDark-20_rinv-0.3_alpha-peak_yukawa-1_13TeV-madgraphMLM-pythia8_n-2632/part-12.root',
       '/store/user/lpcdarkqcd/tchannel_UL/signal_production_2Dscans/2018/MINIAOD/step_MINIAOD_t-channel_mMed-3500_mDark-20_rinv-0.3_alpha-peak_yukawa-1_13TeV-madgraphMLM-pythia8_n-2632/part-13.root',
       '/store/user/lpcdarkqcd/tchannel_UL/signal_production_2Dscans/2018/MINIAOD/step_MINIAOD_t-channel_mMed-3500_mDark-20_rinv-0.3_alpha-peak_yukawa-1_13TeV-madgraphMLM-pythia8_n-2632/part-14.root',
       '/store/user/lpcdarkqcd/tchannel_UL/signal_production_2Dscans/2018/MINIAOD/step_MINIAOD_t-channel_mMed-3500_mDark-20_rinv-0.3_alpha-peak_yukawa-1_13TeV-madgraphMLM-pythia8_n-2632/part-15.root',
       '/store/user/lpcdarkqcd/tchannel_UL/signal_production_2Dscans/2018/MINIAOD/step_MINIAOD_t-channel_mMed-3500_mDark-20_rinv-0.3_alpha-peak_yukawa-1_13TeV-madgraphMLM-pythia8_n-2632/part-16.root',
       '/store/user/lpcdarkqcd/tchannel_UL/signal_production_2Dscans/2018/MINIAOD/step_MINIAOD_t-channel_mMed-3500_mDark-20_rinv-0.3_alpha-peak_yukawa-1_13TeV-madgraphMLM-pythia8_n-2632/part-17.root',
       '/store/user/lpcdarkqcd/tchannel_UL/signal_production_2Dscans/2018/MINIAOD/step_MINIAOD_t-channel_mMed-3500_mDark-20_rinv-0.3_alpha-peak_yukawa-1_13TeV-madgraphMLM-pythia8_n-2632/part-18.root',
       '/store/user/lpcdarkqcd/tchannel_UL/signal_production_2Dscans/2018/MINIAOD/step_MINIAOD_t-channel_mMed-3500_mDark-20_rinv-0.3_alpha-peak_yukawa-1_13TeV-madgraphMLM-pythia8_n-2632/part-19.root',
       '/store/user/lpcdarkqcd/tchannel_UL/signal_production_2Dscans/2018/MINIAOD/step_MINIAOD_t-channel_mMed-3500_mDark-20_rinv-0.3_alpha-peak_yukawa-1_13TeV-madgraphMLM-pythia8_n-2632/part-20.root',
       '/store/user/lpcdarkqcd/tchannel_UL/signal_production_2Dscans/2018/MINIAOD/step_MINIAOD_t-channel_mMed-3500_mDark-20_rinv-0.3_alpha-peak_yukawa-1_13TeV-madgraphMLM-pythia8_n-2632/part-21.root',
       '/store/user/lpcdarkqcd/tchannel_UL/signal_production_2Dscans/2018/MINIAOD/step_MINIAOD_t-channel_mMed-3500_mDark-20_rinv-0.3_alpha-peak_yukawa-1_13TeV-madgraphMLM-pythia8_n-2632/part-22.root',
       '/store/user/lpcdarkqcd/tchannel_UL/signal_production_2Dscans/2018/MINIAOD/step_MINIAOD_t-channel_mMed-3500_mDark-20_rinv-0.3_alpha-peak_yukawa-1_13TeV-madgraphMLM-pythia8_n-2632/part-23.root',
       '/store/user/lpcdarkqcd/tchannel_UL/signal_production_2Dscans/2018/MINIAOD/step_MINIAOD_t-channel_mMed-3500_mDark-20_rinv-0.3_alpha-peak_yukawa-1_13TeV-madgraphMLM-pythia8_n-2632/part-24.root',
       '/store/user/lpcdarkqcd/tchannel_UL/signal_production_2Dscans/2018/MINIAOD/step_MINIAOD_t-channel_mMed-3500_mDark-20_rinv-0.3_alpha-peak_yukawa-1_13TeV-madgraphMLM-pythia8_n-2632/part-25.root',
       '/store/user/lpcdarkqcd/tchannel_UL/signal_production_2Dscans/2018/MINIAOD/step_MINIAOD_t-channel_mMed-3500_mDark-20_rinv-0.3_alpha-peak_yukawa-1_13TeV-madgraphMLM-pythia8_n-2632/part-26.root',
       '/store/user/lpcdarkqcd/tchannel_UL/signal_production_2Dscans/2018/MINIAOD/step_MINIAOD_t-channel_mMed-3500_mDark-20_rinv-0.3_alpha-peak_yukawa-1_13TeV-madgraphMLM-pythia8_n-2632/part-27.root',
       '/store/user/lpcdarkqcd/tchannel_UL/signal_production_2Dscans/2018/MINIAOD/step_MINIAOD_t-channel_mMed-3500_mDark-20_rinv-0.3_alpha-peak_yukawa-1_13TeV-madgraphMLM-pythia8_n-2632/part-28.root',
       '/store/user/lpcdarkqcd/tchannel_UL/signal_production_2Dscans/2018/MINIAOD/step_MINIAOD_t-channel_mMed-3500_mDark-20_rinv-0.3_alpha-peak_yukawa-1_13TeV-madgraphMLM-pythia8_n-2632/part-29.root',
       '/store/user/lpcdarkqcd/tchannel_UL/signal_production_2Dscans/2018/MINIAOD/step_MINIAOD_t-channel_mMed-3500_mDark-20_rinv-0.3_alpha-peak_yukawa-1_13TeV-madgraphMLM-pythia8_n-2632/part-30.root',
       '/store/user/lpcdarkqcd/tchannel_UL/signal_production_2Dscans/2018/MINIAOD/step_MINIAOD_t-channel_mMed-3500_mDark-20_rinv-0.3_alpha-peak_yukawa-1_13TeV-madgraphMLM-pythia8_n-2632/part-31.root',
       '/store/user/lpcdarkqcd/tchannel_UL/signal_production_2Dscans/2018/MINIAOD/step_MINIAOD_t-channel_mMed-3500_mDark-20_rinv-0.3_alpha-peak_yukawa-1_13TeV-madgraphMLM-pythia8_n-2632/part-32.root',
       '/store/user/lpcdarkqcd/tchannel_UL/signal_production_2Dscans/2018/MINIAOD/step_MINIAOD_t-channel_mMed-3500_mDark-20_rinv-0.3_alpha-peak_yukawa-1_13TeV-madgraphMLM-pythia8_n-2632/part-33.root',
       '/store/user/lpcdarkqcd/tchannel_UL/signal_production_2Dscans/2018/MINIAOD/step_MINIAOD_t-channel_mMed-3500_mDark-20_rinv-0.3_alpha-peak_yukawa-1_13TeV-madgraphMLM-pythia8_n-2632/part-34.root',
       '/store/user/lpcdarkqcd/tchannel_UL/signal_production_2Dscans/2018/MINIAOD/step_MINIAOD_t-channel_mMed-3500_mDark-20_rinv-0.3_alpha-peak_yukawa-1_13TeV-madgraphMLM-pythia8_n-2632/part-35.root',
       '/store/user/lpcdarkqcd/tchannel_UL/signal_production_2Dscans/2018/MINIAOD/step_MINIAOD_t-channel_mMed-3500_mDark-20_rinv-0.3_alpha-peak_yukawa-1_13TeV-madgraphMLM-pythia8_n-2632/part-36.root',
       '/store/user/lpcdarkqcd/tchannel_UL/signal_production_2Dscans/2018/MINIAOD/step_MINIAOD_t-channel_mMed-3500_mDark-20_rinv-0.3_alpha-peak_yukawa-1_13TeV-madgraphMLM-pythia8_n-2632/part-37.root',
       '/store/user/lpcdarkqcd/tchannel_UL/signal_production_2Dscans/2018/MINIAOD/step_MINIAOD_t-channel_mMed-3500_mDark-20_rinv-0.3_alpha-peak_yukawa-1_13TeV-madgraphMLM-pythia8_n-2632/part-38.root',
] )
