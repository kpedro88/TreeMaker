import FWCore.ParameterSet.Config as cms

mt2Producer = cms.EDProducer('Mt2Producer',
JetTag_               = cms.InputTag('JetTag'),
MetTag_               = cms.InputTag('MetTag'),
)
