import sys
import firmware_part as fwp

class extractor:
    def __init__(self):
        # 1.0.11 (factory image)
        """
        self.firmware_parts = [
            fwp.firmware_part("begin",         0x00000000, 0x00006800 - 0x00000000),
            fwp.firmware_part("uimage_boot0",  0x00006800, 0x00030100 - 0x00006800),
            fwp.firmware_part("gzip0",         0x00030100, 0x00050000 - 0x00030100),
            fwp.firmware_part("uimage_boot1",  0x00050000, 0x00070200 - 0x00050000),
            fwp.firmware_part("uimage_kernel", 0x00070200, 0x001B6E36 - 0x00070200),
            fwp.firmware_part("xz0",           0x001B6E36, 0x001BE372 - 0x001B6E36),
            fwp.firmware_part("xz1",           0x001BE372, 0x001C5CBE - 0x001BE372),
            fwp.firmware_part("xz2",           0x001C5CBE, 0x001CD50E - 0x001C5CBE),
            fwp.firmware_part("xz3",           0x001CD50E, 0x001D3BB6 - 0x001CD50E),
            fwp.firmware_part("xz4",           0x001D3BB6, 0x001D74F6 - 0x001D3BB6),
            fwp.firmware_part("xz5",           0x001D74F6, 0x001DB81E - 0x001D74F6),
            fwp.firmware_part("xz6",           0x001DB81E, 0x001DF252 - 0x001DB81E),
            fwp.firmware_part("xz7",           0x001DF252, 0x001E1A62 - 0x001DF252),
            fwp.firmware_part("xz8",           0x001E1A62, 0x001E7252 - 0x001E1A62),
            fwp.firmware_part("xz9",           0x001E7252, 0x001E9A5A - 0x001E7252),
            fwp.firmware_part("xz10",          0x001E9A5A, 0x001EECBA - 0x001E9A5A),
            fwp.firmware_part("xz11",          0x001EECBA, 0x001F046A - 0x001EECBA),
            fwp.firmware_part("xz12",          0x001F046A, 0x001F62FA - 0x001F046A),
            fwp.firmware_part("xz13",          0x001F62FA, 0x001FB312 - 0x001F62FA),
            fwp.firmware_part("xz14",          0x001FB312, 0x00201252 - 0x001FB312),
            fwp.firmware_part("xz15",          0x00201252, 0x002078D6 - 0x00201252),
            fwp.firmware_part("xz16",          0x002078D6, 0x0020DB32 - 0x002078D6),
            fwp.firmware_part("xz17",          0x0020DB32, 0x002139A6 - 0x0020DB32),
            fwp.firmware_part("xz18",          0x002139A6, 0x0021A842 - 0x002139A6),
            fwp.firmware_part("xz19",          0x0021A842, 0x00220DE6 - 0x0021A842),
            fwp.firmware_part("xz20",          0x00220DE6, 0x0022703E - 0x00220DE6),
            fwp.firmware_part("xz21",          0x0022703E, 0x0022B0FE - 0x0022703E),
            fwp.firmware_part("xz22",          0x0022B0FE, 0x00233C12 - 0x0022B0FE),
            fwp.firmware_part("xz23",          0x00233C12, 0x0023913A - 0x00233C12),
            fwp.firmware_part("xz24",          0x0023913A, 0x0023A336 - 0x0023913A),
            fwp.firmware_part("xz25",          0x0023A336, 0x0023ED6A - 0x0023A336),
            fwp.firmware_part("xz26",          0x0023ED6A, 0x002441FE - 0x0023ED6A),
            fwp.firmware_part("xz27",          0x002441FE, 0x0024941E - 0x002441FE),
            fwp.firmware_part("xz28",          0x0024941E, 0x0024E79E - 0x0024941E),
            fwp.firmware_part("xz29",          0x0024E79E, 0x00252DC2 - 0x0024E79E),
            fwp.firmware_part("xz30",          0x00252DC2, 0x002583B2 - 0x00252DC2),
            fwp.firmware_part("xz31",          0x002583B2, 0x0026144A - 0x002583B2),
            fwp.firmware_part("xz32",          0x0026144A, 0x00266A0E - 0x0026144A),
            fwp.firmware_part("xz33",          0x00266A0E, 0x0026AC9E - 0x00266A0E),
            fwp.firmware_part("xz34",          0x0026AC9E, 0x0026EB96 - 0x0026AC9E),
            fwp.firmware_part("xz35",          0x0026EB96, 0x0027072A - 0x0026EB96),
            fwp.firmware_part("xz36",          0x0027072A, 0x002745BE - 0x0027072A),
            fwp.firmware_part("xz37",          0x002745BE, 0x00279FCE - 0x002745BE),
            fwp.firmware_part("xz38",          0x00279FCE, 0x0027FE7A - 0x00279FCE),
            fwp.firmware_part("xz39",          0x0027FE7A, 0x00285ADE - 0x0027FE7A),
            fwp.firmware_part("xz40",          0x00285ADE, 0x0028C29A - 0x00285ADE),
            fwp.firmware_part("xz41",          0x0028C29A, 0x00291712 - 0x0028C29A),
            fwp.firmware_part("xz42",          0x00291712, 0x0029772A - 0x00291712),
            fwp.firmware_part("xz43",          0x0029772A, 0x0029D126 - 0x0029772A),
            fwp.firmware_part("xz44",          0x0029D126, 0x002A3BE6 - 0x0029D126),
            fwp.firmware_part("xz45",          0x002A3BE6, 0x002A94E6 - 0x002A3BE6),
            fwp.firmware_part("xz46",          0x002A94E6, 0x002AE1DA - 0x002A94E6),
            fwp.firmware_part("xz47",          0x002AE1DA, 0x002B2E56 - 0x002AE1DA),
            fwp.firmware_part("xz48",          0x002B2E56, 0x002B70D6 - 0x002B2E56),
            fwp.firmware_part("xz49",          0x002B70D6, 0x002BB32E - 0x002B70D6),
            fwp.firmware_part("xz50",          0x002BB32E, 0x002C0376 - 0x002BB32E),
            fwp.firmware_part("xz51",          0x002C0376, 0x002C5B7E - 0x002C0376),
            fwp.firmware_part("xz52",          0x002C5B7E, 0x002CC8CA - 0x002C5B7E),
            fwp.firmware_part("xz53",          0x002CC8CA, 0x002D2396 - 0x002CC8CA),
            fwp.firmware_part("xz54",          0x002D2396, 0x002D78D2 - 0x002D2396),
            fwp.firmware_part("xz55",          0x002D78D2, 0x002DB4F2 - 0x002D78D2),
            fwp.firmware_part("xz56",          0x002DB4F2, 0x002DD082 - 0x002DB4F2),
            fwp.firmware_part("xz57",          0x002DD082, 0x002E1DE2 - 0x002DD082),
            fwp.firmware_part("xz58",          0x002E1DE2, 0x002E6A9E - 0x002E1DE2),
            fwp.firmware_part("xz59",          0x002E6A9E, 0x002EC01A - 0x002E6A9E),
            fwp.firmware_part("xz60",          0x002EC01A, 0x002F19CE - 0x002EC01A),
            fwp.firmware_part("xz61",          0x002F19CE, 0x002FA106 - 0x002F19CE),
            fwp.firmware_part("xz62",          0x002FA106, 0x002FE52E - 0x002FA106),
            fwp.firmware_part("xz63",          0x002FE52E, 0x00301EEA - 0x002FE52E),
            fwp.firmware_part("xz64",          0x00301EEA, 0x003031C2 - 0x00301EEA),
            fwp.firmware_part("xz65",          0x003031C2, 0x00307C22 - 0x003031C2),
            fwp.firmware_part("xz66",          0x00307C22, 0x0030D486 - 0x00307C22),
            fwp.firmware_part("xz67",          0x0030D486, 0x00312A6A - 0x0030D486),
            fwp.firmware_part("xz68",          0x00312A6A, 0x003186BE - 0x00312A6A),
            fwp.firmware_part("xz69",          0x003186BE, 0x0031DF66 - 0x003186BE),
            fwp.firmware_part("xz70",          0x0031DF66, 0x0031E3CA - 0x0031DF66),
            fwp.firmware_part("xz71",          0x0031E3CA, 0x00324AEA - 0x0031E3CA),
            fwp.firmware_part("xz72",          0x00324AEA, 0x003270D2 - 0x00324AEA),
            fwp.firmware_part("xz73",          0x003270D2, 0x0032AB32 - 0x003270D2),
            fwp.firmware_part("xz74",          0x0032AB32, 0x00332B52 - 0x0032AB32),
            fwp.firmware_part("xz75",          0x00332B52, 0x00332E62 - 0x00332B52),
            fwp.firmware_part("xz76",          0x00332E62, 0x00337472 - 0x00332E62),
            fwp.firmware_part("xz77",          0x00337472, 0x0033D632 - 0x00337472),
            fwp.firmware_part("xz78",          0x0033D632, 0x00343866 - 0x0033D632),
            fwp.firmware_part("xz79",          0x00343866, 0x003497FE - 0x00343866),
            fwp.firmware_part("xz80",          0x003497FE, 0x00350602 - 0x003497FE),
            fwp.firmware_part("xz81",          0x00350602, 0x003570E2 - 0x00350602),
            fwp.firmware_part("xz82",          0x003570E2, 0x0035C29A - 0x003570E2),
            fwp.firmware_part("xz83",          0x0035C29A, 0x00360BBE - 0x0035C29A),
            fwp.firmware_part("xz84",          0x00360BBE, 0x00362F62 - 0x00360BBE),
            fwp.firmware_part("xz85",          0x00362F62, 0x00365CCE - 0x00362F62),
            fwp.firmware_part("xz86",          0x00365CCE, 0x0036982E - 0x00365CCE),
            fwp.firmware_part("xz87",          0x0036982E, 0x0036F5C4 - 0x0036982E),
            fwp.firmware_part("xz88",          0x0036F5C4, 0x0036FC4A - 0x0036F5C4),
            fwp.firmware_part("xz89",          0x0036FC4A, 0x003702C0 - 0x0036FC4A),
            fwp.firmware_part("xz90",          0x003702C0, 0x0037114E - 0x003702C0),
            fwp.firmware_part("xz91",          0x0037114E, 0x00371394 - 0x0037114E),
            fwp.firmware_part("xz92",          0x00371394, 0x00371436 - 0x00371394),
            fwp.firmware_part("xz93",          0x00371436, 0x003D0000 - 0x00371436),
            fwp.firmware_part("squashfs",      0x003D0000, 0x006E3CCC - 0x003D0000),
            fwp.firmware_part("gzip1",         0x006E3CCC, 0x00770000 - 0x006E3CCC),
            fwp.firmware_part("jffs2",         0x00770000, 0x00800050 - 0x00770000),
        ]
        """

        # 1.4.3-build251128-rel63757n
        self.firmware_parts = [
            fwp.firmware_part("begin",         0x00000000, 0x00006800 - 0x00000000),
            fwp.firmware_part("uimage_boot0",  0x00006800, 0x00030100 - 0x00006800),
            fwp.firmware_part("gzip0",         0x00030100, 0x00050000 - 0x00030100),
            fwp.firmware_part("uimage_boot1",  0x00050000, 0x00070200 - 0x00050000),
            fwp.firmware_part("uimage_kernel", 0x00070200, 0x001B6D9A - 0x00070200),
            fwp.firmware_part("xz0",           0x001B6D9A, 0x001BE2B2 - 0x001B6D9A),
            fwp.firmware_part("xz1",           0x001BE2B2, 0x001C5BB2 - 0x001BE2B2),
            fwp.firmware_part("xz2",           0x001C5BB2, 0x001CD3AE - 0x001C5BB2),
            fwp.firmware_part("xz3",           0x001CD3AE, 0x001D4FFE - 0x001CD3AE),
            fwp.firmware_part("xz4",           0x001D4FFE, 0x001D54A6 - 0x001D4FFE),
            fwp.firmware_part("xz5",           0x001D54A6, 0x001D8BD6 - 0x001D54A6),
            fwp.firmware_part("xz6",           0x001D8BD6, 0x001DCEFE - 0x001D8BD6),
            fwp.firmware_part("xz7",           0x001DCEFE, 0x001E0932 - 0x001DCEFE),
            fwp.firmware_part("xz8",           0x001E0932, 0x001E3142 - 0x001E0932),
            fwp.firmware_part("xz9",           0x001E3142, 0x001E91AA - 0x001E3142),
            fwp.firmware_part("xz10",          0x001E91AA, 0x001EB9B2 - 0x001E91AA),
            fwp.firmware_part("xz11",          0x001EB9B2, 0x001F0C12 - 0x001EB9B2),
            fwp.firmware_part("xz12",          0x001F0C12, 0x001F23C2 - 0x001F0C12),
            fwp.firmware_part("xz13",          0x001F23C2, 0x001F8252 - 0x001F23C2),
            fwp.firmware_part("xz14",          0x001F8252, 0x001FD26A - 0x001F8252),
            fwp.firmware_part("xz15",          0x001FD26A, 0x002031AA - 0x001FD26A),
            fwp.firmware_part("xz16",          0x002031AA, 0x0020982E - 0x002031AA),
            fwp.firmware_part("xz17",          0x0020982E, 0x0020FA8A - 0x0020982E),
            fwp.firmware_part("xz18",          0x0020FA8A, 0x002158FE - 0x0020FA8A),
            fwp.firmware_part("xz19",          0x002158FE, 0x0021C79A - 0x002158FE),
            fwp.firmware_part("xz20",          0x0021C79A, 0x00222D3E - 0x0021C79A),
            fwp.firmware_part("xz21",          0x00222D3E, 0x00228F96 - 0x00222D3E),
            fwp.firmware_part("xz22",          0x00228F96, 0x0022D056 - 0x00228F96),
            fwp.firmware_part("xz23",          0x0022D056, 0x00235B6A - 0x0022D056),
            fwp.firmware_part("xz24",          0x00235B6A, 0x0023B092 - 0x00235B6A),
            fwp.firmware_part("xz25",          0x0023B092, 0x0023C28E - 0x0023B092),
            fwp.firmware_part("xz26",          0x0023C28E, 0x00240DC6 - 0x0023C28E),
            fwp.firmware_part("xz27",          0x00240DC6, 0x0024699A - 0x00240DC6),
            fwp.firmware_part("xz28",          0x0024699A, 0x0024BED6 - 0x0024699A),
            fwp.firmware_part("xz29",          0x0024BED6, 0x00250F6E - 0x0024BED6),
            fwp.firmware_part("xz30",          0x00250F6E, 0x0025833A - 0x00250F6E),
            fwp.firmware_part("xz31",          0x0025833A, 0x00260CD6 - 0x0025833A),
            fwp.firmware_part("xz32",          0x00260CD6, 0x0026523E - 0x00260CD6),
            fwp.firmware_part("xz33",          0x0026523E, 0x00269186 - 0x0026523E),
            fwp.firmware_part("xz34",          0x00269186, 0x0026A052 - 0x00269186),
            fwp.firmware_part("xz35",          0x0026A052, 0x0026E012 - 0x0026A052),
            fwp.firmware_part("xz36",          0x0026E012, 0x00273786 - 0x0026E012),
            fwp.firmware_part("xz37",          0x00273786, 0x00279A6A - 0x00273786),
            fwp.firmware_part("xz38",          0x00279A6A, 0x0027F20A - 0x00279A6A),
            fwp.firmware_part("xz39",          0x0027F20A, 0x00285B4E - 0x0027F20A),
            fwp.firmware_part("xz40",          0x00285B4E, 0x0028BB82 - 0x00285B4E),
            fwp.firmware_part("xz41",          0x0028BB82, 0x002914AE - 0x0028BB82),
            fwp.firmware_part("xz42",          0x002914AE, 0x0029725A - 0x002914AE),
            fwp.firmware_part("xz43",          0x0029725A, 0x0029CB82 - 0x0029725A),
            fwp.firmware_part("xz44",          0x0029CB82, 0x002A358E - 0x0029CB82),
            fwp.firmware_part("xz45",          0x002A358E, 0x002A9242 - 0x002A358E),
            fwp.firmware_part("xz46",          0x002A9242, 0x002ADD52 - 0x002A9242),
            fwp.firmware_part("xz47",          0x002ADD52, 0x002B28D2 - 0x002ADD52),
            fwp.firmware_part("xz48",          0x002B28D2, 0x002B8C6E - 0x002B28D2),
            fwp.firmware_part("xz49",          0x002B8C6E, 0x002BA65A - 0x002B8C6E),
            fwp.firmware_part("xz50",          0x002BA65A, 0x002BE55A - 0x002BA65A),
            fwp.firmware_part("xz51",          0x002BE55A, 0x002C3576 - 0x002BE55A),
            fwp.firmware_part("xz52",          0x002C3576, 0x002C8D3A - 0x002C3576),
            fwp.firmware_part("xz53",          0x002C8D3A, 0x002CFAD6 - 0x002C8D3A),
            fwp.firmware_part("xz54",          0x002CFAD6, 0x002D55AA - 0x002CFAD6),
            fwp.firmware_part("xz55",          0x002D55AA, 0x002DAAC6 - 0x002D55AA),
            fwp.firmware_part("xz56",          0x002DAAC6, 0x002DE70A - 0x002DAAC6),
            fwp.firmware_part("xz57",          0x002DE70A, 0x002E028E - 0x002DE70A),
            fwp.firmware_part("xz58",          0x002E028E, 0x002E4FA2 - 0x002E028E),
            fwp.firmware_part("xz59",          0x002E4FA2, 0x002E9DF6 - 0x002E4FA2),
            fwp.firmware_part("xz60",          0x002E9DF6, 0x002EF20A - 0x002E9DF6),
            fwp.firmware_part("xz61",          0x002EF20A, 0x002F49E6 - 0x002EF20A),
            fwp.firmware_part("xz62",          0x002F49E6, 0x002FD2B2 - 0x002F49E6),
            fwp.firmware_part("xz63",          0x002FD2B2, 0x003017EE - 0x002FD2B2),
            fwp.firmware_part("xz64",          0x003017EE, 0x0030533A - 0x003017EE),
            fwp.firmware_part("xz65",          0x0030533A, 0x0030673A - 0x0030533A),
            fwp.firmware_part("xz66",          0x0030673A, 0x0030B2A6 - 0x0030673A),
            fwp.firmware_part("xz67",          0x0030B2A6, 0x0031055A - 0x0030B2A6),
            fwp.firmware_part("xz68",          0x0031055A, 0x0031652A - 0x0031055A),
            fwp.firmware_part("xz69",          0x0031652A, 0x0031C4FE - 0x0031652A),
            fwp.firmware_part("xz70",          0x0031C4FE, 0x003225AA - 0x0031C4FE),
            fwp.firmware_part("xz71",          0x003225AA, 0x003284F2 - 0x003225AA),
            fwp.firmware_part("xz72",          0x003284F2, 0x003318CE - 0x003284F2),
            fwp.firmware_part("xz73",          0x003318CE, 0x00333306 - 0x003318CE),
            fwp.firmware_part("xz74",          0x00333306, 0x00339892 - 0x00333306),
            fwp.firmware_part("xz75",          0x00339892, 0x00340886 - 0x00339892),
            fwp.firmware_part("xz76",          0x00340886, 0x00343ADA - 0x00340886),
            fwp.firmware_part("xz77",          0x00343ADA, 0x00349716 - 0x00343ADA),
            fwp.firmware_part("xz78",          0x00349716, 0x00349D22 - 0x00349716),
            fwp.firmware_part("xz79",          0x00349D22, 0x0034D792 - 0x00349D22),
            fwp.firmware_part("xz80",          0x0034D792, 0x00355CB2 - 0x0034D792),
            fwp.firmware_part("xz81",          0x00355CB2, 0x003563C2 - 0x00355CB2),
            fwp.firmware_part("xz82",          0x003563C2, 0x0035912E - 0x003563C2),
            fwp.firmware_part("xz83",          0x0035912E, 0x0035ECFA - 0x0035912E),
            fwp.firmware_part("xz84",          0x0035ECFA, 0x003656CE - 0x0035ECFA),
            fwp.firmware_part("xz85",          0x003656CE, 0x0036BE86 - 0x003656CE),
            fwp.firmware_part("xz86",          0x0036BE86, 0x003721CE - 0x0036BE86),
            fwp.firmware_part("xz87",          0x003721CE, 0x003783AE - 0x003721CE),
            fwp.firmware_part("xz88",          0x003783AE, 0x0037E8D6 - 0x003783AE),
            fwp.firmware_part("xz89",          0x0037E8D6, 0x003855D6 - 0x0037E8D6),
            fwp.firmware_part("xz90",          0x003855D6, 0x0038C1E2 - 0x003855D6),
            fwp.firmware_part("xz91",          0x0038C1E2, 0x003930FE - 0x0038C1E2),
            fwp.firmware_part("xz92",          0x003930FE, 0x0039936E - 0x003930FE),
            fwp.firmware_part("xz93",          0x0039936E, 0x003A0032 - 0x0039936E),
            fwp.firmware_part("xz94",          0x003A0032, 0x003A4146 - 0x003A0032),
            fwp.firmware_part("xz95",          0x003A4146, 0x003A7EEE - 0x003A4146),
            fwp.firmware_part("xz96",          0x003A7EEE, 0x003AD31A - 0x003A7EEE),
            fwp.firmware_part("xz97",          0x003AD31A, 0x003B1B26 - 0x003AD31A),
            fwp.firmware_part("xz98",          0x003B1B26, 0x003B1FC2 - 0x003B1B26),
            fwp.firmware_part("xz99",          0x003B1FC2, 0x003B5F22 - 0x003B1FC2),
            fwp.firmware_part("xz100",         0x003B5F22, 0x003BC9E2 - 0x003B5F22),
            fwp.firmware_part("xz101",         0x003BC9E2, 0x003BF3F0 - 0x003BC9E2),
            fwp.firmware_part("xz102",         0x003BF3F0, 0x003BFA46 - 0x003BF3F0),
            fwp.firmware_part("xz103",         0x003BFA46, 0x003C017C - 0x003BFA46),
            fwp.firmware_part("xz104",         0x003C017C, 0x003C1012 - 0x003C017C),
            fwp.firmware_part("xz105",         0x003C1012, 0x003C13C8 - 0x003C1012),
            fwp.firmware_part("xz106",         0x003C13C8, 0x003C146A - 0x003C13C8),
            fwp.firmware_part("xz107",         0x003C146A, 0x003D0000 - 0x003C146A),
            fwp.firmware_part("squashfs",      0x003D0000, 0x006AD792 - 0x003D0000),
            fwp.firmware_part("xz_tail0",      0x006AD792, 0x006B5CB2 - 0x006AD792),
            fwp.firmware_part("xz_tail1",      0x006B5CB2, 0x006B63C2 - 0x006B5CB2),
            fwp.firmware_part("xz_tail2",      0x006B63C2, 0x006B912E - 0x006B63C2),
            fwp.firmware_part("xz_tail3",      0x006B912E, 0x006BECFA - 0x006B912E),
            fwp.firmware_part("xz_tail4",      0x006BECFA, 0x006C56CE - 0x006BECFA),
            fwp.firmware_part("xz_tail5",      0x006C56CE, 0x006CBE86 - 0x006C56CE),
            fwp.firmware_part("xz_tail6",      0x006CBE86, 0x006D21CE - 0x006CBE86),
            fwp.firmware_part("xz_tail7",      0x006D21CE, 0x006D83AE - 0x006D21CE),
            fwp.firmware_part("xz_tail8",      0x006D83AE, 0x006DE8D6 - 0x006D83AE),
            fwp.firmware_part("xz_tail9",      0x006DE8D6, 0x006E55D6 - 0x006DE8D6),
            fwp.firmware_part("xz_tail10",     0x006E55D6, 0x006EC1E2 - 0x006E55D6),
            fwp.firmware_part("xz_tail11",     0x006EC1E2, 0x006F30FE - 0x006EC1E2),
            fwp.firmware_part("xz_tail12",     0x006F30FE, 0x006F936E - 0x006F30FE),
            fwp.firmware_part("xz_tail13",     0x006F936E, 0x00700032 - 0x006F936E),
            fwp.firmware_part("xz_tail14",     0x00700032, 0x00704146 - 0x00700032),
            fwp.firmware_part("xz_tail15",     0x00704146, 0x00707EEE - 0x00704146),
            fwp.firmware_part("xz_tail16",     0x00707EEE, 0x0070D31A - 0x00707EEE),
            fwp.firmware_part("xz_tail17",     0x0070D31A, 0x00711B26 - 0x0070D31A),
            fwp.firmware_part("xz_tail18",     0x00711B26, 0x00711FC2 - 0x00711B26),
            fwp.firmware_part("xz_tail19",     0x00711FC2, 0x00715F22 - 0x00711FC2),
            fwp.firmware_part("xz_tail20",     0x00715F22, 0x0071C9E2 - 0x00715F22),
            fwp.firmware_part("xz_tail21",     0x0071C9E2, 0x0071F3F0 - 0x0071C9E2),
            fwp.firmware_part("xz_tail22",     0x0071F3F0, 0x0071FA46 - 0x0071F3F0),
            fwp.firmware_part("xz_tail23",     0x0071FA46, 0x0072017C - 0x0071FA46),
            fwp.firmware_part("xz_tail24",     0x0072017C, 0x00721012 - 0x0072017C),
            fwp.firmware_part("xz_tail25",     0x00721012, 0x007213C8 - 0x00721012),
            fwp.firmware_part("xz_tail26",     0x007213C8, 0x0072146A - 0x007213C8),
            fwp.firmware_part("xz_tail27",     0x0072146A, 0x00770000 - 0x0072146A),
            fwp.firmware_part("jffs2",         0x00770000, 0x00800050 - 0x00770000),
        ]
        self.op = None
        self.file = None
        self.argc = len(sys.argv)
        if ( self.argc == 1):
            print("Invalid use, check --help")
            sys.exit()
        elif (self.argc == 2):
            self.op = sys.argv[1]
            if (self.op == "--help"):
                self.help()
                sys.exit()
            else:
                print("Invalid use, check --help")
                sys.exit()
        elif (self.argc == 3):
            print("Invalid use, check --help")
        elif (self.argc == 4):
            self.op = sys.argv[1]
            self.file = sys.argv[2]
            self.path = sys.argv[3]

    def start(self):
        if (self.op == "unpack"):
            file_in = open(self.file, 'rb')
            for part in self.firmware_parts:
                file_out = open(self.path + "/" + part.name, 'wb')
                file_in.seek(part.offset, 0)
                data = file_in.read(part.size)
                file_out.write(data)
                file_out.close()
            file_in.close()
        elif (self.op == "pack"):
            file_out = open(self.file, 'wb')
            for i in range(5, len(self.firmware_parts) - 1):
                part_curr = self.firmware_parts[i]
                part_next = self.firmware_parts[i+1]
                file_in = open(self.path + "/" + part_curr.name, 'rb')
                data = file_in.read(part_curr.size)
                file_out.write(data)
                padding = (part_next.offset - (part_curr.offset + part_curr.size))
                file_out.write(b'\xff' * padding)
                print(f"Padding {part_curr.name} - {hex(padding)}")
                file_in.close()
            file_in = open(self.path + "/" + self.firmware_parts[len(self.firmware_parts)-1].name, 'rb')
            data = file_in.read(self.firmware_parts[len(self.firmware_parts)-1].size)
            file_out.write(data)
            file_in.close()
            padding = (8388688 - (self.firmware_parts[len(self.firmware_parts)-1].offset + self.firmware_parts[len(self.firmware_parts)-1].size))
            file_out.write(b'\xff' * padding)
            print(f"Padding {part_curr.name} - {hex(padding)}")
            file_out.close()

    def help(self):
        print("Usage: python extract.py <operation: (pack/unpack)> <bin-file> <exctraction-path>")

    def print_settings(self):
        print("Operation: " + self.op)
        print("File: " + self.file)

dev = extractor()
dev.start()
