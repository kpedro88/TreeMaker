import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/100000/01233BC7-74AE-3D48-88B1-F2D885EF9296.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/100000/03942B09-ED6D-5E45-B811-379A8C77FEF4.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/100000/14974096-2A2A-5142-9496-23E9DF2CE835.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/100000/1F57DD29-6496-2F47-B5B7-E3970A46C40D.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/100000/28F168B7-27E3-7741-8B13-5A209FF41CBB.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/100000/2DD11CEE-4F53-5B49-A32D-4B8D29E9C17C.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/100000/469119EC-EFEB-2A4F-B8AA-F31AACE28E09.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/100000/59A144DA-EAF7-BA45-83FC-CA4546FDFAB5.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/100000/66D0C0BE-E1B9-9243-B36E-0F7CFAEE0E0F.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/100000/6832BA07-727B-1E47-9788-46161CD31DB3.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/100000/9373FB07-48D5-1B4A-8356-254EB58C48EE.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/100000/9BE61F92-5578-1B46-AE66-BC9A4BA7534A.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/100000/D398EB5B-E61B-CB4A-99F8-E4EAF6016AB2.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/100000/E11B5CCB-6426-684E-8FAB-F7BE2A7C4D00.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/100000/E6B2AD23-E623-7542-BCCC-9350D45DB87C.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/100000/FB87DA8B-1F11-B543-B886-A6294DC7C822.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/100000/FD00C2D4-B240-B445-890E-AF1F955417C1.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/230000/29FABF11-F4EC-A843-9835-8B6F1882970F.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/230000/8D486B20-58FB-AE4A-90FF-F1F43598849E.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/2430000/365153F7-40C4-FE4B-82F1-6E4D7FCFB573.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/2430000/8739FB92-F7A9-F640-B8A9-CF83E8E2FD68.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/2430000/E5412DC2-75D4-604B-8C24-1C130F69F8C8.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/250000/0C69A91D-3C73-0449-9F8A-FE0A93D3D3E8.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/250000/1ADA1DB1-1C94-FA4E-A093-041C10C338D0.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/250000/1CA34498-C70E-C64B-8961-AA206CED86F9.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/250000/246CCBA8-15CB-824A-A469-C33788BADCCA.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/250000/2A9B12BD-9619-1242-A0C1-486A2DF7A272.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/250000/322B07B8-810D-6C45-B152-9662D1715A6D.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/250000/3B3A7D7C-6146-C44D-AF39-0F7BF16F94B1.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/250000/433C17DD-79D1-D443-A693-AE4155F1EB00.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/250000/4493959E-DB09-6E48-8A41-9DFD86094264.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/250000/659F4371-F141-4542-A127-4E5197D5A410.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/250000/715D0AD6-47C2-E549-9A9D-E13DA06B1D3D.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/250000/84D42EA5-B4F6-5D40-AAFF-DAC0B39F646A.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/250000/8F9A8DE8-FB55-5043-96A6-46EC4CD33577.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/250000/92089076-16F9-D445-86BD-E796E1907DCC.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/250000/92C7CB3B-9F91-4E40-B09F-3AE75FB33AE8.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/250000/93186758-943E-F844-9DAD-1C9C99A7F6DE.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/250000/9739D211-0DDD-5F48-B46A-B081907E5DD0.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/250000/A3CB8013-8E31-6B42-8B3B-7041F8B86FF1.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/250000/A6D7523A-75DA-BC47-8540-78BE5DAB4716.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/250000/B6AE85C1-46B6-8943-9606-10DFECC67DC2.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/250000/BCCE5AE1-7C12-1841-9368-19CC4C1F7496.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/250000/BF7ACB09-0AFE-4649-9851-14908DE1E494.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/250000/C59CC52E-8718-DF47-9603-FD03EE0EA121.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/250000/C5EFE905-6C0A-9642-A460-0D61FB3F378B.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/250000/C992F85F-52E3-FD46-B5DE-1407D70A12F3.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/250000/D061C313-4F21-3341-9184-F044165C7D02.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/250000/D1EA9E50-70B5-3844-B9FB-ACDFE52ABC77.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/250000/D4A15CAB-23D4-D54D-B4B4-16F43DEF9F74.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/250000/DE0B842A-04DD-0C40-AD05-50097A48CC45.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/250000/E45BC177-AD85-6C46-9139-2AB7B82F1EBD.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/2510000/38C55F5C-0A3E-1145-9F14-7091A6431D0D.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/2510000/4F277BC9-EF97-094E-BC52-B550C18B432A.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/2510000/6A653AAD-CECD-F845-9BAB-A2BA8677009E.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/40000/38803C06-D53B-A84D-B540-93C34EADD32F.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/40000/3AD6AE1E-B722-014F-A886-34672B7D2726.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/40000/549C3E52-CC5B-5040-B6F6-9BF080E15386.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/40000/693EA5B1-6A9A-B042-BB74-4D5726D191C3.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/40000/7354B911-DCE5-7B4B-ACF5-983CB38D6AE0.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/40000/778398E8-36EB-DE4A-BD7E-86B5C3A0A029.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/40000/7B751C76-48BF-3540-8C99-CEDB020C42BA.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/40000/9924F23A-1389-4749-ADD6-9D59B72B4C27.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/40000/9991350F-904E-4741-9D68-06B0D6D2053F.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/40000/C1A295AD-9029-D34F-8623-E921FEDBD25D.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/40000/D246D0AF-F9EE-A040-A031-ABC0C53748AF.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/40000/F43374DC-B729-DD43-8D94-5CF88FA60A49.root',
] )
