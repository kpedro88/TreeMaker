import FWCore.ParameterSet.Config as cms

from TreeMaker.WeightProducer.MCSampleValues import MCSampleValuesHelper
XSValues = MCSampleValuesHelper.XSValues

SVJxsecs = {
    "s-channel_mMed-200_MADPT300" : {
        "CrossSection" : XSValues(XS_13TeV=7.412),
    },
    "s-channel_mMed-250_MADPT300" : {
        "CrossSection" : XSValues(XS_13TeV=7.044),
    },
    "s-channel_mMed-300_MADPT300" : {
        "CrossSection" : XSValues(XS_13TeV=6.781),
    },
    "s-channel_mMed-350_MADPT300" : {
        "CrossSection" : XSValues(XS_13TeV=6.158),
    },
    "s-channel_mMed-400_MADPT300" : {
        "CrossSection" : XSValues(XS_13TeV=5.566),
    },
    "s-channel_mMed-450_MADPT300" : {
        "CrossSection" : XSValues(XS_13TeV=5.021),
    },
    "s-channel_mMed-500_MADPT300" : {
        "CrossSection" : XSValues(XS_13TeV=4.439),
    },
    "s-channel_mMed-550_MADPT300" : {
        "CrossSection" : XSValues(XS_13TeV=3.795),
    },
    "s-channel_mMed-500"  : { "CrossSection" : XSValues(XS_13TeV=79.21), },
    "s-channel_mMed-600"  : { "CrossSection" : XSValues(XS_13TeV=53.32), },
    "s-channel_mMed-700"  : { "CrossSection" : XSValues(XS_13TeV=35.89), },
    "s-channel_mMed-800"  : { "CrossSection" : XSValues(XS_13TeV=24.16), },
    "s-channel_mMed-900"  : { "CrossSection" : XSValues(XS_13TeV=16.26), },
    "s-channel_mMed-1000" : { "CrossSection" : XSValues(XS_13TeV=10.95), },
    "s-channel_mMed-1100" : { "CrossSection" : XSValues(XS_13TeV=7.368), },
    "s-channel_mMed-1200" : { "CrossSection" : XSValues(XS_13TeV=5.086), },
    "s-channel_mMed-1300" : { "CrossSection" : XSValues(XS_13TeV=3.586), },
    "s-channel_mMed-1400" : { "CrossSection" : XSValues(XS_13TeV=2.574), },
    "s-channel_mMed-1500" : { "CrossSection" : XSValues(XS_13TeV=1.875), },
    "s-channel_mMed-1600" : { "CrossSection" : XSValues(XS_13TeV=1.384), },
    "s-channel_mMed-1700" : { "CrossSection" : XSValues(XS_13TeV=1.033), },
    "s-channel_mMed-1800" : { "CrossSection" : XSValues(XS_13TeV=0.7789), },
    "s-channel_mMed-1900" : { "CrossSection" : XSValues(XS_13TeV=0.5923), },
    "s-channel_mMed-2000" : { "CrossSection" : XSValues(XS_13TeV=0.4537), },
    "s-channel_mMed-2100" : { "CrossSection" : XSValues(XS_13TeV=0.3498), },
    "s-channel_mMed-2200" : { "CrossSection" : XSValues(XS_13TeV=0.2713), },
    "s-channel_mMed-2300" : { "CrossSection" : XSValues(XS_13TeV=0.2116), },
    "s-channel_mMed-2400" : { "CrossSection" : XSValues(XS_13TeV=0.1658), },
    "s-channel_mMed-2500" : { "CrossSection" : XSValues(XS_13TeV=0.1304), },
    "s-channel_mMed-2600" : { "CrossSection" : XSValues(XS_13TeV=0.1029), },
    "s-channel_mMed-2700" : { "CrossSection" : XSValues(XS_13TeV=0.08149), },
    "s-channel_mMed-2800" : { "CrossSection" : XSValues(XS_13TeV=0.06476), },
    "s-channel_mMed-2900" : { "CrossSection" : XSValues(XS_13TeV=0.0516), },
    "s-channel_mMed-3000" : { "CrossSection" : XSValues(XS_13TeV=0.0412), },
    "s-channel_mMed-3100" : { "CrossSection" : XSValues(XS_13TeV=0.03297), },
    "s-channel_mMed-3200" : { "CrossSection" : XSValues(XS_13TeV=0.02644), },
    "s-channel_mMed-3300" : { "CrossSection" : XSValues(XS_13TeV=0.02123), },
    "s-channel_mMed-3400" : { "CrossSection" : XSValues(XS_13TeV=0.01707), },
    "s-channel_mMed-3500" : { "CrossSection" : XSValues(XS_13TeV=0.01376), },
    "s-channel_mMed-3600" : { "CrossSection" : XSValues(XS_13TeV=0.01109), },
    "s-channel_mMed-3700" : { "CrossSection" : XSValues(XS_13TeV=0.008951), },
    "s-channel_mMed-3800" : { "CrossSection" : XSValues(XS_13TeV=0.007234), },
    "s-channel_mMed-3900" : { "CrossSection" : XSValues(XS_13TeV=0.005849), },
    "s-channel_mMed-4000" : { "CrossSection" : XSValues(XS_13TeV=0.004731), },
    "s-channel_mMed-4100" : { "CrossSection" : XSValues(XS_13TeV=0.003828), },
    "s-channel_mMed-4200" : { "CrossSection" : XSValues(XS_13TeV=0.003099), },
    "s-channel_mMed-4300" : { "CrossSection" : XSValues(XS_13TeV=0.002509), },
    "s-channel_mMed-4400" : { "CrossSection" : XSValues(XS_13TeV=0.002032), },
    "s-channel_mMed-4500" : { "CrossSection" : XSValues(XS_13TeV=0.001645), },
    "s-channel_mMed-4600" : { "CrossSection" : XSValues(XS_13TeV=0.001331), },
    "s-channel_mMed-4700" : { "CrossSection" : XSValues(XS_13TeV=0.001078), },
    "s-channel_mMed-4800" : { "CrossSection" : XSValues(XS_13TeV=0.0008709), },
    "s-channel_mMed-4900" : { "CrossSection" : XSValues(XS_13TeV=0.0007043), },
    "s-channel_mMed-5000" : { "CrossSection" : XSValues(XS_13TeV=0.000569), },
    "s-channel_mMed-5100" : { "CrossSection" : XSValues(XS_13TeV=0.0004593), },
    # Full t-channel cross section
    # currently commented out in favor of pair production cross sections (below)
    # todo for UL: improve naming scheme to disambiguate, recalculate cross sections w/ newer PDFs
    #"t-channel_mMed-200" : {
    #    "CrossSection" : XSValues(XS_13TeV=990.8), # uncertainty: 3.617
    #},
    # "t-channel_mMed-400" : {
    #     "CrossSection" : XSValues(XS_13TeV=54.24), # uncertainty: 0.2163
    # },
    #"t-channel_mMed-500" : {
    #    "CrossSection" : XSValues(XS_13TeV=21.7), # uncertainty: 0.08651
    #},
    # "t-channel_mMed-600" : {
    #     "CrossSection" : XSValues(XS_13TeV=10.07), # uncertainty: 0.04063
    # },
    # "t-channel_mMed-800" : {
    #     "CrossSection" : XSValues(XS_13TeV=3.096), # uncertainty: 0.0124
    # },
    # "t-channel_mMed-1000" : {
    #     "CrossSection" : XSValues(XS_13TeV=1.247), # uncertainty: 0.004968
    # },
    # "t-channel_mMed-2000" : {
    #     "CrossSection" : XSValues(XS_13TeV=0.08492), # uncertainty: 3.290e-04
    # },
    # "t-channel_mMed-3000" : {
    #     "CrossSection" : XSValues(XS_13TeV=0.01891), # uncertainty: 7.277e-05
    # },
    #"t-channel_mMed-4000" : {
    #    "CrossSection" : XSValues(XS_13TeV=0.006132), # uncertainty: 2.361e-05
    #},
    #"t-channel_mMed-6000" : {
    #    "CrossSection" : XSValues(XS_13TeV=0.001269), # uncertainty: 4.938e-06
    #},
    # t-channel pair production cross sections
    "t-channel_mMed-400" : {
        "CrossSection" : XSValues(XS_13TeV=13.68), # uncertainty: 0.2579
    },
    "t-channel_mMed-600" : {
        "CrossSection" : XSValues(XS_13TeV=1.315), # uncertainty: 0.02370
    },
    "t-channel_mMed-800" : {
        "CrossSection" : XSValues(XS_13TeV=0.2092), # uncertainty: 0.003806
    },
    "t-channel_mMed-1000" : {
        "CrossSection" : XSValues(XS_13TeV=0.04452), # uncertainty: 8.065e-04
    },
    "t-channel_mMed-2000" : {
        "CrossSection" : XSValues(XS_13TeV=0.0001209), # uncertainty: 2.216e-06
    },
    "t-channel_mMed-3000" : {
        "CrossSection" : XSValues(XS_13TeV=0.000001462), # uncertainty: 2.812e-08
    },

}

