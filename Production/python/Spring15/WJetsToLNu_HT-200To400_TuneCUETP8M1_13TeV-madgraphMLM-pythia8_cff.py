import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15DR74/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/00ED169D-D506-E511-A61E-001CC47C7092.root',
       '/store/mc/RunIISpring15DR74/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/021B1A78-3106-E511-B3C5-0025905B858A.root',
       '/store/mc/RunIISpring15DR74/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/02C5CDA6-3106-E511-AAA2-002618943954.root',
       '/store/mc/RunIISpring15DR74/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/04E03FBE-3F06-E511-A319-0025904A9430.root',
       '/store/mc/RunIISpring15DR74/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/06DF8F11-3206-E511-929A-0CC47A009E22.root',
       '/store/mc/RunIISpring15DR74/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/0C40A476-2406-E511-BFE4-0025905A6056.root',
       '/store/mc/RunIISpring15DR74/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/10959D74-2406-E511-89F6-0025905964BA.root',
       '/store/mc/RunIISpring15DR74/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/12A5C4FC-E807-E511-8839-B083FED43141.root',
       '/store/mc/RunIISpring15DR74/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/12FC7F6C-3106-E511-8A9B-0025905B858C.root',
       '/store/mc/RunIISpring15DR74/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/1478DCF5-2C06-E511-9646-00261894383B.root',
       '/store/mc/RunIISpring15DR74/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/1C384C96-D106-E511-A5DE-001F2907EE22.root',
       '/store/mc/RunIISpring15DR74/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/2A156C77-2C06-E511-99F8-0025905A608A.root',
       '/store/mc/RunIISpring15DR74/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/2A4B82E8-3206-E511-8DB1-0CC47A009148.root',
       '/store/mc/RunIISpring15DR74/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/2C046B3B-3206-E511-BFDB-90B11C27EA38.root',
       '/store/mc/RunIISpring15DR74/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/2CAE317B-3106-E511-B8CA-0025905B855E.root',
       '/store/mc/RunIISpring15DR74/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/2E7EC785-2806-E511-BDDE-0025905A607A.root',
       '/store/mc/RunIISpring15DR74/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/2E8E41A5-E206-E511-93D2-782BCB67826E.root',
       '/store/mc/RunIISpring15DR74/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/2E8F3890-3206-E511-ABB5-003048344A90.root',
       '/store/mc/RunIISpring15DR74/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/30084127-2C06-E511-AF97-0025905A606A.root',
       '/store/mc/RunIISpring15DR74/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/30E2E074-2806-E511-A523-00261894383B.root',
       '/store/mc/RunIISpring15DR74/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/323084C1-3306-E511-988F-003048FFD740.root',
       '/store/mc/RunIISpring15DR74/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/36C93F1D-2506-E511-89FD-0025905B8590.root',
       '/store/mc/RunIISpring15DR74/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/381DBAB5-2506-E511-8843-0025905B859E.root',
       '/store/mc/RunIISpring15DR74/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/38BD103A-3206-E511-886C-002590593878.root',
       '/store/mc/RunIISpring15DR74/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/38D1C1BF-2806-E511-BFFA-0025905964BA.root',
       '/store/mc/RunIISpring15DR74/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/3C2E4520-2506-E511-97E9-0025905A60DA.root',
       '/store/mc/RunIISpring15DR74/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/40A770A5-3D06-E511-BEC4-0025905A6094.root',
       '/store/mc/RunIISpring15DR74/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/42B090B7-3206-E511-AB80-842B2B7682C7.root',
       '/store/mc/RunIISpring15DR74/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/46F8BEBA-2806-E511-B856-0025905A613C.root',
       '/store/mc/RunIISpring15DR74/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/4871D1A4-3D06-E511-A9C7-003048FFCB84.root',
       '/store/mc/RunIISpring15DR74/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/48A6B07D-2806-E511-B4E1-0025905A6094.root',
       '/store/mc/RunIISpring15DR74/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/4CA1B6FB-2C06-E511-A15B-0025905A608A.root',
       '/store/mc/RunIISpring15DR74/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/50125FFF-3D06-E511-B67E-0025905964BC.root',
       '/store/mc/RunIISpring15DR74/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/5096BCA5-3D06-E511-A609-0025905B858C.root',
       '/store/mc/RunIISpring15DR74/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/54462E20-2506-E511-BD09-002590593902.root',
       '/store/mc/RunIISpring15DR74/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/5A9E0B9A-1407-E511-96A4-0025901AC3CE.root',
       '/store/mc/RunIISpring15DR74/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/5AC45DD8-CC06-E511-AC90-A0040420FE80.root',
       '/store/mc/RunIISpring15DR74/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/5C58A573-2C06-E511-9EEF-0025905A613C.root',
       '/store/mc/RunIISpring15DR74/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/601B1D07-C707-E511-8E85-00259021A526.root',
       '/store/mc/RunIISpring15DR74/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/64D88576-B007-E511-83A9-00221982AF2D.root',
       '/store/mc/RunIISpring15DR74/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/662199A0-E706-E511-AF19-000F532734B0.root',
       '/store/mc/RunIISpring15DR74/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/666EE070-4206-E511-8583-00259074AE8C.root',
       '/store/mc/RunIISpring15DR74/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/66F4FDE6-2D06-E511-8493-00259073E33A.root',
       '/store/mc/RunIISpring15DR74/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/684650B7-2506-E511-B875-0025905A608C.root',
       '/store/mc/RunIISpring15DR74/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/6A56E404-AE07-E511-BFC8-D4AE5269DC07.root',
       '/store/mc/RunIISpring15DR74/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/6E108AA0-3206-E511-9DC2-842B2B7680DF.root',
       '/store/mc/RunIISpring15DR74/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/6E83E3F4-8307-E511-B734-02163E011A81.root',
       '/store/mc/RunIISpring15DR74/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/72273F0B-C407-E511-8111-00074305CDB6.root',
       '/store/mc/RunIISpring15DR74/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/72745506-C507-E511-A8D8-00259057461A.root',
       '/store/mc/RunIISpring15DR74/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/742BD661-3106-E511-818C-0025905A4964.root',
       '/store/mc/RunIISpring15DR74/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/74CA91BA-2806-E511-B632-0025905A60B0.root',
       '/store/mc/RunIISpring15DR74/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/76B3BB60-3106-E511-8A80-0025905A612E.root',
       '/store/mc/RunIISpring15DR74/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/7C3C5E40-F107-E511-9775-001F29097068.root',
       '/store/mc/RunIISpring15DR74/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/7C44A945-CC06-E511-8523-0025905A6092.root',
       '/store/mc/RunIISpring15DR74/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/7C5503F9-D006-E511-8265-002590207C28.root',
       '/store/mc/RunIISpring15DR74/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/8084191D-F506-E511-91EC-003048947DA4.root',
       '/store/mc/RunIISpring15DR74/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/82371AB5-E707-E511-A077-0025901D08EC.root',
       '/store/mc/RunIISpring15DR74/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/82E9EA2B-CC06-E511-BE1C-008CFA1C6564.root',
       '/store/mc/RunIISpring15DR74/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/8499A3D4-5906-E511-8E1C-0CC47A13CFC0.root',
       '/store/mc/RunIISpring15DR74/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/863DC91F-2506-E511-A82E-0025905A48D8.root',
       '/store/mc/RunIISpring15DR74/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/86A0D49F-3106-E511-BBF4-0CC47A13D052.root',
       '/store/mc/RunIISpring15DR74/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/8C007201-E006-E511-B641-001E67A3F92F.root',
       '/store/mc/RunIISpring15DR74/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/8C3D9603-2D06-E511-A723-0025905964B2.root',
       '/store/mc/RunIISpring15DR74/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/8E2CD108-0F07-E511-B586-003048F5B300.root',
       '/store/mc/RunIISpring15DR74/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/8E576703-3106-E511-93BA-002618943809.root',
       '/store/mc/RunIISpring15DR74/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/90B37A89-BF07-E511-BF2A-008CFA197D38.root',
       '/store/mc/RunIISpring15DR74/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/9223FFF9-2C06-E511-9468-0025905A60BE.root',
       '/store/mc/RunIISpring15DR74/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/940CAC39-3206-E511-8032-0025905A6080.root',
       '/store/mc/RunIISpring15DR74/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/940F6FB0-3106-E511-9C12-002618943845.root',
       '/store/mc/RunIISpring15DR74/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/96077FA1-3106-E511-87B9-0CC47A13CB36.root',
       '/store/mc/RunIISpring15DR74/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/962E2691-3206-E511-B6EC-003048341B26.root',
       '/store/mc/RunIISpring15DR74/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/98B01F27-DB08-E511-BBE8-A0369F3102F6.root',
       '/store/mc/RunIISpring15DR74/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/9C285D52-3F06-E511-A2A8-0025901D08BC.root',
       '/store/mc/RunIISpring15DR74/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/9C8EE625-2C06-E511-9E46-0025905A608A.root',
       '/store/mc/RunIISpring15DR74/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/A02443C3-3306-E511-89DA-003048FFCB9E.root',
       '/store/mc/RunIISpring15DR74/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/A20474BE-D406-E511-89D8-6CC2173D5F20.root',
       '/store/mc/RunIISpring15DR74/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/A22049FE-3006-E511-9DC2-0026189438B1.root',
       '/store/mc/RunIISpring15DR74/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/A2C7A49A-3206-E511-8114-003048341B00.root',
       '/store/mc/RunIISpring15DR74/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/A435E4BB-2506-E511-99B9-0025905A60E4.root',
       '/store/mc/RunIISpring15DR74/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/A61ABC00-CC06-E511-9186-0002C92DB46C.root',
       '/store/mc/RunIISpring15DR74/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/A8BC4487-D706-E511-BC61-002590552126.root',
       '/store/mc/RunIISpring15DR74/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/AA060656-D306-E511-866E-001E67A3FB91.root',
       '/store/mc/RunIISpring15DR74/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/AA8B178B-2B06-E511-A499-0025905B857C.root',
       '/store/mc/RunIISpring15DR74/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/AE828E4E-3206-E511-A4B3-0025901D16AC.root',
       '/store/mc/RunIISpring15DR74/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/AE84A3BC-2506-E511-95FB-002590596486.root',
       '/store/mc/RunIISpring15DR74/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/B032D4BA-2806-E511-8247-00259073E53E.root',
       '/store/mc/RunIISpring15DR74/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/B04B8BEA-2D06-E511-820D-00259073E470.root',
       '/store/mc/RunIISpring15DR74/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/B2A147D8-5F09-E511-9865-00304867FD63.root',
       '/store/mc/RunIISpring15DR74/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/B2CD7456-3106-E511-8ACE-00261894384F.root',
       '/store/mc/RunIISpring15DR74/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/B4ECCB4E-3E06-E511-89C2-0CC47A13CFC0.root',
       '/store/mc/RunIISpring15DR74/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/B64BDC27-B107-E511-B216-00269E95B17C.root',
       '/store/mc/RunIISpring15DR74/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/B86A60A4-3106-E511-8D09-00238BCE4650.root',
       '/store/mc/RunIISpring15DR74/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/B8E3F1F4-CB06-E511-9BD7-0002C952E782.root',
       '/store/mc/RunIISpring15DR74/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/BA41E77F-C108-E511-9671-00259074AE9A.root',
       '/store/mc/RunIISpring15DR74/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/BEB11A41-F908-E511-96D1-002618943821.root',
       '/store/mc/RunIISpring15DR74/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/C0C3D73D-0A07-E511-8987-003048F5B2A0.root',
       '/store/mc/RunIISpring15DR74/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/C0D62A1D-2506-E511-9F50-0025905A613C.root',
       '/store/mc/RunIISpring15DR74/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/C236D986-2806-E511-975B-0025905A6118.root',
       '/store/mc/RunIISpring15DR74/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/C2487788-FD06-E511-A30B-0025905A6136.root',
       '/store/mc/RunIISpring15DR74/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/C61144D9-5906-E511-B2BE-0CC47A13CFC0.root',
       '/store/mc/RunIISpring15DR74/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/C6E1FF30-2908-E511-8048-0025905A605E.root',
       '/store/mc/RunIISpring15DR74/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/C8C59671-3106-E511-80FE-0025905A608A.root',
       '/store/mc/RunIISpring15DR74/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/C8EACFBA-2506-E511-A43E-0025905A60B4.root',
       '/store/mc/RunIISpring15DR74/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/CA2F8183-2806-E511-80EF-002618943924.root',
       '/store/mc/RunIISpring15DR74/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/CC24A012-0F07-E511-BB91-00259073E502.root',
       '/store/mc/RunIISpring15DR74/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/CE557BB1-3F06-E511-85AE-0025901AFEA2.root',
       '/store/mc/RunIISpring15DR74/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/D25C26E1-CC06-E511-9954-0025905A6122.root',
       '/store/mc/RunIISpring15DR74/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/D280E3A5-3106-E511-AA5F-0025905A611C.root',
       '/store/mc/RunIISpring15DR74/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/D2ABA6C0-2806-E511-95B6-0025905A60CA.root',
       '/store/mc/RunIISpring15DR74/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/D49AC437-E306-E511-B20D-003048947CBC.root',
       '/store/mc/RunIISpring15DR74/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/D88F78A1-3106-E511-AD50-0025905A60A0.root',
       '/store/mc/RunIISpring15DR74/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/D8A143FE-3D06-E511-B902-0025905B8596.root',
       '/store/mc/RunIISpring15DR74/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/D8A800B7-2506-E511-B92A-0025905AA9CC.root',
       '/store/mc/RunIISpring15DR74/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/DC0BA944-B407-E511-A2E6-28924A33AFC2.root',
       '/store/mc/RunIISpring15DR74/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/DC537354-3E06-E511-83F1-003048F5ADEA.root',
       '/store/mc/RunIISpring15DR74/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/E2EFE008-2A06-E511-9CA5-00259073E456.root',
       '/store/mc/RunIISpring15DR74/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/E40B2884-2B06-E511-A0BE-0025905B8596.root',
       '/store/mc/RunIISpring15DR74/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/E425F413-E206-E511-AE47-6C3BE5B5B078.root',
       '/store/mc/RunIISpring15DR74/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/E628515C-2E06-E511-BF28-0025905B85D8.root',
       '/store/mc/RunIISpring15DR74/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/E68D4AFA-2C06-E511-8F6B-0025905A6070.root',
       '/store/mc/RunIISpring15DR74/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/E80A730A-3E06-E511-9C35-0CC47A13D2BE.root',
       '/store/mc/RunIISpring15DR74/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/E8197D55-E306-E511-8343-20CF3019DF10.root',
       '/store/mc/RunIISpring15DR74/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/E81E79A0-E706-E511-AA2D-782BCB408B63.root',
       '/store/mc/RunIISpring15DR74/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/EC203660-2E06-E511-9A7D-0025905A610C.root',
       '/store/mc/RunIISpring15DR74/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/EC25AD8A-3206-E511-A93A-000F530E4780.root',
       '/store/mc/RunIISpring15DR74/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/EE4493C0-3106-E511-85B4-001EC9B22502.root',
       '/store/mc/RunIISpring15DR74/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/EE8FC79E-E206-E511-9C0A-00221982C62E.root',
       '/store/mc/RunIISpring15DR74/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/F093B177-D306-E511-AE70-6CC2173D5F20.root',
       '/store/mc/RunIISpring15DR74/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/F0D3B973-D907-E511-A044-90B11C08AD92.root',
       '/store/mc/RunIISpring15DR74/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/F235540D-3E06-E511-87F7-002590CB0B5A.root',
       '/store/mc/RunIISpring15DR74/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/F4C7E906-2A06-E511-9D7B-00259073E442.root',
       '/store/mc/RunIISpring15DR74/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/FAFEF38B-2B06-E511-A238-003048FFD740.root',
       '/store/mc/RunIISpring15DR74/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/FCC403FF-3006-E511-B139-002618943857.root',
       '/store/mc/RunIISpring15DR74/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/FCDDAB2A-B107-E511-8026-A4BADB3CF272.root',
       '/store/mc/RunIISpring15DR74/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/10000/FE0172B0-3106-E511-939E-002618943845.root',
       '/store/mc/RunIISpring15DR74/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/084441D9-F705-E511-9804-90B11C2AAEEC.root',
       '/store/mc/RunIISpring15DR74/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/401D0767-F705-E511-B0FD-00259073E37A.root',
       '/store/mc/RunIISpring15DR74/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/70680368-F705-E511-AF28-00259073E474.root',
       '/store/mc/RunIISpring15DR74/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/82CA66C2-F705-E511-88BF-002590E39D90.root',
       '/store/mc/RunIISpring15DR74/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/D42A6A94-F705-E511-806F-002590E2F5CE.root',
       '/store/mc/RunIISpring15DR74/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/EEF5C684-F705-E511-9359-0025905B8572.root' ] );


secFiles.extend( [
               ] )

