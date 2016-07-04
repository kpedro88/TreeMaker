import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15MiniAODv2/TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/0235B538-676E-E511-8A03-001E67E6F855.root',
       '/store/mc/RunIISpring15MiniAODv2/TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/023DDF06-536E-E511-AAED-02163E012DB3.root',
       '/store/mc/RunIISpring15MiniAODv2/TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/02ADA1C8-9A6E-E511-9AEF-0025902008DC.root',
       '/store/mc/RunIISpring15MiniAODv2/TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/0411BDD9-626E-E511-ACD8-002590200A88.root',
       '/store/mc/RunIISpring15MiniAODv2/TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/0656E63A-7D6E-E511-9A8E-02163E00C3FE.root',
       '/store/mc/RunIISpring15MiniAODv2/TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/0AC2C2B8-7B6E-E511-97C3-02163E016908.root',
       '/store/mc/RunIISpring15MiniAODv2/TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/12AE4D7E-5A6E-E511-ACED-001E67E71CC7.root',
       '/store/mc/RunIISpring15MiniAODv2/TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/1427ADD3-7A6E-E511-AC7F-02163E01679D.root',
       '/store/mc/RunIISpring15MiniAODv2/TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/1A172F08-656E-E511-AB1E-02163E016087.root',
       '/store/mc/RunIISpring15MiniAODv2/TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/1AC01C52-7F6E-E511-83F0-02163E00EA56.root',
       '/store/mc/RunIISpring15MiniAODv2/TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/1E8C6106-7F6E-E511-9FFB-02163E015FAA.root',
       '/store/mc/RunIISpring15MiniAODv2/TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/1EA01E85-7A6E-E511-A863-02163E00B54A.root',
       '/store/mc/RunIISpring15MiniAODv2/TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/20F76932-7E6E-E511-B011-02163E00BBC0.root',
       '/store/mc/RunIISpring15MiniAODv2/TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/20FAAA35-776F-E511-96BD-001D09FDD6AB.root',
       '/store/mc/RunIISpring15MiniAODv2/TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/223966A1-876F-E511-B092-0025905C96A6.root',
       '/store/mc/RunIISpring15MiniAODv2/TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/241E19B1-886F-E511-9594-0025905C2CA4.root',
       '/store/mc/RunIISpring15MiniAODv2/TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/2445F845-586E-E511-B019-001E67E6F8E6.root',
       '/store/mc/RunIISpring15MiniAODv2/TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/24DF09FB-7E6E-E511-B9D7-02163E010DBF.root',
       '/store/mc/RunIISpring15MiniAODv2/TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/28CA2819-7B6E-E511-97A0-02163E016AD7.root',
       '/store/mc/RunIISpring15MiniAODv2/TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/2EA5F8E7-646E-E511-A9BE-02163E013C11.root',
       '/store/mc/RunIISpring15MiniAODv2/TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/343FB47A-716E-E511-A7A8-0025904B2CA8.root',
       '/store/mc/RunIISpring15MiniAODv2/TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/3A37E091-7B6E-E511-BF32-02163E014FC7.root',
       '/store/mc/RunIISpring15MiniAODv2/TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/3CA8974B-5B6E-E511-8CC8-02163E013F71.root',
       '/store/mc/RunIISpring15MiniAODv2/TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/3CBE9FC9-956F-E511-80ED-28924A33B9AA.root',
       '/store/mc/RunIISpring15MiniAODv2/TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/3E8D6B40-5B6E-E511-B9E8-001E67E71B14.root',
       '/store/mc/RunIISpring15MiniAODv2/TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/40CC8319-7E6E-E511-A2AE-02163E00C051.root',
       '/store/mc/RunIISpring15MiniAODv2/TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/42665253-5C6E-E511-9F59-001E67E71BDC.root',
       '/store/mc/RunIISpring15MiniAODv2/TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/44AE9866-5E6E-E511-9252-0025902008A4.root',
       '/store/mc/RunIISpring15MiniAODv2/TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/463F43F1-7C6E-E511-B49F-02163E010DBF.root',
       '/store/mc/RunIISpring15MiniAODv2/TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/48E82DC5-9A6E-E511-BA42-002590200B74.root',
       '/store/mc/RunIISpring15MiniAODv2/TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/4C910253-7C6E-E511-9E73-02163E00E605.root',
       '/store/mc/RunIISpring15MiniAODv2/TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/4CD7A631-816E-E511-8D37-02163E00F30A.root',
       '/store/mc/RunIISpring15MiniAODv2/TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/4EA7AFA7-7B6E-E511-8976-02163E012EE0.root',
       '/store/mc/RunIISpring15MiniAODv2/TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/564D06EF-7A6E-E511-B409-02163E00CD58.root',
       '/store/mc/RunIISpring15MiniAODv2/TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/5AE3788C-7B6E-E511-AA03-02163E014C03.root',
       '/store/mc/RunIISpring15MiniAODv2/TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/5AE52AD4-7A6E-E511-BD19-02163E00BBC0.root',
       '/store/mc/RunIISpring15MiniAODv2/TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/5CE014AF-546E-E511-ACDC-001E67E6F909.root',
       '/store/mc/RunIISpring15MiniAODv2/TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/620BB481-7A6E-E511-A91F-02163E010DBF.root',
       '/store/mc/RunIISpring15MiniAODv2/TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/6234812B-7B6E-E511-AD39-02163E00BE88.root',
       '/store/mc/RunIISpring15MiniAODv2/TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/66890A8C-876F-E511-93EA-0025905C2CD0.root',
       '/store/mc/RunIISpring15MiniAODv2/TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/68ED7CC8-5A6E-E511-BF09-02163E0151F5.root',
       '/store/mc/RunIISpring15MiniAODv2/TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/6A04FB7C-5A6E-E511-B322-02163E00F36A.root',
       '/store/mc/RunIISpring15MiniAODv2/TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/6C7E13E3-696E-E511-8388-02163E00E618.root',
       '/store/mc/RunIISpring15MiniAODv2/TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/7246EF30-856F-E511-81BF-C4346BC80410.root',
       '/store/mc/RunIISpring15MiniAODv2/TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/7420405F-7B6E-E511-9FCC-02163E015117.root',
       '/store/mc/RunIISpring15MiniAODv2/TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/74351898-5A6E-E511-A88B-02163E00F4D3.root',
       '/store/mc/RunIISpring15MiniAODv2/TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/76ABA760-536E-E511-A8AA-02163E015120.root',
       '/store/mc/RunIISpring15MiniAODv2/TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/783DE74B-716E-E511-978C-001E67C9B1BD.root',
       '/store/mc/RunIISpring15MiniAODv2/TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/7866DDD6-626E-E511-B7BC-001E67396897.root',
       '/store/mc/RunIISpring15MiniAODv2/TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/7898FCD3-646E-E511-83FE-0025902009B0.root',
       '/store/mc/RunIISpring15MiniAODv2/TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/7A6A44DA-7E6E-E511-B968-02163E00AED8.root',
       '/store/mc/RunIISpring15MiniAODv2/TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/7A87E691-7B6E-E511-B47D-02163E014FC7.root',
       '/store/mc/RunIISpring15MiniAODv2/TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/7ECCA63D-676E-E511-A179-002590200A88.root',
       '/store/mc/RunIISpring15MiniAODv2/TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/7EE2E3DA-7B6E-E511-A389-02163E0135F7.root',
       '/store/mc/RunIISpring15MiniAODv2/TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/828644B4-7B6E-E511-9375-02163E00C24B.root',
       '/store/mc/RunIISpring15MiniAODv2/TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/8892DDED-646E-E511-AB2F-02163E00EA1B.root',
       '/store/mc/RunIISpring15MiniAODv2/TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/8A4CDC03-7B6E-E511-917E-02163E014B89.root',
       '/store/mc/RunIISpring15MiniAODv2/TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/8E7B1F5D-5B6E-E511-AF6C-02163E010D06.root',
       '/store/mc/RunIISpring15MiniAODv2/TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/8EB56850-586E-E511-8623-001E67E6F819.root',
       '/store/mc/RunIISpring15MiniAODv2/TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/8EC67D85-5C6E-E511-A697-002590200B14.root',
       '/store/mc/RunIISpring15MiniAODv2/TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/900A269A-5E6E-E511-964A-02163E010DB9.root',
       '/store/mc/RunIISpring15MiniAODv2/TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/909D3087-606E-E511-BCCB-001E673967C5.root',
       '/store/mc/RunIISpring15MiniAODv2/TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/961ECBC4-5B6E-E511-8629-02163E0167B8.root',
       '/store/mc/RunIISpring15MiniAODv2/TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/96299A4B-7D6E-E511-9974-02163E014252.root',
       '/store/mc/RunIISpring15MiniAODv2/TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/96548890-876F-E511-AD86-0025905C96EA.root',
       '/store/mc/RunIISpring15MiniAODv2/TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/A0B7E1D6-626E-E511-9DA2-001E67396897.root',
       '/store/mc/RunIISpring15MiniAODv2/TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/A4364B9A-7B6E-E511-BCBA-02163E012FF2.root',
       '/store/mc/RunIISpring15MiniAODv2/TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/A47EEA1C-7B6E-E511-A920-02163E00F43B.root',
       '/store/mc/RunIISpring15MiniAODv2/TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/A499096A-7B6E-E511-9D55-02163E00E61B.root',
       '/store/mc/RunIISpring15MiniAODv2/TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/A60724C5-9A6E-E511-B974-002590200868.root',
       '/store/mc/RunIISpring15MiniAODv2/TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/A67D6F3C-676E-E511-B6A6-0025902009B0.root',
       '/store/mc/RunIISpring15MiniAODv2/TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/A68ADC7B-716E-E511-B2D8-02163E016740.root',
       '/store/mc/RunIISpring15MiniAODv2/TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/AC1A3ED9-626E-E511-BE51-001E67396D56.root',
       '/store/mc/RunIISpring15MiniAODv2/TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/AC479FF2-476E-E511-B46C-02163E015120.root',
       '/store/mc/RunIISpring15MiniAODv2/TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/AC74EC41-5B6E-E511-B8F8-002590A371AC.root',
       '/store/mc/RunIISpring15MiniAODv2/TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/AEA54B93-5E6E-E511-A1D1-02163E013D8D.root',
       '/store/mc/RunIISpring15MiniAODv2/TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/AEEAEBCB-9A6E-E511-AE93-0025902009A4.root',
       '/store/mc/RunIISpring15MiniAODv2/TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/B2BB3923-7B6E-E511-AD5A-02163E012FB5.root',
       '/store/mc/RunIISpring15MiniAODv2/TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/B43A22E7-7A6E-E511-A500-02163E016942.root',
       '/store/mc/RunIISpring15MiniAODv2/TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/B89F3985-7A6E-E511-88A5-02163E015E68.root',
       '/store/mc/RunIISpring15MiniAODv2/TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/B8CFD2E3-7A6E-E511-9245-02163E015122.root',
       '/store/mc/RunIISpring15MiniAODv2/TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/BC20DC99-7A6E-E511-B40E-02163E00B35D.root',
       '/store/mc/RunIISpring15MiniAODv2/TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/BE9E7543-676E-E511-A6AF-F04DA23BCE4C.root',
       '/store/mc/RunIISpring15MiniAODv2/TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/C00DBC40-676E-E511-9071-001E67398D5E.root',
       '/store/mc/RunIISpring15MiniAODv2/TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/C25DF444-7E6E-E511-8B07-02163E00B54A.root',
       '/store/mc/RunIISpring15MiniAODv2/TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/C696C8BF-476E-E511-A442-02163E00E7D0.root',
       '/store/mc/RunIISpring15MiniAODv2/TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/C82E47BF-7A6E-E511-8D18-02163E00EA56.root',
       '/store/mc/RunIISpring15MiniAODv2/TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/C87175FA-646E-E511-B212-02163E0118D4.root',
       '/store/mc/RunIISpring15MiniAODv2/TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/C8E98A9D-7A6E-E511-A516-02163E00C051.root',
       '/store/mc/RunIISpring15MiniAODv2/TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/CAA63C3C-7F6E-E511-8EC4-02163E00B35D.root',
       '/store/mc/RunIISpring15MiniAODv2/TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/CAD38C45-676E-E511-A2F7-F04DA23BCE4C.root',
       '/store/mc/RunIISpring15MiniAODv2/TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/CCEF3882-5B6E-E511-A3DC-02163E00E7CB.root',
       '/store/mc/RunIISpring15MiniAODv2/TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/D025F6EE-7E6E-E511-A601-02163E01679D.root',
       '/store/mc/RunIISpring15MiniAODv2/TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/D4E0013C-676E-E511-8D28-001E67E6F65C.root',
       '/store/mc/RunIISpring15MiniAODv2/TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/D64B6D4A-716E-E511-A660-0025904B2C78.root',
       '/store/mc/RunIISpring15MiniAODv2/TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/DC185724-7B6E-E511-9E84-02163E00F43B.root',
       '/store/mc/RunIISpring15MiniAODv2/TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/DC47BDD9-626E-E511-9267-002590200A88.root',
       '/store/mc/RunIISpring15MiniAODv2/TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/DE78A83E-676E-E511-BB20-001E67398390.root',
       '/store/mc/RunIISpring15MiniAODv2/TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/E4000399-876F-E511-9AA4-0025905BA734.root',
       '/store/mc/RunIISpring15MiniAODv2/TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/E4E8EB16-7B6E-E511-9996-02163E00F30A.root',
       '/store/mc/RunIISpring15MiniAODv2/TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/E8FB3062-5B6E-E511-B46A-001E673986B0.root',
       '/store/mc/RunIISpring15MiniAODv2/TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/EE125F91-7C6E-E511-93CE-02163E00C58C.root',
       '/store/mc/RunIISpring15MiniAODv2/TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/EEB3B185-716E-E511-8207-002590494FDA.root',
       '/store/mc/RunIISpring15MiniAODv2/TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/F4919B3A-7B6E-E511-81A7-02163E015FAA.root',
       '/store/mc/RunIISpring15MiniAODv2/TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/F68F607B-7A6E-E511-BCFE-02163E014252.root',
       '/store/mc/RunIISpring15MiniAODv2/TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/F6B45089-7A6E-E511-B06A-02163E013B3B.root',
       '/store/mc/RunIISpring15MiniAODv2/TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/FA2543FB-696E-E511-BEEC-02163E011FE2.root',
       '/store/mc/RunIISpring15MiniAODv2/TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/FACB6E8C-7A6E-E511-B93A-02163E010BF8.root',
       '/store/mc/RunIISpring15MiniAODv2/TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/FCF28568-5E6E-E511-8D12-002590200A94.root',
       '/store/mc/RunIISpring15MiniAODv2/TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/FE22D171-5A6E-E511-ACE5-02163E00EB0B.root',
       '/store/mc/RunIISpring15MiniAODv2/TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/FE4AA6E5-7A6E-E511-B151-02163E014957.root',
] )