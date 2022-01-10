import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2520000/6EF2F81A-F561-D646-B768-66ABFAB0B079.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/068CC332-D6E4-8742-8C87-0C1BEE5CA668.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/16BD1B80-C32A-5547-8F7C-62045CD3D545.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/2E158777-5BD3-274E-825C-418009B4FF39.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/3161C62C-A41A-4D4C-B79A-498D4D3E99F1.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/3D858BD2-6C89-9340-B222-F27DB3A98144.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/400A44E9-ACBD-E04B-B32A-6F1B865B32E1.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/55C345DA-46C3-204E-A656-7A5F4274E594.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/709B905A-0B3A-EA4D-ADF1-CB219AC8E12D.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/7FED634E-1F80-7A4C-A44C-832A46965C7E.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/819A0489-9AD6-F14F-8365-CF04C587BF3F.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/8B95CB1F-1253-C74B-B133-330BD68F458C.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/8D5BC0D0-C2EF-F544-AD2E-E0C46F0E61EC.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/AEE8880F-3D5E-DE49-A5B7-177E87A18FEE.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/CF6CB6C1-2336-6647-9509-5D8460658D51.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/DECEEBCC-63D6-6944-99C2-CBADFE9CBA49.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/FCF69B78-E56C-E341-A6D1-6D4B96563BCC.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/79A98DB4-4932-2F4D-A9D1-2497FEAC641E.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/AC2ED216-40A5-4547-AE63-E592511D7B88.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/BD0702BE-12AB-2743-AA21-C4627BCA3597.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/C5A2E10B-450D-D34D-9B3E-6C57CEE15EFA.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/270000/0691C2E0-2F4D-824F-8476-C760E7470AA4.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/270000/0E9B2C93-C121-7F45-8EC9-466C53869C04.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/270000/16D78450-7B56-2C4B-953F-16F5BAA4E222.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/270000/32E455E2-9EDF-F94A-9841-841019AE1217.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/270000/3395C6F9-B779-0F49-B04C-D08ACA247D74.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/270000/5632738B-11DE-FC41-87E4-D43C9025E169.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/270000/6A00D74E-BB61-074F-A643-A24A93370503.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/270000/6ADE7517-4D49-AE49-883E-1B62124F5864.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/270000/6D80850B-5B43-954D-9E02-7A64487803D6.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/270000/7241CB19-A6D9-0946-9974-E71EBB29C5B0.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/270000/7BDAAA82-883F-6B48-9360-EC68F7986F16.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/270000/7DCCF117-227C-ED4C-B5FC-CE49F1D74041.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/270000/821BCB04-45E2-B548-9FF7-ABBA0EBD10FD.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/270000/83094B9B-D623-A448-B716-FC02D4AA154C.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/270000/936DCCBA-35E7-CB4F-9F13-2989EB927FB6.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/270000/9DDE59FE-86E2-EA4A-86D4-0F4408BEE31A.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/270000/B01C02DD-76E7-334E-9D74-ED8FF8CBF23E.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/270000/BA17E46C-4840-9D44-8D02-C577C3A21A54.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/270000/C6DFE06F-D4CE-0040-B8D3-6B8412139033.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/270000/C769FB80-0ED1-4547-9E86-20A6BB750A7E.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/270000/E080D9C5-9A2D-0546-9EC5-A267D5031854.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/270000/F94D48E5-6911-B648-AA62-A3CA10231AD5.root',
] )
