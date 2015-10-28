import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-625_mLSP-400to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/30000/020498CC-6566-E511-919A-00259073E37C.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-625_mLSP-400to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/30000/1263B1CB-6566-E511-836C-7845C4FC3A67.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-625_mLSP-400to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/30000/12A634CE-6566-E511-8764-00259073E488.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-625_mLSP-400to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/30000/1A3EC4D0-6566-E511-BF24-00266CF9B034.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-625_mLSP-400to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/30000/2A10F6CB-6566-E511-AFEB-002590747DF0.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-625_mLSP-400to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/30000/2EC7C0CD-6566-E511-AADE-00259073E34A.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-625_mLSP-400to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/30000/325246D2-6566-E511-A493-00266CFAE7D0.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-625_mLSP-400to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/30000/32F88FCE-6566-E511-A2C1-00266CF9B5D0.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-625_mLSP-400to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/30000/3E377AE3-6666-E511-AF17-3417EBE64C51.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-625_mLSP-400to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/30000/42A16ED2-6566-E511-AF0B-00266CFAEC8C.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-625_mLSP-400to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/30000/4EAB54CC-6566-E511-A9F9-00259074AEDE.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-625_mLSP-400to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/30000/508909CE-6566-E511-AC2D-00266CFADD94.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-625_mLSP-400to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/30000/58D28AE6-6666-E511-AC6B-3417EBE64C51.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-625_mLSP-400to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/30000/644A06CF-6566-E511-8158-008CFA00317C.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-625_mLSP-400to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/30000/6AF161D0-6566-E511-B7FE-00259073E4AC.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-625_mLSP-400to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/30000/6E30A3CE-6566-E511-9357-00259073E3E4.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-625_mLSP-400to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/30000/7688A3CD-6566-E511-A777-00259074AEAE.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-625_mLSP-400to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/30000/7822BBCE-6566-E511-9ABA-00259073E3E4.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-625_mLSP-400to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/30000/7A5018CE-6566-E511-B5EC-00266CF9BE6C.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-625_mLSP-400to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/30000/7AEBDD1D-6A66-E511-AEA2-3417EBE643DE.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-625_mLSP-400to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/30000/8893BBD9-6566-E511-85CE-20CF305B04F0.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-625_mLSP-400to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/30000/8AE58BD3-6566-E511-B212-00266CF25878.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-625_mLSP-400to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/30000/9EA66CCD-6566-E511-9909-00259073E3AC.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-625_mLSP-400to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/30000/A88764CC-6566-E511-93A7-00259074AEDE.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-625_mLSP-400to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/30000/AAC555CD-6566-E511-870A-00A0D1EE271C.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-625_mLSP-400to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/30000/AE12FBCC-6566-E511-A4A2-00259073E3AC.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-625_mLSP-400to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/30000/B0C7A2CD-6566-E511-83C1-00259074AEAE.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-625_mLSP-400to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/30000/BA88DBD3-6566-E511-966C-00266CF25878.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-625_mLSP-400to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/30000/BE2B6CE6-6666-E511-B055-3417EBE64C51.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-625_mLSP-400to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/30000/C68A5FCE-6566-E511-8A85-00259073E3B2.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-625_mLSP-400to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/30000/C6E53BCE-6566-E511-9599-00259073E488.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-625_mLSP-400to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/30000/CA59F6CD-6566-E511-88F0-00259073E3B2.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-625_mLSP-400to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/30000/CE5424CE-6566-E511-B234-00259073E488.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-625_mLSP-400to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/30000/D0D35CCE-6566-E511-A8FE-3417EBE6495A.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-625_mLSP-400to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/30000/D0DE22CB-6566-E511-8CA7-00259073E390.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-625_mLSP-400to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/30000/DA5CDCD4-6566-E511-8B8C-008CFA00038C.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-625_mLSP-400to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/30000/E21898CD-6566-E511-9D96-00266CF268B8.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-625_mLSP-400to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/30000/E4832FE6-6666-E511-8B02-3417EBE64C51.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-625_mLSP-400to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/30000/F4532FD0-6566-E511-97AE-00266CF9BEF8.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-625_mLSP-400to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/30000/F4C76FCB-6566-E511-B5AE-00259073E3D2.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-625_mLSP-400to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/30000/F651EDCB-6566-E511-A35E-00259073E4BC.root',
       '/store/mc/RunIISpring15FSPremix/SMS-T1bbbb_mGluino-625_mLSP-400to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/MCRUN2_74_V9-v1/30000/FA1F892B-6666-E511-A8F5-3417EBE643DE.root' ] );


secFiles.extend( [
               ] )
