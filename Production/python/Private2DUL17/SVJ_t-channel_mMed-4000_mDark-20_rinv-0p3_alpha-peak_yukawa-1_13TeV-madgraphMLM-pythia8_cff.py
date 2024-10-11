import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/user/lpcdarkqcd/tchannel_UL/signal_production_2Dscans/2017/MINIAOD/step_MINIAOD_t-channel_mMed-4000_mDark-20_rinv-0.3_alpha-peak_yukawa-1_13TeV-madgraphMLM-pythia8_n-2664/part-1.root',
       '/store/user/lpcdarkqcd/tchannel_UL/signal_production_2Dscans/2017/MINIAOD/step_MINIAOD_t-channel_mMed-4000_mDark-20_rinv-0.3_alpha-peak_yukawa-1_13TeV-madgraphMLM-pythia8_n-2664/part-2.root',
       '/store/user/lpcdarkqcd/tchannel_UL/signal_production_2Dscans/2017/MINIAOD/step_MINIAOD_t-channel_mMed-4000_mDark-20_rinv-0.3_alpha-peak_yukawa-1_13TeV-madgraphMLM-pythia8_n-2664/part-3.root',
       '/store/user/lpcdarkqcd/tchannel_UL/signal_production_2Dscans/2017/MINIAOD/step_MINIAOD_t-channel_mMed-4000_mDark-20_rinv-0.3_alpha-peak_yukawa-1_13TeV-madgraphMLM-pythia8_n-2664/part-4.root',
       '/store/user/lpcdarkqcd/tchannel_UL/signal_production_2Dscans/2017/MINIAOD/step_MINIAOD_t-channel_mMed-4000_mDark-20_rinv-0.3_alpha-peak_yukawa-1_13TeV-madgraphMLM-pythia8_n-2664/part-5.root',
       '/store/user/lpcdarkqcd/tchannel_UL/signal_production_2Dscans/2017/MINIAOD/step_MINIAOD_t-channel_mMed-4000_mDark-20_rinv-0.3_alpha-peak_yukawa-1_13TeV-madgraphMLM-pythia8_n-2664/part-6.root',
       '/store/user/lpcdarkqcd/tchannel_UL/signal_production_2Dscans/2017/MINIAOD/step_MINIAOD_t-channel_mMed-4000_mDark-20_rinv-0.3_alpha-peak_yukawa-1_13TeV-madgraphMLM-pythia8_n-2664/part-7.root',
       '/store/user/lpcdarkqcd/tchannel_UL/signal_production_2Dscans/2017/MINIAOD/step_MINIAOD_t-channel_mMed-4000_mDark-20_rinv-0.3_alpha-peak_yukawa-1_13TeV-madgraphMLM-pythia8_n-2664/part-8.root',
       '/store/user/lpcdarkqcd/tchannel_UL/signal_production_2Dscans/2017/MINIAOD/step_MINIAOD_t-channel_mMed-4000_mDark-20_rinv-0.3_alpha-peak_yukawa-1_13TeV-madgraphMLM-pythia8_n-2664/part-9.root',
       '/store/user/lpcdarkqcd/tchannel_UL/signal_production_2Dscans/2017/MINIAOD/step_MINIAOD_t-channel_mMed-4000_mDark-20_rinv-0.3_alpha-peak_yukawa-1_13TeV-madgraphMLM-pythia8_n-2664/part-10.root',
       '/store/user/lpcdarkqcd/tchannel_UL/signal_production_2Dscans/2017/MINIAOD/step_MINIAOD_t-channel_mMed-4000_mDark-20_rinv-0.3_alpha-peak_yukawa-1_13TeV-madgraphMLM-pythia8_n-2664/part-11.root',
       '/store/user/lpcdarkqcd/tchannel_UL/signal_production_2Dscans/2017/MINIAOD/step_MINIAOD_t-channel_mMed-4000_mDark-20_rinv-0.3_alpha-peak_yukawa-1_13TeV-madgraphMLM-pythia8_n-2664/part-12.root',
       '/store/user/lpcdarkqcd/tchannel_UL/signal_production_2Dscans/2017/MINIAOD/step_MINIAOD_t-channel_mMed-4000_mDark-20_rinv-0.3_alpha-peak_yukawa-1_13TeV-madgraphMLM-pythia8_n-2664/part-13.root',
       '/store/user/lpcdarkqcd/tchannel_UL/signal_production_2Dscans/2017/MINIAOD/step_MINIAOD_t-channel_mMed-4000_mDark-20_rinv-0.3_alpha-peak_yukawa-1_13TeV-madgraphMLM-pythia8_n-2664/part-14.root',
       '/store/user/lpcdarkqcd/tchannel_UL/signal_production_2Dscans/2017/MINIAOD/step_MINIAOD_t-channel_mMed-4000_mDark-20_rinv-0.3_alpha-peak_yukawa-1_13TeV-madgraphMLM-pythia8_n-2664/part-15.root',
       '/store/user/lpcdarkqcd/tchannel_UL/signal_production_2Dscans/2017/MINIAOD/step_MINIAOD_t-channel_mMed-4000_mDark-20_rinv-0.3_alpha-peak_yukawa-1_13TeV-madgraphMLM-pythia8_n-2664/part-16.root',
       '/store/user/lpcdarkqcd/tchannel_UL/signal_production_2Dscans/2017/MINIAOD/step_MINIAOD_t-channel_mMed-4000_mDark-20_rinv-0.3_alpha-peak_yukawa-1_13TeV-madgraphMLM-pythia8_n-2664/part-17.root',
       '/store/user/lpcdarkqcd/tchannel_UL/signal_production_2Dscans/2017/MINIAOD/step_MINIAOD_t-channel_mMed-4000_mDark-20_rinv-0.3_alpha-peak_yukawa-1_13TeV-madgraphMLM-pythia8_n-2664/part-18.root',
       '/store/user/lpcdarkqcd/tchannel_UL/signal_production_2Dscans/2017/MINIAOD/step_MINIAOD_t-channel_mMed-4000_mDark-20_rinv-0.3_alpha-peak_yukawa-1_13TeV-madgraphMLM-pythia8_n-2664/part-19.root',
       '/store/user/lpcdarkqcd/tchannel_UL/signal_production_2Dscans/2017/MINIAOD/step_MINIAOD_t-channel_mMed-4000_mDark-20_rinv-0.3_alpha-peak_yukawa-1_13TeV-madgraphMLM-pythia8_n-2664/part-20.root',
       '/store/user/lpcdarkqcd/tchannel_UL/signal_production_2Dscans/2017/MINIAOD/step_MINIAOD_t-channel_mMed-4000_mDark-20_rinv-0.3_alpha-peak_yukawa-1_13TeV-madgraphMLM-pythia8_n-2664/part-21.root',
       '/store/user/lpcdarkqcd/tchannel_UL/signal_production_2Dscans/2017/MINIAOD/step_MINIAOD_t-channel_mMed-4000_mDark-20_rinv-0.3_alpha-peak_yukawa-1_13TeV-madgraphMLM-pythia8_n-2664/part-22.root',
       '/store/user/lpcdarkqcd/tchannel_UL/signal_production_2Dscans/2017/MINIAOD/step_MINIAOD_t-channel_mMed-4000_mDark-20_rinv-0.3_alpha-peak_yukawa-1_13TeV-madgraphMLM-pythia8_n-2664/part-23.root',
       '/store/user/lpcdarkqcd/tchannel_UL/signal_production_2Dscans/2017/MINIAOD/step_MINIAOD_t-channel_mMed-4000_mDark-20_rinv-0.3_alpha-peak_yukawa-1_13TeV-madgraphMLM-pythia8_n-2664/part-24.root',
       '/store/user/lpcdarkqcd/tchannel_UL/signal_production_2Dscans/2017/MINIAOD/step_MINIAOD_t-channel_mMed-4000_mDark-20_rinv-0.3_alpha-peak_yukawa-1_13TeV-madgraphMLM-pythia8_n-2664/part-25.root',
       '/store/user/lpcdarkqcd/tchannel_UL/signal_production_2Dscans/2017/MINIAOD/step_MINIAOD_t-channel_mMed-4000_mDark-20_rinv-0.3_alpha-peak_yukawa-1_13TeV-madgraphMLM-pythia8_n-2664/part-26.root',
] )
