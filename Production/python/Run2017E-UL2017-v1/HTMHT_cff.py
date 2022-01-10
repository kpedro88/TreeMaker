import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
    '/store/data/Run2017E/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/18761E9F-A2DA-6646-94E9-1DD05F50C211.root',
    '/store/data/Run2017E/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/270000/87B947ED-67EC-6C42-83D5-E50227082BDB.root',
    '/store/data/Run2017E/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/270000/AD49A91C-7A0D-6E4B-AB68-89839952D68A.root',
    '/store/data/Run2017E/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/270000/95F04FE4-DE2B-E649-BF5D-96783FB20A3B.root',
    '/store/data/Run2017E/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/270000/4113C020-0C62-874F-ACD9-339F71EA0FE7.root',
    '/store/data/Run2017E/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/270000/E2867894-54B8-FD4B-9628-818ED3FF82B2.root',
    '/store/data/Run2017E/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/270000/36C54844-9353-6C47-A6B4-89E66CA8300C.root',
    '/store/data/Run2017E/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/270000/4C62E429-BF47-EE44-8995-2DC6D30549E8.root',
    '/store/data/Run2017E/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/270000/686BA0F7-7398-7948-842F-1E1533FF5859.root',
    '/store/data/Run2017E/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/270000/71595A58-C48C-A84B-8C8D-ED31DD14DC43.root',
    '/store/data/Run2017E/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/270000/5E0BC7D8-002E-F543-95CB-253F39983A82.root',
    '/store/data/Run2017E/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/270000/175A6BDC-9BE2-2D4C-A203-8AAFF8907F24.root',
    '/store/data/Run2017E/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/270000/0D8764FC-A8C5-D24D-8A33-90BAFA744623.root',
    '/store/data/Run2017E/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/270000/3300B089-CFC7-734D-A4FC-04C00807A426.root',
    '/store/data/Run2017E/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/270000/0D899BE3-0721-6C49-A769-DF68BAC6EC38.root',
    '/store/data/Run2017E/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/270000/B57E85A7-CC70-204B-AAA1-72D5969346F6.root',
    '/store/data/Run2017E/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/270000/5E4CF7F5-DF9A-7E43-AE3C-20DE60ECE1B7.root',
    '/store/data/Run2017E/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/270000/143274B3-3AB7-7247-B3AD-DE143D4570E0.root',
    '/store/data/Run2017E/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/270000/ABB7741A-2B52-F64F-B82A-064D2D61D422.root',
    '/store/data/Run2017E/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/270000/30E44BA0-6614-9747-8944-E326DF095D74.root',
    '/store/data/Run2017E/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/270000/DA319E6B-D057-2E43-9D73-588E776A1901.root',
    '/store/data/Run2017E/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/270000/36314E95-513D-5946-B18C-165DFC126A2E.root',
    '/store/data/Run2017E/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/270000/05E2672B-6A29-C348-AB3D-FF3B36175953.root',
    '/store/data/Run2017E/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/270000/89BC9E75-6C84-7346-907F-C8EC3CD5F6C4.root',
    '/store/data/Run2017E/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/270000/E3A7FC0C-C2F2-8B4A-842F-13D5751C0B0D.root',
    '/store/data/Run2017E/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/270000/CFE27EBF-0F9E-9447-886A-9ED42B3511FD.root',
    '/store/data/Run2017E/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/270000/557DD954-1432-7F4D-A91D-1A21C1411211.root',
    '/store/data/Run2017E/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/270000/EFD152A0-5817-2C46-AD75-907F19B61042.root',
    '/store/data/Run2017E/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/270000/75D8386D-9243-5844-A980-CAD7F6B0F94B.root',
    '/store/data/Run2017E/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/270000/DFC9913C-5927-0544-90B8-3F69259357C5.root',
    '/store/data/Run2017E/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/270000/7382CB50-68E0-984E-BF8A-D88AB63BEFD9.root',
    '/store/data/Run2017E/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/270000/B5660B58-BABE-EB48-8AA3-86163919CE0E.root',
    '/store/data/Run2017E/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/270000/6D85D2F0-A1D0-2248-9120-7DAF69F681B6.root',
    '/store/data/Run2017E/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/270000/FF41185E-3CDB-4341-9E1E-457B8B668BD4.root',
    '/store/data/Run2017E/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/270000/0EF100F6-79AE-E74F-B214-D761306DEC13.root',
    '/store/data/Run2017E/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/270000/91E0735C-244B-474A-BCC6-71C2DDEA139A.root',
    '/store/data/Run2017E/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/270000/528C8901-2D95-FA41-AA99-487C27E900CA.root',
    '/store/data/Run2017E/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/270000/C262E913-BFEE-2B4B-8251-CC7941DCD6DF.root',
    '/store/data/Run2017E/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/270000/D9DB2F69-D303-E542-A8FB-360B919DCAF0.root',
    '/store/data/Run2017E/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/270000/80272FE6-072B-DE48-8340-980AFC3F5D80.root',
    '/store/data/Run2017E/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/270000/863A8475-FCBE-8340-B490-C7DABAD3ED7C.root',
    '/store/data/Run2017E/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/270000/F5EDBC23-B9DD-9C42-B65D-543C9385E6B6.root',
    '/store/data/Run2017E/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/270000/F66F4C22-FF7B-104D-B9A8-EB115E0C1372.root',
    '/store/data/Run2017E/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/270000/7253C7B9-0454-364B-9FCE-1EF77D2A0173.root',
    '/store/data/Run2017E/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/270000/C25D5088-0C43-FD45-8253-2DAB1852B46D.root',
    '/store/data/Run2017E/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/270000/63AB944B-B01F-3D42-919E-958B53F86F9C.root',
    '/store/data/Run2017E/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/270000/1B321A2C-E4FC-634D-BA40-5FF97B30D3F9.root',
    '/store/data/Run2017E/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/270000/8F255F1C-8699-0B43-AD11-2AEAFF3121C7.root',
    '/store/data/Run2017E/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/270000/3ACA5C50-B338-AE44-B7D3-9DC2C22D8C5D.root',
    '/store/data/Run2017E/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/270000/7FF532BE-2138-F147-A05D-82CB413BD843.root',
    '/store/data/Run2017E/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/270000/D53903D3-01F9-AF4C-A18E-E81726117ACC.root',
    '/store/data/Run2017E/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/270000/F2C8D9B4-5D8A-4341-842E-D11C2F0F8EE2.root',
    '/store/data/Run2017E/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/78B3B773-4C7A-BF4D-AC87-50E8DD09F425.root',
    '/store/data/Run2017E/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/D2046D2D-5AA0-6740-9AF1-AB4FBCF98643.root',
    '/store/data/Run2017E/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/AF244F80-D733-0B4C-B87F-97DAA4D24D28.root',
    '/store/data/Run2017E/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/C91E40DA-F79A-674C-9AE5-373475019B22.root',
    '/store/data/Run2017E/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/7AB6F09D-5E36-1D47-9806-F0FC86B37B28.root',
    '/store/data/Run2017E/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/775DA929-4ADA-C749-94E9-C760D4CB36BB.root',
    '/store/data/Run2017E/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/5F79474A-55C0-6242-B4BE-EDE187393C29.root',
    '/store/data/Run2017E/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/C784C6F4-A454-2140-9E8C-351CF1C4979E.root',
    '/store/data/Run2017E/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/B2FCA559-E26E-CF43-A086-506F5A6EE24F.root',
    '/store/data/Run2017E/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/7E000DC1-01C6-044C-8682-5C3779AB9C6B.root',
    '/store/data/Run2017E/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/BF78AA69-F903-794B-8847-36CC13C084F6.root',
    '/store/data/Run2017E/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/99C57C87-46D6-8D4D-BDB9-598DB646BB4E.root',
    '/store/data/Run2017E/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/B493771E-C2E8-A444-9510-F75FB2415E6A.root',
    '/store/data/Run2017E/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/2267070F-92ED-784B-967D-23E4470EA608.root',
    '/store/data/Run2017E/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/A252B20A-4FC5-E044-9751-7D839327EB42.root',
    '/store/data/Run2017E/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/C9B1586E-94AD-BD45-9E15-F468390741E1.root',
    '/store/data/Run2017E/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/4FB78591-F749-CE47-8EC5-61468DDB40FA.root',
    '/store/data/Run2017E/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/33899FCF-E69A-E044-8E05-E716E77AE412.root',
    '/store/data/Run2017E/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/11149C0C-7737-3B42-ADD5-0BF0F14EFDAE.root',
    '/store/data/Run2017E/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/55DC4A15-8202-524C-91D8-10FD8A84306D.root',
    '/store/data/Run2017E/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/59AC1D45-D4F3-9A44-9E66-963500E78B70.root',
    '/store/data/Run2017E/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/7537E428-B97F-4C48-B110-6136899C4582.root',
    '/store/data/Run2017E/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/9CA9EA84-0765-7B4E-9ABA-908110E173DC.root',
    '/store/data/Run2017E/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/E25A517D-2C98-454E-B07A-92B6CD52EAEF.root',
    '/store/data/Run2017E/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/6AB209E6-DB30-E946-BFA2-97DDF68A16D7.root',
    '/store/data/Run2017E/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/672FC119-78BC-E04F-9115-B2222D6ACB86.root',
    '/store/data/Run2017E/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/158313D1-40BF-FD44-B0E4-0AA97BA5F14F.root',
    '/store/data/Run2017E/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/8FA5CF4F-0ECB-A943-9B24-C64BEBD7A89A.root',
    '/store/data/Run2017E/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/F2AA6519-E7C1-3644-A299-5803664BDE21.root',
    '/store/data/Run2017E/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/4CB0A268-D533-A145-956D-6B7E7E749070.root',
    '/store/data/Run2017E/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/C4FCC676-2B8B-0447-A383-1B67841EC16E.root',
    '/store/data/Run2017E/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/8A6D8F53-9914-4F4F-9926-308C74771583.root',
    '/store/data/Run2017E/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/EA7C440A-4AA7-D14B-BD69-871D2C416DF3.root',
    '/store/data/Run2017E/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/827533E4-F842-B544-82E4-6F59ADF18E86.root',
    '/store/data/Run2017E/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/2D136025-8F6A-8545-8D72-3398E296EC6B.root',
    '/store/data/Run2017E/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/DE3BD8A0-4F9D-4043-9CA2-5A737868AC4F.root',
    '/store/data/Run2017E/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/6A536B9D-B2EC-FA47-8573-3ACBE426DC53.root',
    '/store/data/Run2017E/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/68A6B74D-B181-374E-B123-90E8A8394494.root',
    '/store/data/Run2017E/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/034B3DBA-A697-444A-B088-979756BE64F9.root',
    '/store/data/Run2017E/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/DF7C5620-89C9-1449-94D0-CA948B256412.root',
    '/store/data/Run2017E/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/EEDF0706-85E8-3848-BCA2-4929479CE737.root',
    '/store/data/Run2017E/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/1BF942AD-4478-304B-9832-3A19B10AE4B7.root',
    '/store/data/Run2017E/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/10CF89F7-CAC8-C34F-A450-9645F1854551.root',
    '/store/data/Run2017E/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/16E3D538-8AD5-4542-9CED-29CC7F5EC6B6.root',
    '/store/data/Run2017E/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/6A63C861-39F3-5248-AB96-BBF689CE28BF.root',
    '/store/data/Run2017E/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/4564002A-6F33-E649-894C-C7B21C6CD540.root',
    '/store/data/Run2017E/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/D3AA4FC6-EA42-8B4B-BAC0-DBD0CCB21A70.root',
    '/store/data/Run2017E/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/427FAA79-1075-F941-968E-77FBCE0F1EAA.root',
    '/store/data/Run2017E/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/A3780C7B-8F33-6142-A6E1-C9667725AB59.root',
    '/store/data/Run2017E/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/627B3618-DF8A-D34F-94D5-8C8B63340F26.root',
    '/store/data/Run2017E/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/68917571-FBBE-3545-B83F-CAE1AE7DC25D.root',
    '/store/data/Run2017E/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/4120641F-A394-D04D-A310-A628334C6846.root',
    '/store/data/Run2017E/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/67BE2D29-613D-D948-B189-2BF1D781EFF0.root',
    '/store/data/Run2017E/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/865321DE-D88B-3648-8E36-09FA5427C98F.root',
    '/store/data/Run2017E/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/B0C0A986-121D-C04C-9DC1-7CDA89FC377A.root',
    '/store/data/Run2017E/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/9EDC62B4-E5F0-3A43-91EC-0F4A4DF90869.root',
    '/store/data/Run2017E/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/D437784F-A3F7-9F4D-8118-0390F84FE341.root',
    '/store/data/Run2017E/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/92ADB621-E0BF-9141-BE6D-E49F3BDD7A9A.root',
    '/store/data/Run2017E/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/7911297D-4507-0149-937A-8D5E85BE0546.root',
    '/store/data/Run2017E/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/4495AFB1-B847-1C4B-B756-A8464A2DD8A1.root',
    '/store/data/Run2017E/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/2A64C344-FECB-8547-8AA9-57D360F377D7.root',
    '/store/data/Run2017E/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/D694F695-968F-3C40-82BB-DF4732FDD329.root',
    '/store/data/Run2017E/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/728A767D-6DB1-3B44-B9C6-CDE7A95A579A.root',
    '/store/data/Run2017E/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/77D5B781-0EE2-8645-A510-030F881A8C7A.root',
    '/store/data/Run2017E/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/5C9C2E72-16A5-2141-B8B5-3F9B359D67AA.root',
    '/store/data/Run2017E/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/0FF9D663-DC73-F346-8BB2-6D67B4BDBA6E.root',
    '/store/data/Run2017E/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/F3AC0E4A-098A-8449-9E33-1D72239ADA02.root',
    '/store/data/Run2017E/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/F389650B-4773-494A-A471-BE964D7F0A7D.root',
    '/store/data/Run2017E/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/30F23376-DB2D-3845-9407-0876596616E7.root',
    '/store/data/Run2017E/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/B4CFD47B-0042-444C-91C0-269FD223A6B3.root',
    '/store/data/Run2017E/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/4ED52370-004F-6746-88F7-EF4E5271C429.root',
    '/store/data/Run2017E/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/DF6EF2AB-AB2C-1A47-BC60-0D82B3CE1653.root',
    '/store/data/Run2017E/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/6E838388-C760-8049-96A4-1214882F6739.root',
    '/store/data/Run2017E/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/8090A0ED-E2E3-7D4D-93CE-C3944CC8E64B.root',
    '/store/data/Run2017E/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/10064220-E9D3-6947-97ED-354FED453F5A.root',
    '/store/data/Run2017E/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/0ED2DE16-C429-764E-8E23-89E7829979C7.root',
    '/store/data/Run2017E/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/59CD2753-0A9D-504B-9E66-5FA2F16B4DA1.root',
    '/store/data/Run2017E/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/584A67BD-4049-C14D-823F-854463EE7ECB.root',
    '/store/data/Run2017E/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/C341AD67-D3B4-1947-A83D-663CD64FFB92.root',
    '/store/data/Run2017E/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/2AFC99FA-BC44-BF40-9B2B-936810913118.root',
    '/store/data/Run2017E/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/9A8DC020-FF3F-A645-8ED5-B0E2D52620A0.root',
    '/store/data/Run2017E/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/90E9996A-0E6C-EC4D-A144-17CB7817DA83.root',
    '/store/data/Run2017E/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/A7B0899B-3181-8848-BEF6-CFD28E8132E4.root',
    '/store/data/Run2017E/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/414B448A-4CCD-8741-8212-FC0EEC1B7A59.root',
    '/store/data/Run2017E/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/219D9FB2-D7D6-E84F-BE4A-30431F8FF779.root',
    '/store/data/Run2017E/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/EE478733-F459-8247-AD0D-0121084A77A6.root',
    '/store/data/Run2017E/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/319B33B5-6903-6D4F-A2A8-9BDC44ABACD0.root',
    '/store/data/Run2017E/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/7158C205-4E87-0C4C-B1A8-F686D47FB170.root',
    '/store/data/Run2017E/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/AB39861A-2DFD-0E4C-8514-F6EEABEED849.root',
    '/store/data/Run2017E/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/4F93D874-6A96-D24E-9E32-B27A661B06A2.root',
    '/store/data/Run2017E/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/7D717076-FE38-A24D-BA0A-3E6B41262785.root',
    '/store/data/Run2017E/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/570FEE74-0727-9940-96B9-B7028C02233F.root',
    '/store/data/Run2017E/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/6768E664-845D-B94C-8692-1683044586F0.root',
    '/store/data/Run2017E/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/A53C4BCF-FCAE-C54D-BD53-0E281A83941B.root',
    '/store/data/Run2017E/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/E4E0B0E9-BEA6-3748-B155-FDC637344B18.root',
    '/store/data/Run2017E/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/11F03BCB-D4D3-8A4A-8C15-4EE874AB9A49.root',
    '/store/data/Run2017E/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/C8F0182E-5ECD-3646-A365-BFF775527FB2.root',
    '/store/data/Run2017E/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/98037746-AB44-6F4C-A9C9-F8F7588CE1BC.root',
    '/store/data/Run2017E/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/E0F251CA-773E-9543-B09F-A1FC97549911.root',
    '/store/data/Run2017E/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/CED28814-EAAF-2C45-B838-6D05D14626C1.root',
    '/store/data/Run2017E/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/9A015322-4E7C-3241-A31D-C3A8CAAFE15E.root',
    '/store/data/Run2017E/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/77361F22-DBEB-3541-8688-C2A1613A2A45.root',
    '/store/data/Run2017E/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/280000/CF171872-AEF4-0C49-85C4-BF3BCAF6F98A.root',
    '/store/data/Run2017E/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/270000/230DD38E-F636-234C-9A44-49CAE0B0A76A.root',
    '/store/data/Run2017E/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/260000/C67CA3A6-87FB-E34F-A98F-BCAD00C2431C.root',
    '/store/data/Run2017E/HTMHT/MINIAOD/UL2017_MiniAODv2-v1/50000/19B42E18-6829-C642-AA25-50F492EC3027.root',
] )