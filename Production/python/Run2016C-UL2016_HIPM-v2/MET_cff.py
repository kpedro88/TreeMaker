import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
    '/store/data/Run2016C/MET/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/85E62A74-44FE-CD43-A935-12A3CCDBCC2B.root',
    '/store/data/Run2016C/MET/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/D17F4DD4-048F-F849-A992-5C2C701CD109.root',
    '/store/data/Run2016C/MET/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/895B28A6-EB93-EE45-99E4-C0E7DACCD6D4.root',
    '/store/data/Run2016C/MET/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/5F219CC3-FE7A-E740-861E-C41B47E74188.root',
    '/store/data/Run2016C/MET/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/DF3ABB02-99BB-754A-96D8-DDEB9BF33E77.root',
    '/store/data/Run2016C/MET/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/94E8559B-0F57-D448-AF2B-9C08D757D0FF.root',
    '/store/data/Run2016C/MET/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/23B8BAAD-4E8C-6944-B0E9-D7767440187E.root',
    '/store/data/Run2016C/MET/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/99009F3F-12B7-244E-878B-B2A9FF3DABB3.root',
    '/store/data/Run2016C/MET/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/7CA540C0-4CE3-8F4A-9C2C-D20B5F60313C.root',
    '/store/data/Run2016C/MET/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/B405E37B-C4E3-9E4A-BD6D-FB6A395DFD23.root',
    '/store/data/Run2016C/MET/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/35787BD7-D6D2-A24F-84EE-26DEF3987B39.root',
    '/store/data/Run2016C/MET/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/EABF6704-E171-F74A-AA39-58883E536FAE.root',
    '/store/data/Run2016C/MET/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/B4EB3ABE-FE2F-F542-AF2C-6AB5C6C2DB37.root',
    '/store/data/Run2016C/MET/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/1F84A649-D144-1F4A-A5A8-7929A98E9910.root',
    '/store/data/Run2016C/MET/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/C56A2EF3-9DD0-7340-BD7E-89FFDDFFB240.root',
    '/store/data/Run2016C/MET/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/9ABA2086-B5C9-1B46-8998-20E566D26C39.root',
    '/store/data/Run2016C/MET/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/17209BE0-182C-BB42-B773-1BA3AA6167FA.root',
    '/store/data/Run2016C/MET/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/7E2AECD2-5B09-344F-B1B5-E82337658098.root',
    '/store/data/Run2016C/MET/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/CB0EF6B8-FE25-4449-9A09-336D09D29668.root',
    '/store/data/Run2016C/MET/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/C55E8989-79D8-BE4C-9CFC-2109B31C7CE1.root',
    '/store/data/Run2016C/MET/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/2D2938C3-110B-5940-88D3-FC0567A8770B.root',
    '/store/data/Run2016C/MET/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/F6C537F2-5F97-4649-AB24-D4E2D7EADD54.root',
    '/store/data/Run2016C/MET/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/87611BD8-3D85-D24B-A25A-2A8BC7B14952.root',
    '/store/data/Run2016C/MET/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/7D2D8366-1412-6E48-904D-354BD2BB2F83.root',
    '/store/data/Run2016C/MET/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/1E6DED95-C5E8-C84D-9193-0C34365F9B8F.root',
    '/store/data/Run2016C/MET/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/F614069B-56F7-D24E-8375-89A0CE8F736F.root',
    '/store/data/Run2016C/MET/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/845A2CFE-D729-AF47-9FF4-8A9CE94E6825.root',
    '/store/data/Run2016C/MET/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/3EDAD7A0-2EBF-804C-B7C5-C3539F4E9521.root',
    '/store/data/Run2016C/MET/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/3AE83032-D89E-D741-BE44-26BCA1988581.root',
    '/store/data/Run2016C/MET/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/03E8A546-27B9-7345-A0F8-9A196DF22AE9.root',
    '/store/data/Run2016C/MET/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/C42DDB7E-ACB2-7547-B4AE-467065838221.root',
    '/store/data/Run2016C/MET/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/536E04B0-6E05-6141-99C5-F1ED001A866F.root',
    '/store/data/Run2016C/MET/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/B9D36C79-4447-3848-B31B-110027BED2FE.root',
    '/store/data/Run2016C/MET/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/B09C5C19-BC91-254E-89DD-B054FD02CFE2.root',
    '/store/data/Run2016C/MET/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/629970ED-C11C-A144-A8E8-85946CA0D9B1.root',
    '/store/data/Run2016C/MET/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/342B7CD9-0337-4F44-B38E-6D200F9FE4C2.root',
    '/store/data/Run2016C/MET/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/EAF7D9D5-13E2-3144-962A-7E0318EAD0D6.root',
    '/store/data/Run2016C/MET/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/12EE8E6D-546E-854E-926E-06282BE57A4D.root',
    '/store/data/Run2016C/MET/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/74A51BE4-1458-8E43-84F4-C60BB88E98A6.root',
    '/store/data/Run2016C/MET/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/F182AA6F-4631-3846-9E65-9061A0978D33.root',
    '/store/data/Run2016C/MET/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/2DC20FBE-7551-7149-BE2B-3A7E69957278.root',
    '/store/data/Run2016C/MET/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/F84E3ED2-66AE-2F49-AC1A-A3E9B8433520.root',
    '/store/data/Run2016C/MET/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/5084BBB6-243D-A547-929D-1EA30A9831B1.root',
    '/store/data/Run2016C/MET/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/A561A3BB-6BB3-DA4D-BA03-CB785D9329A4.root',
    '/store/data/Run2016C/MET/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/54E9DCD4-7850-0349-9800-21751486CF1B.root',
    '/store/data/Run2016C/MET/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/9E4FE0ED-03FB-1C44-A82D-57E40DA1FD27.root',
    '/store/data/Run2016C/MET/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/6C1309C3-5A50-A04F-9041-9D691E61E24A.root',
    '/store/data/Run2016C/MET/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/13FDDC8C-89ED-D349-B955-0FD0300136B0.root',
    '/store/data/Run2016C/MET/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/0874E4BA-3ED1-644F-898A-69E58C235EF6.root',
    '/store/data/Run2016C/MET/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/A981CCA0-02B9-EE41-9303-A60E68430A0F.root',
    '/store/data/Run2016C/MET/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/504B7D2F-58E4-3A41-AA58-E9D43C5941CD.root',
    '/store/data/Run2016C/MET/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/7C958A45-4BE9-574B-960E-5764BF464008.root',
    '/store/data/Run2016C/MET/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/BEDFBF3F-7170-A14A-B937-8D965DF92C2A.root',
    '/store/data/Run2016C/MET/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/D72365C2-5E7C-214C-A1F3-C0A6D32D4DD9.root',
    '/store/data/Run2016C/MET/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/37D39422-E57A-5641-BA3E-551FB5603ECE.root',
    '/store/data/Run2016C/MET/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/1DF62809-874E-A04D-BE9C-A4F186D8C626.root',
    '/store/data/Run2016C/MET/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/8AF9971D-1C25-CC4C-9409-24174ED3D943.root',
    '/store/data/Run2016C/MET/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/70351056-8AA5-9247-9244-44D9C9C1E898.root',
    '/store/data/Run2016C/MET/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/E6422C2A-4CF2-7345-9F8C-4A8914D03A3C.root',
    '/store/data/Run2016C/MET/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/77E5F86B-6A8D-4B42-9A87-818DD98D29E0.root',
    '/store/data/Run2016C/MET/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/134D9936-139B-174D-8F8B-FC455A9D2A38.root',
    '/store/data/Run2016C/MET/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/0D42456E-9C1F-1A48-9BD1-85A572573789.root',
    '/store/data/Run2016C/MET/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/E9C78ED1-1EC9-5B4B-A835-8668F79C75A2.root',
    '/store/data/Run2016C/MET/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/DA2CF3B6-4FA2-FF4E-9571-595E50AF4B80.root',
    '/store/data/Run2016C/MET/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/95A4CB4D-1D5D-5F4E-AA1E-C92FD4E31078.root',
    '/store/data/Run2016C/MET/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/3988DB92-6178-7C4B-87CB-2F2BD7DFCFAF.root',
    '/store/data/Run2016C/MET/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/AF1F16B9-6861-9346-98E2-C85949FD9C2A.root',
    '/store/data/Run2016C/MET/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/BA63D22E-AC1F-4041-84A4-B2606A28431F.root',
    '/store/data/Run2016C/MET/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/8603B532-5CB3-BD48-AD2E-79590ED8663F.root',
    '/store/data/Run2016C/MET/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/95F869E6-F1DF-F74D-9316-C6C206397C2A.root',
    '/store/data/Run2016C/MET/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/2AE9D17D-D709-B245-8EBC-A6E056E11439.root',
    '/store/data/Run2016C/MET/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/6C68B3EB-2FCF-F14E-B32D-A64D3F073EE8.root',
    '/store/data/Run2016C/MET/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/BE934AF4-9FBD-B740-B1E3-94014ABF9F14.root',
    '/store/data/Run2016C/MET/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/862DAC21-B91E-214D-BB7D-974EBC9B50D8.root',
    '/store/data/Run2016C/MET/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/FD6F26AA-6023-DC40-85C8-E4ED9E567C9F.root',
    '/store/data/Run2016C/MET/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/6D6FE40C-C400-4B4E-8EFE-DD57B7D7199C.root',
    '/store/data/Run2016C/MET/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/D1CE885F-329E-2648-B4DC-C6BF222F6779.root',
    '/store/data/Run2016C/MET/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/3B88A064-B936-A842-908D-194E2A1A15BB.root',
    '/store/data/Run2016C/MET/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/34912C73-80E8-FC4F-9B45-10A773577351.root',
    '/store/data/Run2016C/MET/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/7E56C992-1C53-C948-8029-84B14B5044EA.root',
    '/store/data/Run2016C/MET/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/75530DD5-4B49-EA49-B934-26849F5D2E24.root',
    '/store/data/Run2016C/MET/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/D9BE2475-A71F-3446-B6D8-5A59CCCC0B7C.root',
    '/store/data/Run2016C/MET/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/C32CDEFD-EEA9-6D43-84A4-3421AC21B7CF.root',
    '/store/data/Run2016C/MET/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/17C3EE45-4387-DB40-8420-ADE5ADD5F4ED.root',
    '/store/data/Run2016C/MET/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/0E01A4A0-B9C6-ED45-827F-390C6F3B2340.root',
    '/store/data/Run2016C/MET/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/6BA3E30F-BC95-EC49-ABC6-F3FAD301D334.root',
    '/store/data/Run2016C/MET/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/75DDB7D4-203E-964E-853A-7055FEBF51E3.root',
    '/store/data/Run2016C/MET/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/A63C4B94-9F0F-3243-BF1C-872095386DC0.root',
    '/store/data/Run2016C/MET/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/225D3676-2B45-7744-BFF2-5E3DB527862E.root',
    '/store/data/Run2016C/MET/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/028F76EB-3B93-E94B-8BF1-A44557D049A5.root',
    '/store/data/Run2016C/MET/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/3A6286D6-4487-5D4F-A9F9-EDFD838544D3.root',
    '/store/data/Run2016C/MET/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/5B03D496-602D-5049-9CFF-7E20FFC93610.root',
    '/store/data/Run2016C/MET/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/EF435002-144F-1C4E-8781-EC7838B833CD.root',
    '/store/data/Run2016C/MET/MINIAOD/HIPM_UL2016_MiniAODv2-v2/70000/9DA6B97F-2859-4340-ADC9-C36B7AAB56E0.root',
    '/store/data/Run2016C/MET/MINIAOD/HIPM_UL2016_MiniAODv2-v2/70000/1C180F2B-1C38-594E-9DD6-8F129FBCF4BE.root',
    '/store/data/Run2016C/MET/MINIAOD/HIPM_UL2016_MiniAODv2-v2/70000/6D27ECCB-5061-8E40-87A4-F067E707D362.root',
    '/store/data/Run2016C/MET/MINIAOD/HIPM_UL2016_MiniAODv2-v2/70000/F441C731-CA42-D247-B010-011E44FB4FAA.root',
    '/store/data/Run2016C/MET/MINIAOD/HIPM_UL2016_MiniAODv2-v2/70000/99883DBA-698E-974A-8042-FB8CF866E30A.root',
    '/store/data/Run2016C/MET/MINIAOD/HIPM_UL2016_MiniAODv2-v2/70000/089C62AF-651B-6146-B0CC-8F5F34C45939.root',
    '/store/data/Run2016C/MET/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/56C1BC4A-FB48-0E48-804E-9E3B441C1860.root',
    '/store/data/Run2016C/MET/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/D5418C00-C45E-3E4F-A56F-40CFE6A02950.root',
    '/store/data/Run2016C/MET/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/5EF7C8C5-49BB-C647-9800-D1CAA4F0AA73.root',
    '/store/data/Run2016C/MET/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/0C159F0F-EA1E-D344-B66E-5FFCAB1072B6.root',
    '/store/data/Run2016C/MET/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/71EE0655-6786-A84F-8876-DBD8FC89E489.root',
    '/store/data/Run2016C/MET/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/1EA71B91-583E-9F42-B3E8-D4759C1A0BFE.root',
    '/store/data/Run2016C/MET/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/3CEA9A2C-2AAE-7F42-AD7C-7AAECC7E17AB.root',
    '/store/data/Run2016C/MET/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/66367FDA-F354-FB41-9964-FD19656F9E54.root',
    '/store/data/Run2016C/MET/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/4713D60E-1727-5548-9749-BE3263B06943.root',
    '/store/data/Run2016C/MET/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/2A3C1275-2048-724E-B12B-7A3373585453.root',
    '/store/data/Run2016C/MET/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/1577A0FA-B445-D048-B8B2-6A11EB0C69A2.root',
    '/store/data/Run2016C/MET/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/CB67E859-244B-3347-81A8-77A25FE02823.root',
    '/store/data/Run2016C/MET/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/78052CE0-A3D9-F44F-8F27-B38B60DF5A10.root',
    '/store/data/Run2016C/MET/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/8D0A76D6-BA02-1742-A0FE-2F2B6F15E707.root',
    '/store/data/Run2016C/MET/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/5EE4A8A9-392E-D145-9637-F0A9D2F44943.root',
    '/store/data/Run2016C/MET/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/0A1F37E2-3C23-F340-871A-C3264AA59FB8.root',
    '/store/data/Run2016C/MET/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/A4D23EB8-D5A1-3841-9D04-BADBEDF9527A.root',
    '/store/data/Run2016C/MET/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/8CC46AA3-B87A-CE45-88CA-EB8BFFDF5429.root',
    '/store/data/Run2016C/MET/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/EA683079-20DD-954B-8F69-34C586ED08A9.root',
    '/store/data/Run2016C/MET/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/A63A1782-4144-434C-BF87-004E0C76AD7E.root',
    '/store/data/Run2016C/MET/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/BA91C637-A92F-3B44-9829-7591D013419C.root',
    '/store/data/Run2016C/MET/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/EDFCA792-9B11-1E41-99A7-CAD4166C85EC.root',
    '/store/data/Run2016C/MET/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/E4E7EB0B-2C5A-2341-AFC7-8DEA0599FEE1.root',
    '/store/data/Run2016C/MET/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/5A348220-28AF-4A4E-9E52-1D6201C7D191.root',
    '/store/data/Run2016C/MET/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/99412A4C-05FF-174A-A708-633B4A916ED2.root',
    '/store/data/Run2016C/MET/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/3E9EC776-E4CE-7C4E-AC82-B495C485E584.root',
    '/store/data/Run2016C/MET/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/2CB0303C-5D8A-924C-BE34-68292550950A.root',
    '/store/data/Run2016C/MET/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/929587BC-5104-1C43-95DD-B6F6A52659C3.root',
    '/store/data/Run2016C/MET/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/6FCCE962-64EF-0147-9E14-BD17E219EBBC.root',
    '/store/data/Run2016C/MET/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/F169F51B-29DB-3746-8215-133925F26C60.root',
    '/store/data/Run2016C/MET/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/4ECF01FA-4C12-CE49-9B6C-D4228B07A86C.root',
    '/store/data/Run2016C/MET/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/141962FB-DA09-864A-A895-779A3EA02F08.root',
    '/store/data/Run2016C/MET/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/824B5574-DFE5-F142-B41C-9774F27B3C45.root',
    '/store/data/Run2016C/MET/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/C2998F7A-E6D1-F645-99D9-4A684035F7BD.root',
    '/store/data/Run2016C/MET/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/389409FE-5C99-A447-90CF-0D98E82F356C.root',
    '/store/data/Run2016C/MET/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/F767EA1A-81F7-BC46-9B02-38F1DBCC533A.root',
    '/store/data/Run2016C/MET/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/FB338663-06EE-E446-8B4A-79428942E7B2.root',
    '/store/data/Run2016C/MET/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/2E22CD94-05C2-FE4E-A75A-9F1AFAB397F7.root',
    '/store/data/Run2016C/MET/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/44687D10-3CE8-B745-BA36-D08AD9F875B2.root',
    '/store/data/Run2016C/MET/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/D686A44B-C5E6-794F-A21D-2B555B3EE40D.root',
    '/store/data/Run2016C/MET/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/4DA3EDB6-BC12-8E4E-B252-20403C4D9A64.root',
    '/store/data/Run2016C/MET/MINIAOD/HIPM_UL2016_MiniAODv2-v2/120000/6A90C119-68DA-5842-9B44-103CD7D2510D.root',
    '/store/data/Run2016C/MET/MINIAOD/HIPM_UL2016_MiniAODv2-v2/70000/36232E94-4F76-B549-B09E-E26A5BBE820B.root',
] )