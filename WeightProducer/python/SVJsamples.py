import FWCore.ParameterSet.Config as cms

from TreeMaker.WeightProducer.MCSample import MCSample

# semivisible jet signals
SVJsamples = [
    MCSample("step4_MINIAOD_2016_mZprime-3000_mDark-20_rinv-0.3_alpha-0.2_n-1000", "ProductionV3", "", "Constant", 48974),
    MCSample("step4_MINIAOD_mZprime-3000_mDark-20_rinv-0.3_alpha-0.2_n-1000", "ProductionV3", "", "Constant", 49414),
    MCSample("step4_MINIAOD_mZprime-3000_mDark-20_rinv-0.3_alpha-peak_n-1000", "ProductionV3", "", "Constant", 49206),
    MCSample("step4_MINIAOD_mZprime-1000_mDark-20_rinv-0.3_alpha-peak_n-1000", "ProductionV3", "", "Constant", 49204),
    MCSample("step4_MINIAOD_mZprime-1500_mDark-20_rinv-0.3_alpha-peak_n-1000", "ProductionV3", "", "Constant", 48603),
    MCSample("step4_MINIAOD_mZprime-2000_mDark-20_rinv-0.3_alpha-peak_n-1000", "ProductionV3", "", "Constant", 49156),
    MCSample("step4_MINIAOD_mZprime-2500_mDark-20_rinv-0.3_alpha-peak_n-1000", "ProductionV3", "", "Constant", 48821),
    MCSample("step4_MINIAOD_mZprime-3500_mDark-20_rinv-0.3_alpha-peak_n-1000", "ProductionV3", "", "Constant", 48974),
    MCSample("step4_MINIAOD_mZprime-4000_mDark-20_rinv-0.3_alpha-peak_n-1000", "ProductionV3", "", "Constant", 48978),
    MCSample("step4_MINIAOD_mZprime-3000_mDark-5_rinv-0.3_alpha-peak_n-1000" , "ProductionV3", "", "Constant", 49194),
    MCSample("step4_MINIAOD_mZprime-3000_mDark-50_rinv-0.3_alpha-peak_n-1000", "ProductionV3", "", "Constant", 48693),
    MCSample("step4_MINIAOD_mZprime-3000_mDark-20_rinv-0_alpha-peak_n-1000"  , "ProductionV3", "", "Constant", 98200),
    MCSample("step4_MINIAOD_mZprime-3000_mDark-20_rinv-0.1_alpha-peak_n-1000", "ProductionV3", "", "Constant", 49792),
    MCSample("step4_MINIAOD_mZprime-3000_mDark-20_rinv-0.2_alpha-peak_n-1000", "ProductionV3", "", "Constant", 48903),
    MCSample("step4_MINIAOD_mZprime-3000_mDark-20_rinv-0.4_alpha-peak_n-1000", "ProductionV3", "", "Constant", 49043),
    MCSample("step4_MINIAOD_mZprime-3000_mDark-20_rinv-0.5_alpha-peak_n-1000", "ProductionV3", "", "Constant", 48986),
    MCSample("step4_MINIAOD_mZprime-3000_mDark-20_rinv-0.6_alpha-peak_n-1000", "ProductionV3", "", "Constant", 49104),
    MCSample("step4_MINIAOD_mZprime-3000_mDark-20_rinv-0.7_alpha-peak_n-1000", "ProductionV3", "", "Constant", 48982),
    MCSample("step4_MINIAOD_mZprime-3000_mDark-20_rinv-0.8_alpha-peak_n-1000", "ProductionV3", "", "Constant", 49033),
    MCSample("step4_MINIAOD_mZprime-3000_mDark-20_rinv-0.9_alpha-peak_n-1000", "ProductionV3", "", "Constant", 49484),
    MCSample("step4_MINIAOD_mZprime-3000_mDark-20_rinv-1_alpha-peak_n-1000"  , "ProductionV3", "", "Constant", 49204),
    MCSample("step4_MINIAOD_mZprime-3000_mDark-20_rinv-0.3_alpha-high_n-1000", "ProductionV3", "", "Constant", 49001),
    MCSample("step4_MINIAOD_mZprime-3000_mDark-20_rinv-0.3_alpha-low_n-1000" , "ProductionV3", "", "Constant", 49155),
    MCSample("step4_MINIAOD_mZprime-500_mDark-20_rinv-0.3_alpha-peak_n-2000", "ProductionV3", "", "Constant", 49223),
    MCSample("step4_MINIAOD_mZprime-600_mDark-20_rinv-0.3_alpha-peak_n-2000", "ProductionV3", "", "Constant", 49041),
    MCSample("step4_MINIAOD_mZprime-700_mDark-20_rinv-0.3_alpha-peak_n-2000", "ProductionV3", "", "Constant", 49120),
    MCSample("step4_MINIAOD_mZprime-800_mDark-20_rinv-0.3_alpha-peak_n-2000", "ProductionV3", "", "Constant", 49217),
    MCSample("step4_MINIAOD_mZprime-900_mDark-20_rinv-0.3_alpha-peak_n-2000", "ProductionV3", "", "Constant", 48958),
    MCSample("step4_MINIAOD_mZprime-1100_mDark-20_rinv-0.3_alpha-peak_n-2000", "ProductionV3", "", "Constant", 49050),
    MCSample("step4_MINIAOD_mZprime-1200_mDark-20_rinv-0.3_alpha-peak_n-2000", "ProductionV3", "", "Constant", 49153),
    MCSample("step4_MINIAOD_mZprime-1300_mDark-20_rinv-0.3_alpha-peak_n-2000", "ProductionV3", "", "Constant", 49086),
    MCSample("step4_MINIAOD_mZprime-1400_mDark-20_rinv-0.3_alpha-peak_n-2000", "ProductionV3", "", "Constant", 49268),
    MCSample("step4_MINIAOD_mZprime-1600_mDark-20_rinv-0.3_alpha-peak_n-2000", "ProductionV3", "", "Constant", 49023),
    MCSample("step4_MINIAOD_mZprime-1700_mDark-20_rinv-0.3_alpha-peak_n-2000", "ProductionV3", "", "Constant", 49151),
    MCSample("step4_MINIAOD_mZprime-1800_mDark-20_rinv-0.3_alpha-peak_n-2000", "ProductionV3", "", "Constant", 49156),
    MCSample("step4_MINIAOD_mZprime-1900_mDark-20_rinv-0.3_alpha-peak_n-2000", "ProductionV3", "", "Constant", 49220),
    MCSample("step4_MINIAOD_mZprime-2100_mDark-20_rinv-0.3_alpha-peak_n-2000", "ProductionV3", "", "Constant", 48873),
    MCSample("step4_MINIAOD_mZprime-2200_mDark-20_rinv-0.3_alpha-peak_n-2000", "ProductionV3", "", "Constant", 49108),
    MCSample("step4_MINIAOD_mZprime-2300_mDark-20_rinv-0.3_alpha-peak_n-2000", "ProductionV3", "", "Constant", 49272),
    MCSample("step4_MINIAOD_mZprime-2400_mDark-20_rinv-0.3_alpha-peak_n-2000", "ProductionV3", "", "Constant", 49050),
    MCSample("step4_MINIAOD_mZprime-2600_mDark-20_rinv-0.3_alpha-peak_n-2000", "ProductionV3", "", "Constant", 49273),
    MCSample("step4_MINIAOD_mZprime-2700_mDark-20_rinv-0.3_alpha-peak_n-2000", "ProductionV3", "", "Constant", 49296),
    MCSample("step4_MINIAOD_mZprime-2800_mDark-20_rinv-0.3_alpha-peak_n-2000", "ProductionV3", "", "Constant", 49030),
    MCSample("step4_MINIAOD_mZprime-2900_mDark-20_rinv-0.3_alpha-peak_n-2000", "ProductionV3", "", "Constant", 49268),
    MCSample("step4_MINIAOD_mZprime-3000_mDark-1_rinv-0.3_alpha-peak_n-2000", "ProductionV3", "", "Constant", 49184),
    MCSample("step4_MINIAOD_mZprime-3000_mDark-10_rinv-0.3_alpha-peak_n-2000", "ProductionV3", "", "Constant", 49056),
    MCSample("step4_MINIAOD_mZprime-3000_mDark-30_rinv-0.3_alpha-peak_n-2000", "ProductionV3", "", "Constant", 49180),
    MCSample("step4_MINIAOD_mZprime-3000_mDark-40_rinv-0.3_alpha-peak_n-2000", "ProductionV3", "", "Constant", 49144),
    MCSample("step4_MINIAOD_mZprime-3000_mDark-60_rinv-0.3_alpha-peak_n-2000", "ProductionV3", "", "Constant", 49130),
    MCSample("step4_MINIAOD_mZprime-3000_mDark-70_rinv-0.3_alpha-peak_n-2000", "ProductionV3", "", "Constant", 48939),
    MCSample("step4_MINIAOD_mZprime-3000_mDark-80_rinv-0.3_alpha-peak_n-2000", "ProductionV3", "", "Constant", 49071),
    MCSample("step4_MINIAOD_mZprime-3000_mDark-90_rinv-0.3_alpha-peak_n-2000", "ProductionV3", "", "Constant", 49415),
    MCSample("step4_MINIAOD_mZprime-3000_mDark-100_rinv-0.3_alpha-peak_n-2000", "ProductionV3", "", "Constant", 49173),
    MCSample("step4_MINIAOD_mZprime-3100_mDark-20_rinv-0.3_alpha-peak_n-2000", "ProductionV3", "", "Constant", 49033),
    MCSample("step4_MINIAOD_mZprime-3200_mDark-20_rinv-0.3_alpha-peak_n-2000", "ProductionV3", "", "Constant", 48956),
    MCSample("step4_MINIAOD_mZprime-3300_mDark-20_rinv-0.3_alpha-peak_n-2000", "ProductionV3", "", "Constant", 49125),
    MCSample("step4_MINIAOD_mZprime-3400_mDark-20_rinv-0.3_alpha-peak_n-2000", "ProductionV3", "", "Constant", 49017),
    MCSample("step4_MINIAOD_mZprime-3600_mDark-20_rinv-0.3_alpha-peak_n-2000", "ProductionV3", "", "Constant", 49062),
    MCSample("step4_MINIAOD_mZprime-3700_mDark-20_rinv-0.3_alpha-peak_n-2000", "ProductionV3", "", "Constant", 49045),
    MCSample("step4_MINIAOD_mZprime-3800_mDark-20_rinv-0.3_alpha-peak_n-2000", "ProductionV3", "", "Constant", 49086),
    MCSample("step4_MINIAOD_mZprime-3900_mDark-20_rinv-0.3_alpha-peak_n-2000", "ProductionV3", "", "Constant", 49135),
    MCSample("step4_MINIAOD_mZprime-4100_mDark-20_rinv-0.3_alpha-peak_n-2000", "ProductionV3", "", "Constant", 49142),
    MCSample("step4_MINIAOD_mZprime-4200_mDark-20_rinv-0.3_alpha-peak_n-2000", "ProductionV3", "", "Constant", 49101),
    MCSample("step4_MINIAOD_mZprime-4300_mDark-20_rinv-0.3_alpha-peak_n-2000", "ProductionV3", "", "Constant", 48978),
    MCSample("step4_MINIAOD_mZprime-4400_mDark-20_rinv-0.3_alpha-peak_n-2000", "ProductionV3", "", "Constant", 49226),
    MCSample("step4_MINIAOD_mZprime-4500_mDark-20_rinv-0.3_alpha-peak_n-2000", "ProductionV3", "", "Constant", 49336),
    MCSample('SVJ_mZprime-3000_mDark-20_rinv-0p3_alpha-peak_TuneCP2_13TeV_pythia8', 'PU2017_12Apr2018_DMinvis_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 98216, False),
    MCSample("step4_MINIAOD_t-channel_mMed-200_mDark-20_rinv-0.3_alpha-peak_yukawa-1_13TeV-madgraphMLM-pythia8_n-1000", "", "", "Constant", 42874),
    MCSample("step4_MINIAOD_t-channel_mMed-400_mDark-20_rinv-0.3_alpha-peak_yukawa-1_13TeV-madgraphMLM-pythia8_n-1000", "", "", "Constant", 38814),
    MCSample("step4_MINIAOD_t-channel_mMed-600_mDark-20_rinv-0.3_alpha-peak_yukawa-1_13TeV-madgraphMLM-pythia8_n-1000", "", "", "Constant", 38375),
    MCSample("step4_MINIAOD_t-channel_mMed-800_mDark-20_rinv-0.1_alpha-peak_yukawa-1_13TeV-madgraphMLM-pythia8_n-1000", "", "", "Constant", 46764),
    MCSample("step4_MINIAOD_t-channel_mMed-800_mDark-20_rinv-0.3_alpha-peak_yukawa-1_13TeV-madgraphMLM-pythia8_n-1000", "", "", "Constant", 38845),
    MCSample("step4_MINIAOD_t-channel_mMed-800_mDark-20_rinv-0.5_alpha-peak_yukawa-1_13TeV-madgraphMLM-pythia8_n-1000", "", "", "Constant", 38214),
    MCSample("step4_MINIAOD_t-channel_mMed-800_mDark-20_rinv-0.7_alpha-peak_yukawa-1_13TeV-madgraphMLM-pythia8_n-1000", "", "", "Constant", 37961),
    MCSample("step4_MINIAOD_t-channel_mMed-1000_mDark-20_rinv-0.3_alpha-peak_yukawa-1_13TeV-madgraphMLM-pythia8_n-1000", "", "", "Constant", 38948),
    MCSample("step4_MINIAOD_t-channel_mMed-2000_mDark-20_rinv-0.3_alpha-peak_yukawa-1_13TeV-madgraphMLM-pythia8_n-1000", "", "", "Constant", 40967),
    MCSample("step4_MINIAOD_t-channel_mMed-3000_mDark-1_rinv-0.3_alpha-peak_yukawa-1_13TeV-madgraphMLM-pythia8_n-1000", "", "", "Constant", 40132),
    MCSample("step4_MINIAOD_t-channel_mMed-3000_mDark-20_rinv-0.3_alpha-peak_yukawa-1_13TeV-madgraphMLM-pythia8_n-1000", "", "", "Constant", 41292),
    MCSample("step4_MINIAOD_t-channel_mMed-3000_mDark-50_rinv-0.3_alpha-peak_yukawa-1_13TeV-madgraphMLM-pythia8_n-1000", "", "", "Constant", 42495),
    MCSample("step4_MINIAOD_t-channel_mMed-3000_mDark-100_rinv-0.3_alpha-peak_yukawa-1_13TeV-madgraphMLM-pythia8_n-1000", "", "", "Constant", 43436),
    MCSample("step4_MINIAOD_t-channel_mMed-3000_mDark-20_rinv-0.1_alpha-peak_yukawa-1_13TeV-madgraphMLM-pythia8_n-1000", "", "", "Constant", 48853),
    MCSample("step4_MINIAOD_t-channel_mMed-3000_mDark-20_rinv-0.5_alpha-peak_yukawa-1_13TeV-madgraphMLM-pythia8_n-1000", "", "", "Constant", 40621),
    MCSample("step4_MINIAOD_t-channel_mMed-3000_mDark-20_rinv-0.7_alpha-peak_yukawa-1_13TeV-madgraphMLM-pythia8_n-1000", "", "", "Constant", 40798),
    MCSample("step4_MINIAOD_t-channel_mMed-3000_mDark-20_rinv-0.3_alpha-low_yukawa-1_13TeV-madgraphMLM-pythia8_n-1000", "", "", "Constant", 41539),
    MCSample("step4_MINIAOD_t-channel_mMed-3000_mDark-20_rinv-0.3_alpha-high_yukawa-1_13TeV-madgraphMLM-pythia8_n-1000", "", "", "Constant", 41572),
    MCSample("step4_MINIAOD_t-channel_mMed-4000_mDark-20_rinv-0.3_alpha-peak_yukawa-1_13TeV-madgraphMLM-pythia8_n-1000", "", "", "Constant", 41348),
    MCSample("step4_MINIAOD_t-channel_mMed-6000_mDark-20_rinv-0.3_alpha-peak_yukawa-1_13TeV-madgraphMLM-pythia8_n-1000", "", "", "Constant", 40765),
    MCSample("step4_MINIAOD_t-channel_mMed-400_mDark-20_rinv-0.3_alpha-peak_yukawa-1_13TeV-pythia8_n-1000", "", "", "Constant", 49850),
    MCSample("step4_MINIAOD_t-channel_mMed-600_mDark-20_rinv-0.3_alpha-peak_yukawa-1_13TeV-pythia8_n-1000", "", "", "Constant", 49234),
    MCSample("step4_MINIAOD_t-channel_mMed-800_mDark-20_rinv-0.3_alpha-peak_yukawa-1_13TeV-pythia8_n-1000", "", "", "Constant", 49291),
    MCSample("step4_MINIAOD_t-channel_mMed-1000_mDark-20_rinv-0.3_alpha-peak_yukawa-1_13TeV-pythia8_n-1000", "", "", "Constant", 49426),
    MCSample("step4_MINIAOD_t-channel_mMed-2000_mDark-20_rinv-0.3_alpha-peak_yukawa-1_13TeV-pythia8_n-1000", "", "", "Constant", 49919),
    MCSample("step4_MINIAOD_t-channel_mMed-3000_mDark-20_rinv-0.3_alpha-peak_yukawa-1_13TeV-pythia8_n-1000", "", "", "Constant", 50160),
]
