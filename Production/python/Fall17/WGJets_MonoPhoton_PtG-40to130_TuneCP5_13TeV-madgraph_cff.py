import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/30000/2410F1B1-9175-E811-BE4F-549F3525C0BC.root',
       '/store/mc/RunIIFall17MiniAODv2/WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/30000/764A8000-9175-E811-A87F-00000086FE80.root',
       '/store/mc/RunIIFall17MiniAODv2/WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/30000/840F5DAF-9175-E811-A5C8-00259055CA34.root',
       '/store/mc/RunIIFall17MiniAODv2/WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/30000/84E1E3CE-E774-E811-ACCD-24BE05C6E591.root',
       '/store/mc/RunIIFall17MiniAODv2/WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/30000/88583219-9275-E811-82E4-0CC47A4C8E38.root',
       '/store/mc/RunIIFall17MiniAODv2/WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/30000/8CD19EC6-9175-E811-9A2F-0CC47AD98F72.root',
       '/store/mc/RunIIFall17MiniAODv2/WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/50000/00928489-9A76-E811-8A3F-0CC47A4D7678.root',
       '/store/mc/RunIIFall17MiniAODv2/WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/50000/020BC3C8-7877-E811-A18B-1CB72C1B65D4.root',
       '/store/mc/RunIIFall17MiniAODv2/WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/50000/042A721C-6B75-E811-BACB-5065F3818281.root',
       '/store/mc/RunIIFall17MiniAODv2/WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/50000/04C3CCA5-7575-E811-98AD-0CC47AA992B0.root',
       '/store/mc/RunIIFall17MiniAODv2/WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/50000/0851A7AF-8B75-E811-B3FF-B8CA3A70A520.root',
       '/store/mc/RunIIFall17MiniAODv2/WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/50000/08986785-C775-E811-B760-A0369F30FFD2.root',
       '/store/mc/RunIIFall17MiniAODv2/WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/50000/0AFE0B32-7A78-E811-90BF-0CC47AF9B2E6.root',
       '/store/mc/RunIIFall17MiniAODv2/WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/50000/0C1B7EC3-A476-E811-83E0-0CC47A4C8E98.root',
       '/store/mc/RunIIFall17MiniAODv2/WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/50000/0ED44757-C876-E811-9C7C-0CC47A4C8E22.root',
       '/store/mc/RunIIFall17MiniAODv2/WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/50000/101E87B3-7A78-E811-9B88-4C79BA1811F3.root',
       '/store/mc/RunIIFall17MiniAODv2/WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/50000/12E36068-7A78-E811-94CE-0CC47AA53D92.root',
       '/store/mc/RunIIFall17MiniAODv2/WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/50000/16274C42-6175-E811-8D2D-B8CA3A70B608.root',
       '/store/mc/RunIIFall17MiniAODv2/WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/50000/186FEF02-AE75-E811-B4EB-5065F37DD4B2.root',
       '/store/mc/RunIIFall17MiniAODv2/WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/50000/18C27FCD-9F76-E811-B436-0CC47A4D7678.root',
       '/store/mc/RunIIFall17MiniAODv2/WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/50000/1A2B0571-9C77-E811-8A63-90E2BACBAA90.root',
       '/store/mc/RunIIFall17MiniAODv2/WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/50000/1C19190F-BF76-E811-99F6-0CC47A4D75F4.root',
       '/store/mc/RunIIFall17MiniAODv2/WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/50000/1E2BAEE6-AC76-E811-8A34-0CC47A7C340E.root',
       '/store/mc/RunIIFall17MiniAODv2/WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/50000/22E85C9F-9C77-E811-96D0-3417EBE465FE.root',
       '/store/mc/RunIIFall17MiniAODv2/WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/50000/26614C5C-D475-E811-9878-A0369F310120.root',
       '/store/mc/RunIIFall17MiniAODv2/WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/50000/2A2C13A2-C675-E811-9DBC-B8CA3A70A5E8.root',
       '/store/mc/RunIIFall17MiniAODv2/WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/50000/2CE0D646-5875-E811-8FDB-A0369F30FFD2.root',
       '/store/mc/RunIIFall17MiniAODv2/WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/50000/2E85B15F-DF76-E811-B2CF-0025905A6110.root',
       '/store/mc/RunIIFall17MiniAODv2/WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/50000/32E21479-9D76-E811-A19D-0CC47A4C8EB0.root',
       '/store/mc/RunIIFall17MiniAODv2/WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/50000/34C14C0B-C675-E811-952E-A0369F30FFD2.root',
       '/store/mc/RunIIFall17MiniAODv2/WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/50000/36A61C0E-B775-E811-9BB7-00000086FE80.root',
       '/store/mc/RunIIFall17MiniAODv2/WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/50000/38DBB333-7A78-E811-94D7-0090FAA58D84.root',
       '/store/mc/RunIIFall17MiniAODv2/WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/50000/3A600283-C175-E811-B127-A0369F3102B6.root',
       '/store/mc/RunIIFall17MiniAODv2/WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/50000/42C1E043-7A78-E811-88F5-0023AEEEB559.root',
       '/store/mc/RunIIFall17MiniAODv2/WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/50000/44DCF026-AE75-E811-91EA-24BE05C60641.root',
       '/store/mc/RunIIFall17MiniAODv2/WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/50000/46A67DE3-AB76-E811-8C82-0CC47A4D75EE.root',
       '/store/mc/RunIIFall17MiniAODv2/WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/50000/4AC2EA2A-9676-E811-A66E-0025905A60E4.root',
       '/store/mc/RunIIFall17MiniAODv2/WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/50000/4ACCF7EC-AD76-E811-8A01-0CC47A4D75EE.root',
       '/store/mc/RunIIFall17MiniAODv2/WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/50000/4E87A094-A475-E811-B9EE-5065F381F262.root',
       '/store/mc/RunIIFall17MiniAODv2/WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/50000/52E00F13-0D77-E811-A3C0-003048CC71C0.root',
       '/store/mc/RunIIFall17MiniAODv2/WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/50000/5699234D-C275-E811-8D03-B8CA3A708F98.root',
       '/store/mc/RunIIFall17MiniAODv2/WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/50000/5A93CED6-A776-E811-AF1C-0025905B85CC.root',
       '/store/mc/RunIIFall17MiniAODv2/WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/50000/5ADD21FB-A976-E811-8C05-0CC47A5FA3BD.root',
       '/store/mc/RunIIFall17MiniAODv2/WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/50000/662BD386-7A78-E811-82C9-0CC47A4C8EA8.root',
       '/store/mc/RunIIFall17MiniAODv2/WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/50000/684D8A23-8276-E811-9F8E-0CC47A4D7692.root',
       '/store/mc/RunIIFall17MiniAODv2/WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/50000/68E66BEC-9777-E811-86DF-0CC47A7C3430.root',
       '/store/mc/RunIIFall17MiniAODv2/WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/50000/6AFC6E63-BB76-E811-8A36-0CC47A4D7644.root',
       '/store/mc/RunIIFall17MiniAODv2/WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/50000/6CE291B0-7A78-E811-9857-801844DEDDC8.root',
       '/store/mc/RunIIFall17MiniAODv2/WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/50000/6E409B07-6776-E811-AEF6-0025905B858C.root',
       '/store/mc/RunIIFall17MiniAODv2/WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/50000/6E56E978-D276-E811-A9E6-0025905B85AA.root',
       '/store/mc/RunIIFall17MiniAODv2/WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/50000/72C4F70C-8776-E811-9191-0CC47A4C8E22.root',
       '/store/mc/RunIIFall17MiniAODv2/WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/50000/7493D14C-8D76-E811-A6D5-0CC47A4C8EB0.root',
       '/store/mc/RunIIFall17MiniAODv2/WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/50000/76A465E4-9A75-E811-85F7-E0071B740D80.root',
       '/store/mc/RunIIFall17MiniAODv2/WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/50000/7A6C3174-7A78-E811-8544-0242AC1C0504.root',
       '/store/mc/RunIIFall17MiniAODv2/WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/50000/7EF1788C-9C77-E811-913E-002590FD5694.root',
       '/store/mc/RunIIFall17MiniAODv2/WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/50000/8051CFED-CA75-E811-A35F-0CC47AA992AC.root',
       '/store/mc/RunIIFall17MiniAODv2/WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/50000/827B58F3-AF76-E811-926D-44A842B4CC8B.root',
       '/store/mc/RunIIFall17MiniAODv2/WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/50000/8A22B845-7A78-E811-A4E8-90B11CBCFF4E.root',
       '/store/mc/RunIIFall17MiniAODv2/WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/50000/9443CDE2-9E76-E811-B7A8-0CC47A745298.root',
       '/store/mc/RunIIFall17MiniAODv2/WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/50000/96723733-7A78-E811-98E2-0CC47AFC3C7C.root',
       '/store/mc/RunIIFall17MiniAODv2/WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/50000/9684A699-AD76-E811-A173-EC0D9A822636.root',
       '/store/mc/RunIIFall17MiniAODv2/WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/50000/9A3E4439-9575-E811-B54D-00000086FE80.root',
       '/store/mc/RunIIFall17MiniAODv2/WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/50000/9E30F82D-B976-E811-8F4D-FA163E8FA495.root',
       '/store/mc/RunIIFall17MiniAODv2/WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/50000/9E61FF64-7A78-E811-8FCC-0CC47AD98D06.root',
       '/store/mc/RunIIFall17MiniAODv2/WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/50000/A2A99AC9-7B76-E811-BAB9-0CC47A4D7690.root',
       '/store/mc/RunIIFall17MiniAODv2/WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/50000/A2B5FE61-CD76-E811-8BF6-0CC47A78A2F6.root',
       '/store/mc/RunIIFall17MiniAODv2/WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/50000/AE2BE3BD-C575-E811-B452-0CC47AD9901C.root',
       '/store/mc/RunIIFall17MiniAODv2/WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/50000/AEDF3367-A975-E811-838C-24BE05C38C91.root',
       '/store/mc/RunIIFall17MiniAODv2/WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/50000/B0A38CC0-9F75-E811-8A3C-00000086FE80.root',
       '/store/mc/RunIIFall17MiniAODv2/WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/50000/B0A8B17B-A576-E811-9457-1C6A7A26C9A7.root',
       '/store/mc/RunIIFall17MiniAODv2/WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/50000/B0CCE9F9-5C76-E811-92A6-0025905A6080.root',
       '/store/mc/RunIIFall17MiniAODv2/WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/50000/B219BF10-9076-E811-880A-0025905A48BA.root',
       '/store/mc/RunIIFall17MiniAODv2/WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/50000/BE6420FB-9B77-E811-B43C-00259021A262.root',
       '/store/mc/RunIIFall17MiniAODv2/WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/50000/BE778DBB-BC75-E811-A062-24BE05BD62A2.root',
       '/store/mc/RunIIFall17MiniAODv2/WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/50000/C08450AF-7B78-E811-936E-1866DA87AC15.root',
       '/store/mc/RunIIFall17MiniAODv2/WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/50000/C2C46AF6-A776-E811-8786-0CC47A4D7634.root',
       '/store/mc/RunIIFall17MiniAODv2/WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/50000/C42477EF-A476-E811-826B-0025905B8604.root',
       '/store/mc/RunIIFall17MiniAODv2/WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/50000/C8EBACBE-9C77-E811-AE3A-0025900EAB5E.root',
       '/store/mc/RunIIFall17MiniAODv2/WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/50000/D0951E49-7A78-E811-A8F5-002590E7DE20.root',
       '/store/mc/RunIIFall17MiniAODv2/WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/50000/D60A2E17-7976-E811-8085-00266CF85F70.root',
       '/store/mc/RunIIFall17MiniAODv2/WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/50000/D815109D-8B76-E811-AC22-40F2E9C6ADC0.root',
       '/store/mc/RunIIFall17MiniAODv2/WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/50000/DA592B02-E475-E811-9F03-FA163E385EBB.root',
       '/store/mc/RunIIFall17MiniAODv2/WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/50000/DAFC3EDD-9B77-E811-830B-6CC2173C39E0.root',
       '/store/mc/RunIIFall17MiniAODv2/WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/50000/DEFE6898-B176-E811-9BAE-0CC47A4C8ED8.root',
       '/store/mc/RunIIFall17MiniAODv2/WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/50000/E0820222-7A78-E811-90F8-FA163E05F0A4.root',
       '/store/mc/RunIIFall17MiniAODv2/WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/50000/E2C47FD6-9776-E811-910C-0CC47A4D7678.root',
       '/store/mc/RunIIFall17MiniAODv2/WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/50000/E631D07C-9476-E811-9A2F-0CC47A4C8EB0.root',
       '/store/mc/RunIIFall17MiniAODv2/WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/50000/E89E0477-A676-E811-A387-0025905A6082.root',
       '/store/mc/RunIIFall17MiniAODv2/WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/50000/E8E30CBB-7E76-E811-8BE0-0025905B85FC.root',
       '/store/mc/RunIIFall17MiniAODv2/WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/50000/EAE7B204-6F77-E811-A617-18DED7C60DEB.root',
       '/store/mc/RunIIFall17MiniAODv2/WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/50000/EE5EE04A-7A78-E811-865A-34E6D7E38781.root',
       '/store/mc/RunIIFall17MiniAODv2/WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/50000/F4067721-A276-E811-B242-0025905B8572.root',
       '/store/mc/RunIIFall17MiniAODv2/WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/50000/F49EBA4E-C275-E811-8F2C-E0071B7A3540.root',
       '/store/mc/RunIIFall17MiniAODv2/WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/50000/F88CCCB7-7776-E811-88C8-0CC47A78A408.root',
       '/store/mc/RunIIFall17MiniAODv2/WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/50000/F8DED5A4-C175-E811-8589-5065F381A282.root',
       '/store/mc/RunIIFall17MiniAODv2/WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/50000/FA64DD76-7B78-E811-A3CE-A4BF0126D1BB.root',
       '/store/mc/RunIIFall17MiniAODv2/WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/50000/FAF31849-7A78-E811-ADAC-3417EBE528B2.root',
       '/store/mc/RunIIFall17MiniAODv2/WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/90000/063FD062-7D70-E811-9676-008CFA11137C.root',
       '/store/mc/RunIIFall17MiniAODv2/WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/90000/0CBAD572-6E66-E811-95BA-24BE05BDCEF1.root',
       '/store/mc/RunIIFall17MiniAODv2/WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/90000/0CE50F68-7D70-E811-A5A1-0CC47A4D768C.root',
       '/store/mc/RunIIFall17MiniAODv2/WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/90000/22AFEE80-7D70-E811-AD7A-A0369FC52390.root',
       '/store/mc/RunIIFall17MiniAODv2/WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/90000/44B087C4-7D70-E811-8554-AC1F6B0DE3F8.root',
       '/store/mc/RunIIFall17MiniAODv2/WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/90000/4632727E-7D70-E811-9F61-90E2BACBAA90.root',
       '/store/mc/RunIIFall17MiniAODv2/WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/90000/4C9FB464-7D70-E811-8BED-001E67DFFB86.root',
       '/store/mc/RunIIFall17MiniAODv2/WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/90000/4CB183BF-7D70-E811-9730-001E6779266A.root',
       '/store/mc/RunIIFall17MiniAODv2/WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/90000/52424E68-7D70-E811-BB99-0CC47AD98D10.root',
       '/store/mc/RunIIFall17MiniAODv2/WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/90000/5A299181-7D70-E811-A0FD-0CC47A1DF60C.root',
       '/store/mc/RunIIFall17MiniAODv2/WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/90000/9425D038-105C-E811-8D44-24BE05C63741.root',
       '/store/mc/RunIIFall17MiniAODv2/WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/90000/C0F40D79-7D70-E811-A8BE-0CC47A7E69D8.root',
       '/store/mc/RunIIFall17MiniAODv2/WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/90000/EA5A9B5B-7D70-E811-A7CB-00000086FE80.root',
       '/store/mc/RunIIFall17MiniAODv2/WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/90000/EAFBFDC0-7D70-E811-8F56-509A4C833A2A.root',
       '/store/mc/RunIIFall17MiniAODv2/WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/90000/F0FD0ADB-DE67-E811-A94B-0025905A60F2.root',
] )