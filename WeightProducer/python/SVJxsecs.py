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
    "mZprime-500"  : {
        "CrossSection" : XSValues(XS_13TeV=71.37),
    },
    "mZprime-600"  : {
        "CrossSection" : XSValues(XS_13TeV=33.22),
    },
    "mZprime-700"  : {
        "CrossSection" : XSValues(XS_13TeV=18.17),
    },
    "mZprime-800"  : {
        "CrossSection" : XSValues(XS_13TeV=10.75),
    },
    "mZprime-900"  : {
        "CrossSection" : XSValues(XS_13TeV=7.04),
    },
    "mZprime-1000" : {
        "CrossSection" : XSValues(XS_13TeV=4.612),
    },
    "mZprime-1100" : {
        "CrossSection" : XSValues(XS_13TeV=3.021),
    },
    "mZprime-1200" : {
        "CrossSection" : XSValues(XS_13TeV=2.039),
    },
    "mZprime-1300" : {
        "CrossSection" : XSValues(XS_13TeV=1.459),
    },
    "mZprime-1400" : {
        "CrossSection" : XSValues(XS_13TeV=1.057),
    },
    "mZprime-1500" : {
        "CrossSection" : XSValues(XS_13TeV=0.77),
    },
    "mZprime-1600" : {
        "CrossSection" : XSValues(XS_13TeV=0.5667),
    },
    "mZprime-1700" : {
        "CrossSection" : XSValues(XS_13TeV=0.4327),
    },
    "mZprime-1800" : {
        "CrossSection" : XSValues(XS_13TeV=0.3304),
    },
    "mZprime-1900" : {
        "CrossSection" : XSValues(XS_13TeV=0.2479),
    },
    "mZprime-2000" : {
        "CrossSection" : XSValues(XS_13TeV=0.1849),
    },
    "mZprime-2100" : {
        "CrossSection" : XSValues(XS_13TeV=0.1384),
    },
    "mZprime-2200" : {
        "CrossSection" : XSValues(XS_13TeV=0.1044),
    },
    "mZprime-2300" : {
        "CrossSection" : XSValues(XS_13TeV=0.08124),
    },
    "mZprime-2400" : {
        "CrossSection" : XSValues(XS_13TeV=0.06361),
    },
    "mZprime-2500" : {
        "CrossSection" : XSValues(XS_13TeV=0.04977),
    },
    "mZprime-2600" : {
        "CrossSection" : XSValues(XS_13TeV=0.03891),
    },
    "mZprime-2700" : {
        "CrossSection" : XSValues(XS_13TeV=0.03042),
    },
    "mZprime-2800" : {
        "CrossSection" : XSValues(XS_13TeV=0.02447),
    },
    "mZprime-2900" : {
        "CrossSection" : XSValues(XS_13TeV=0.01969),
    },
    "mZprime-3000" : {
        "CrossSection" : XSValues(XS_13TeV=0.0155),
    },
    "mZprime-3100" : {
        "CrossSection" : XSValues(XS_13TeV=0.01209),
    },
    "mZprime-3200" : {
        "CrossSection" : XSValues(XS_13TeV=0.009518),
    },
    "mZprime-3300" : {
        "CrossSection" : XSValues(XS_13TeV=0.007494),
    },
    "mZprime-3400" : {
        "CrossSection" : XSValues(XS_13TeV=0.006148),
    },
    "mZprime-3500" : {
        "CrossSection" : XSValues(XS_13TeV=0.005036),
    },
    "mZprime-3600" : {
        "CrossSection" : XSValues(XS_13TeV=0.004047),
    },
    "mZprime-3700" : {
        "CrossSection" : XSValues(XS_13TeV=0.003252),
    },
    "mZprime-3800" : {
        "CrossSection" : XSValues(XS_13TeV=0.002613),
    },
    "mZprime-3900" : {
        "CrossSection" : XSValues(XS_13TeV=0.0021),
    },
    "mZprime-4000" : {
        "CrossSection" : XSValues(XS_13TeV=0.001688),
    },
    "mZprime-4100" : {
        "CrossSection" : XSValues(XS_13TeV=0.001356),
    },
    "mZprime-4200" : {
        "CrossSection" : XSValues(XS_13TeV=0.00109),
    },
    "mZprime-4300" : {
        "CrossSection" : XSValues(XS_13TeV=0.0008757),
    },
    "mZprime-4400" : {
        "CrossSection" : XSValues(XS_13TeV=0.0007037),
    },
    "mZprime-4500" : {
        "CrossSection" : XSValues(XS_13TeV=0.0005655),
    },
    "mZprime-4600" : {
        "CrossSection" : XSValues(XS_13TeV=0.0004544),
    },
    "mZprime-4700" : {
        "CrossSection" : XSValues(XS_13TeV=0.0003652),
    },
    "mZprime-4800" : {
        "CrossSection" : XSValues(XS_13TeV=0.0002934),
    },
    "mZprime-4900" : {
        "CrossSection" : XSValues(XS_13TeV=0.0002358),
    },
    "mZprime-5000" : {
        "CrossSection" : XSValues(XS_13TeV=0.0001895),
    },
    "mZprime-5100" : {
        "CrossSection" : XSValues(XS_13TeV=0.0001523),
    },
    # Full t-channel cross section
    # now recalculated: including matching/merging efficiency but deliberately NOT downstream filters i.e. Z2 symmetry
    # if pair-production only cross sections are restored, find better naming scheme to disambiguate
    "t-channel_mMed-500_yukawa-1" : {
        "CrossSection" : XSValues(XS_13TeV=4.176e+01),
    },
    "t-channel_mMed-600_yukawa-1" : {
        "CrossSection" : XSValues(XS_13TeV=1.965e+01),
    },
    "t-channel_mMed-700_yukawa-1" : {
        "CrossSection" : XSValues(XS_13TeV=1.038e+01),
    },
    "t-channel_mMed-800_yukawa-1" : {
        "CrossSection" : XSValues(XS_13TeV=6.006e+00),
    },
    "t-channel_mMed-900_yukawa-1" : {
        "CrossSection" : XSValues(XS_13TeV=3.717e+00),
    },
    "t-channel_mMed-1000_yukawa-1" : {
        "CrossSection" : XSValues(XS_13TeV=2.413e+00),
    },
    "t-channel_mMed-1500_yukawa-1" : {
        "CrossSection" : XSValues(XS_13TeV=4.832e-01),
    },
    "t-channel_mMed-2000_yukawa-1" : {
        "CrossSection" : XSValues(XS_13TeV=1.634e-01),
    },
    "t-channel_mMed-2500_yukawa-1" : {
        "CrossSection" : XSValues(XS_13TeV=7.178e-02),
    },
    "t-channel_mMed-3000_yukawa-1" : {
        "CrossSection" : XSValues(XS_13TeV=3.603e-02),
    },
    "t-channel_mMed-3500_yukawa-1" : {
        "CrossSection" : XSValues(XS_13TeV=1.999e-02),
    },
    "t-channel_mMed-4000_yukawa-1" : {
        "CrossSection" : XSValues(XS_13TeV=1.185e-02),
    },
}

