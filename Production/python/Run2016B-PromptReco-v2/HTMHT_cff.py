import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/273/150/00000/B00996D1-D719-E611-8F3C-02163E0144BF.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/273/158/00000/1E2DF43A-4C1A-E611-A689-02163E01354D.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/273/158/00000/24070649-291A-E611-A268-02163E013447.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/273/158/00000/4AE9C849-261A-E611-B0E1-02163E0124A7.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/273/158/00000/7EE91C9C-2D1A-E611-94C2-02163E011A9C.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/273/158/00000/F64244D7-301A-E611-AA00-02163E01434C.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/273/287/00000/161FEBC3-141A-E611-B0B8-02163E01216A.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/273/290/00000/FEABBD4C-171A-E611-8C42-02163E0134C5.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/273/291/00000/526A1034-431A-E611-8745-02163E0143D1.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/273/292/00000/60292FB4-221A-E611-B825-02163E012381.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/273/294/00000/E8780A0A-241A-E611-9960-02163E011A07.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/273/295/00000/98E2CAFD-231A-E611-8273-02163E011BFF.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/273/296/00000/482BF9E4-381A-E611-A149-02163E013779.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/273/299/00000/02FDCB81-511A-E611-A5BF-02163E011E1B.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/273/301/00000/68D0BF1F-9A1A-E611-A9E5-02163E01433B.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/273/301/00000/7275EF27-901A-E611-B109-02163E012AA8.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/273/301/00000/8E8605E8-961A-E611-95BB-02163E011C1D.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/273/302/00000/CC321374-A91A-E611-954D-02163E0143F2.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/273/302/00000/D86BF47E-AF1A-E611-9076-02163E01349D.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/273/402/00000/DE1DA748-4D1B-E611-8D86-02163E0119AA.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/273/403/00000/486A1902-4D1B-E611-9A9A-02163E01471E.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/273/404/00000/0082A7DE-441B-E611-B71F-02163E014702.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/273/405/00000/2A04993F-501B-E611-8E00-02163E0145A7.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/273/406/00000/D82949DD-6F1B-E611-B75E-02163E0145EB.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/273/407/00000/38C5C007-3C1B-E611-8DD5-02163E011980.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/273/408/00000/4A6320B1-411B-E611-9BCA-02163E0125BC.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/273/409/00000/56B7E0E7-761B-E611-966A-02163E011EB0.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/273/410/00000/1E654F1D-711B-E611-9864-02163E014231.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/273/411/00000/A28F21F9-731B-E611-9D30-02163E014213.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/273/412/00000/08C85E66-621B-E611-8C99-02163E0141AD.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/273/424/00000/E2D369F6-591B-E611-9055-02163E011D55.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/273/425/00000/C08E8059-281C-E611-BA77-02163E0142BD.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/273/425/00000/E08D552B-B31B-E611-8CFC-02163E011854.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/273/425/00000/FAAC48A9-B81B-E611-863F-02163E01369C.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/273/426/00000/04B3FED6-CE1B-E611-BA22-02163E011999.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/273/443/00000/2E6AE35F-AD1B-E611-B225-02163E0137FA.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/273/444/00000/50C3DAE2-AD1B-E611-894A-02163E01368F.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/273/445/00000/469FFF0B-B11B-E611-9D79-02163E014797.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/273/446/00000/FC9778A2-E31B-E611-B17C-02163E011FFA.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/273/447/00000/2ED72BC3-F31B-E611-9C5B-02163E014552.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/273/447/00000/4A11D341-E61B-E611-8945-02163E0143F2.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/273/447/00000/E43D76D3-EF1B-E611-B146-02163E011A9C.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/273/448/00000/44C1999C-1A1C-E611-84AA-02163E01347B.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/273/448/00000/D6EC4171-2B1C-E611-A226-02163E0135C0.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/273/449/00000/0A4B8BCF-321C-E611-84AE-02163E011A0A.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/273/450/00000/4C4E91DA-4A1C-E611-984C-02163E014438.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/273/450/00000/6238D8D7-471C-E611-935E-02163E0145DB.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/273/450/00000/94AD1605-5D1C-E611-8C14-02163E012444.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/273/492/00000/3A17A6DB-591D-E611-9322-02163E013917.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/273/493/00000/CA98564A-791D-E611-9CB7-02163E0143E8.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/273/494/00000/3E29A97B-7D1D-E611-B833-02163E01469F.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/273/502/00000/66E2095B-911F-E611-9D84-02163E0146CF.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/273/502/00000/ACC72AC2-1A1F-E611-83A5-02163E01374F.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/273/502/00000/BAF532D3-1A1F-E611-B36B-02163E014638.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/273/502/00000/EAACFCBD-1A1F-E611-9499-02163E01348B.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/273/503/00000/0E5CBC9A-2D1F-E611-87C8-02163E01221A.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/273/503/00000/C48F4328-3E1F-E611-A93D-02163E01367F.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/273/504/00000/FC7F8C0E-321F-E611-B28A-02163E0135F1.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/273/523/00000/1210868A-481F-E611-ABA7-02163E014611.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/273/526/00000/D25FCA77-571F-E611-85FF-02163E0142C2.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/273/537/00000/64754583-881F-E611-8125-02163E011B67.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/273/554/00000/1C09EF03-E01F-E611-AF6D-02163E012694.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/273/554/00000/BA79D842-DB1F-E611-8661-02163E0142C8.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/273/555/00000/A6F6845D-1920-E611-A6F7-02163E0118E1.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/273/589/00000/5C6CC4B5-DD1F-E611-975B-02163E013546.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/273/590/00000/68E408D0-0420-E611-88DE-02163E0146B9.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/273/592/00000/E4639AFF-0B20-E611-B66F-02163E01450E.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/273/725/00000/004322D9-8620-E611-B89B-02163E01440B.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/273/725/00000/0E0E5D09-8920-E611-8AE1-02163E013400.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/273/725/00000/2ABD2B71-B920-E611-9890-02163E011C70.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/273/725/00000/3ABBC36D-8020-E611-83BA-02163E01188C.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/273/725/00000/3ED1850D-9120-E611-B858-02163E0143F4.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/273/725/00000/404B8C68-8B20-E611-B528-02163E012143.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/273/725/00000/4609DFE8-8A20-E611-BF88-02163E014731.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/273/725/00000/661EDA79-8D20-E611-9BF5-02163E014748.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/273/725/00000/6AD7800C-8820-E611-BA93-02163E0146DD.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/273/725/00000/B20D04E6-8420-E611-941A-02163E0144EE.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/273/725/00000/BC88A415-8F20-E611-A30A-02163E01265D.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/273/725/00000/CAC1E5EF-9520-E611-AAA6-02163E012801.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/273/728/00000/B8C058BF-E320-E611-AE1A-02163E0139CC.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/273/730/00000/0690DF60-AC21-E611-946B-02163E011922.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/273/730/00000/3AEDD7FE-8921-E611-9DC3-02163E01468F.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/273/730/00000/56C3855A-AC21-E611-8ED0-02163E014474.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/273/730/00000/62837751-AC21-E611-BDA4-02163E0144C6.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/273/730/00000/8047A640-AC21-E611-A34F-02163E01472B.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/273/730/00000/86377C6F-9D21-E611-88AD-02163E0143B9.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/273/730/00000/A0CBB632-8D21-E611-AD68-02163E01447E.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/273/730/00000/A4A7EE5A-AC21-E611-828E-02163E014474.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/273/730/00000/CC933840-A521-E611-8783-02163E0137FF.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/273/730/00000/DC1BB65A-AC21-E611-B596-02163E014474.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/274/079/00000/4C0CF985-DF24-E611-BE15-02163E014480.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/274/080/00000/5001EB19-E324-E611-841B-02163E012453.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/274/081/00000/F62F1012-E724-E611-9998-02163E0135A8.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/274/083/00000/4C1EC73E-FB24-E611-9B7F-02163E011F64.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/274/087/00000/F0F3BB47-0B25-E611-80F7-02163E01380B.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/274/088/00000/66C921AD-0825-E611-BA0C-02163E014568.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/274/094/00000/0E4E4081-7F25-E611-AA2C-02163E01383E.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/274/094/00000/B4345A1A-7225-E611-9E0D-02163E012620.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/274/102/00000/8420667A-CB26-E611-A373-02163E0146EE.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/274/103/00000/98235A4E-CE26-E611-914A-02163E014270.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/274/104/00000/44CD4BC0-CE26-E611-A071-02163E01389E.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/274/105/00000/C882CD6D-CF26-E611-BADF-02163E012516.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/274/106/00000/72D3E914-D026-E611-AE56-02163E0134D3.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/274/107/00000/30F8D55E-D026-E611-AB86-02163E011D09.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/274/108/00000/8EAB3448-D126-E611-88F1-02163E01352A.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/274/142/00000/20709080-D226-E611-BEB7-02163E012A7E.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/274/146/00000/8ED361B9-D326-E611-B334-02163E01431E.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/274/147/00000/E4E5EED2-D326-E611-9746-02163E013404.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/274/157/00000/4052693E-0727-E611-BB72-02163E014229.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/274/157/00000/42DDA038-0727-E611-AE3D-02163E0145EC.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/274/157/00000/A439DE3C-0727-E611-9BC1-02163E012474.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/274/157/00000/C004D03B-0727-E611-BC38-02163E014354.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/274/159/00000/92C48449-DB26-E611-87E8-02163E0142F5.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/274/160/00000/5622A6F4-DD26-E611-A216-02163E011A79.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/274/160/00000/5A00A5F5-DD26-E611-9E27-02163E014218.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/274/161/00000/22188D52-0927-E611-BC4B-02163E0123DD.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/274/161/00000/40C88C70-0927-E611-84B1-02163E01429F.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/274/161/00000/ACB7A263-0927-E611-80F1-02163E01349C.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/274/172/00000/5C1966AF-2427-E611-8DC0-02163E01363C.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/274/197/00000/189FC24B-5827-E611-A48D-02163E0123FA.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/274/198/00000/C8C78876-9327-E611-B7B1-02163E014256.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/274/198/00000/FE51BBDD-8427-E611-823F-02163E011CDA.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/274/199/00000/0C6F134C-B127-E611-932C-02163E0137BB.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/274/199/00000/26B6B801-BE27-E611-9F10-02163E012429.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/274/199/00000/44F20B73-AE27-E611-98F5-02163E013695.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/274/199/00000/506DDC34-D127-E611-BBB3-02163E011AA8.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/274/199/00000/9EDF90BF-B327-E611-B426-02163E01189F.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/274/199/00000/CA735CC9-AA27-E611-9B1A-02163E0141BA.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/274/200/00000/B4D2DD88-F327-E611-9052-02163E013806.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/274/200/00000/BC35FC61-CD27-E611-9E0E-02163E01394F.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/274/200/00000/C07EFFEB-D927-E611-9D1B-02163E0120FE.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/274/200/00000/C0BFA225-D027-E611-80C2-02163E014756.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/274/200/00000/D80C9F20-D327-E611-ABD4-02163E01191C.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/274/239/00000/3484610E-FA27-E611-988B-02163E01263F.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/274/240/00000/EC739A2E-4E28-E611-8933-02163E014506.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/274/241/00000/0A338AE0-CE28-E611-A09D-02163E0141A2.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/274/241/00000/343F78D0-CE28-E611-BA7E-02163E011A51.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/274/241/00000/3A67E3CD-CE28-E611-B38C-02163E0133BB.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/274/241/00000/483E8C3F-FC28-E611-AB9B-02163E014426.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/274/241/00000/5E5F57D9-CE28-E611-88A5-02163E0134D5.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/274/241/00000/BEC1FBCC-CE28-E611-A27F-02163E01189F.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/274/241/00000/CA28ECE1-CE28-E611-B2F4-02163E01447E.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/274/241/00000/DA9A9ED0-CE28-E611-BBD4-02163E012864.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/274/241/00000/E05543CF-CE28-E611-8D97-02163E0136FF.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/274/241/00000/F071CDE1-CE28-E611-80A3-02163E0139DB.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/274/243/00000/30A30CA4-CF28-E611-9D54-02163E011DE8.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/274/244/00000/1EB83666-0829-E611-93CC-02163E0133FB.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/274/244/00000/6E3AA7DB-D228-E611-A60B-02163E01362B.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/274/244/00000/76B248F1-D228-E611-9492-02163E0119F0.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/274/244/00000/94FBD6DD-D228-E611-BF7F-02163E01354B.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/274/244/00000/C41553E0-D228-E611-A499-02163E0133E8.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/274/249/00000/7E3C8027-0A29-E611-A9B0-02163E0125EC.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/274/250/00000/2C00FB24-3E29-E611-96C4-02163E01368A.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/274/250/00000/5A95DF0E-3E29-E611-BD29-02163E014449.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/274/250/00000/76C5E417-3E29-E611-A5FB-02163E014659.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/274/250/00000/CEB56CA3-5029-E611-AD31-02163E011967.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/274/250/00000/D0F89D12-3E29-E611-BC86-02163E0120F3.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/274/250/00000/E83D7B0F-3E29-E611-8357-02163E014160.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/274/250/00000/F057F00E-3E29-E611-8723-02163E0118DA.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/274/250/00000/F05D240C-3E29-E611-AE00-02163E01472E.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/274/251/00000/445540F8-4429-E611-9F07-02163E011826.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/274/251/00000/5C3890E9-4429-E611-B554-02163E011A9C.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/274/251/00000/6815B4E1-4429-E611-B06D-02163E0141E8.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/274/251/00000/BAE6AEE1-4429-E611-86F0-02163E01454B.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/274/251/00000/E2030DCB-5829-E611-9483-02163E0142ED.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/274/278/00000/BC983D15-6029-E611-9C72-02163E012353.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/274/282/00000/74677A6C-6329-E611-ABBA-02163E0142B0.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/274/283/00000/5C3AA10B-6529-E611-B9AC-02163E0129DC.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/274/284/00000/50F5D27D-9929-E611-A5D8-02163E014459.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/274/284/00000/7A044BD8-6A29-E611-B46B-02163E013494.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/274/284/00000/9A1554DF-6A29-E611-958A-02163E0138F6.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/274/285/00000/3C231C7F-8029-E611-B509-02163E012812.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/274/286/00000/0C8B0CF6-8B29-E611-B70E-02163E0128DB.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/274/286/00000/94FE2DC7-8429-E611-B934-02163E013892.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/274/303/00000/0ED110E1-9A29-E611-A311-02163E0134CF.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/274/314/00000/8A8CA001-D629-E611-91DE-02163E0143C5.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/274/314/00000/C8AB66D4-162A-E611-8E5E-02163E014421.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/274/315/00000/00A0C7BC-D829-E611-8678-02163E011AE2.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/274/315/00000/8C45765D-0C2A-E611-A893-02163E0134D5.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/274/315/00000/8E0793DD-D829-E611-B1D7-02163E0144CC.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/274/315/00000/A0082F7C-032A-E611-927B-02163E011C90.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/274/315/00000/BCFCA1BA-D829-E611-8B11-02163E012A03.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/274/315/00000/E03EB217-DD29-E611-A557-02163E013843.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/274/315/00000/E6A1BDDE-D829-E611-9D8E-02163E01237C.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/274/316/00000/02C6FD3C-222A-E611-806A-02163E01186C.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/274/316/00000/127A21DB-0A2A-E611-B713-02163E011F30.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/274/316/00000/501114A4-0B2A-E611-931F-02163E0133C8.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/274/316/00000/54426276-062A-E611-8889-02163E01458A.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/274/316/00000/54E570AE-492A-E611-AEF7-02163E013589.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/274/316/00000/A2283DFB-032A-E611-B358-02163E011D5E.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/274/316/00000/C0EBBBCE-072A-E611-A293-02163E014311.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/274/316/00000/DC9D810F-102A-E611-B949-02163E014674.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/274/316/00000/DE9B43D6-092A-E611-A992-02163E0146D8.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/274/316/00000/E440E502-FF29-E611-92AB-02163E01448A.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/274/316/00000/EAECE0BF-022A-E611-8944-02163E012B3C.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/274/317/00000/4AF4B4D7-3B2A-E611-A9FE-02163E011B75.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/274/318/00000/D26708C6-172A-E611-A586-02163E0143C4.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/274/319/00000/8425EC9B-572A-E611-8568-02163E0135BD.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/274/319/00000/B68017BD-462A-E611-A947-02163E01357F.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/PromptReco-v2/000/274/334/00000/E2D37EF7-3E2A-E611-9F95-02163E014743.root',
] )
