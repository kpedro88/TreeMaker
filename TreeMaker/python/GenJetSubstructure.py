# based on https://github.com/cms-svj/SVJProduction/blob/Run2_UL/python/genJetSubstructure.py
import FWCore.ParameterSet.Config as cms

# helper function
def addModule(mod, process, prefix, suffix, base, module):
    if not base in mod:
        mod[base] = prefix+base+suffix
        setattr(process, mod[base], module)
    return mod, process

# a mini jet toolbox for genjets
def addGenSub(process, size, prefix, suffix, src, mod=None):
    if mod is None:
        mod = {}

    from RecoJets.Configuration.RecoGenJets_cff import ak4GenJets
    mod, process = addModule(mod, process, prefix, suffix,
        "GenJets",
        ak4GenJets.clone(
            rParam = size,
            src = src,
        ),
    )
    mod, process = addModule(mod, process, prefix, suffix,
        "GenJetsArea",
        getattr(process,mod["GenJets"]).clone(
            doAreaFastjet = True,
        ),
    )
    mod, process = addModule(mod, process, prefix, suffix,
        "GenJetsSoftDrop",
        getattr(process,mod["GenJetsArea"]).clone(
            R0 = cms.double(size),
            useSoftDrop = cms.bool(True),
            zcut = cms.double(0.1),
            beta = cms.double(0.0),
            useExplicitGhosts = cms.bool(True),
            writeCompound = cms.bool(True),
            jetCollInstanceName = cms.string("SubJets"),
        ),
    )
    from RecoJets.JetProducers.ECFAdder_cfi import ECFAdder
    mod, process = addModule(mod, process, prefix, suffix,
        "ECFNbeta1",
        ECFAdder.clone(
            src = mod["GenJetsSoftDrop"],
            ecftype = "N",
        ),
    )
    mod, process = addModule(mod, process, prefix, suffix,
        "ECFNbeta2",
        getattr(process,mod["ECFNbeta1"]).clone(
            alpha = 2.0,
            beta = 2.0,
        ),
    )
    mod, process = addModule(mod, process, prefix, suffix,
        "GenJetsPacked",
        cms.EDProducer("GenJetSubstructurePacker",
            jetSrc = cms.InputTag(mod["GenJetsArea"]),
            distMax = cms.double(size),
            algoTag = cms.InputTag(mod["GenJetsSoftDrop"]),
           	algoFloatTags = cms.VInputTag(
				cms.InputTag(mod["ECFNbeta1"],"ecfN1"),
				cms.InputTag(mod["ECFNbeta1"],"ecfN2"),
				cms.InputTag(mod["ECFNbeta1"],"ecfN3"),
				cms.InputTag(mod["ECFNbeta2"],"ecfN1"),
				cms.InputTag(mod["ECFNbeta2"],"ecfN2"),
				cms.InputTag(mod["ECFNbeta2"],"ecfN3"),
			),
			algoFloatLabels = cms.vstring(
				"ecfN1b1",
				"ecfN2b1",
				"ecfN3b1",
				"ecfN1b2",
				"ecfN2b2",
				"ecfN3b2",
			)
        ),
    )
    return process
