import sys
import firmware_part as fwp

class extractor:
    def __init__(self):
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
