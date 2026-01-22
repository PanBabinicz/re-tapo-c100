import sys

class firmware_part:
    def __init__(self, name, offset, size):
        self.name = name
        self.offset = offset
        self.size = size

firmware_parts = [
    firmware_part("begin", 0x0, 0x6800),
    firmware_part("uimage0", 0x6800, 82133),
    firmware_part("gzip0", 0x30100, 53568),
    firmware_part("uimage1", 0x50000, 66729),
    firmware_part("uimage2", 0x70200, 1298384),
    firmware_part("xz0", 0x1B6E36, 30012),
    firmware_part("xz1", 0x1BE372, 31052),
    firmware_part("xz2", 0x1C5CBE, 30800),
    firmware_part("xz3", 0x1CD50E, 26280),
    firmware_part("xz4", 0x1D3BB6, 14656),
    firmware_part("xz5", 0x1D74F6, 17192),
    firmware_part("xz6", 0x1DB81E, 14900),
    firmware_part("xz7", 0x1DF252, 10256),
    firmware_part("xz8", 0x1E1A62, 22512),
    firmware_part("xz9", 0x1E7252, 10248),
    firmware_part("xz10", 0x1E9A5A, 21088),
    firmware_part("xz11", 0x1EECBA, 6064),
    firmware_part("xz12", 0x1F046A, 24208),
    firmware_part("xz13", 0x1F62FA, 20504),
    firmware_part("xz14", 0x1FB312, 24384),
    firmware_part("xz15", 0x201252, 26244),
    firmware_part("xz16", 0x2078D6, 25180),
    firmware_part("xz17", 0x20DB32, 24180),
    firmware_part("xz18", 0x2139A6, 28316),
    firmware_part("xz19", 0x21A842, 26020),
    firmware_part("xz20", 0x220DE6, 25176),
    firmware_part("xz21", 0x22703E, 16576),
    firmware_part("xz22", 0x22B0FE, 35604),
    firmware_part("xz23", 0x233C12, 21800),
    firmware_part("xz24", 0x23913A, 4604),
    firmware_part("xz25", 0x23A336, 18996),
    firmware_part("xz26", 0x23ED6A, 21652),
    firmware_part("xz27", 0x2441FE, 21024),
    firmware_part("xz28", 0x24941E, 21376),
    firmware_part("xz29", 0x24E79E, 17956),
    firmware_part("xz30", 0x252DC2, 22000),
    firmware_part("xz31", 0x2583B2, 37016),
    firmware_part("xz32", 0x26144A, 21956),
    firmware_part("xz33", 0x266A0E, 17040),
    firmware_part("xz34", 0x26AC9E, 16120),
    firmware_part("xz35", 0x26EB96, 7060),
    firmware_part("xz36", 0x27072A, 16020),
    firmware_part("xz37", 0x2745BE, 23056),
    firmware_part("xz38", 0x279FCE, 24236),
    firmware_part("xz39", 0x27FE7A, 23652),
    firmware_part("xz40", 0x285ADE, 26556),
    firmware_part("xz41", 0x28C29A, 21624),
    firmware_part("xz42", 0x291712, 24600),
    firmware_part("xz43", 0x29772A, 23036),
    firmware_part("xz44", 0x29D126, 27328),
    firmware_part("xz45", 0x2A3BE6, 22784),
    firmware_part("xz46", 0x2A94E6, 19700),
    firmware_part("xz47", 0x2AE1DA, 19580),
    firmware_part("xz48", 0x2B2E56, 17024),
    firmware_part("xz49", 0x2B70D6, 16984),
    firmware_part("xz50", 0x2BB32E, 20552),
    firmware_part("xz51", 0x2C0376, 22536),
    firmware_part("xz52", 0x2C5B7E, 27980),
    firmware_part("xz53", 0x2CC8CA, 23244),
    firmware_part("xz54", 0x2D2396, 21820),
    firmware_part("xz55", 0x2D78D2, 15392),
    firmware_part("xz56", 0x2DB4F2, 7056),
    firmware_part("xz57", 0x2DD082, 19808),
    firmware_part("xz58", 0x2E1DE2, 19644),
    firmware_part("xz59", 0x2E6A9E, 21884),
    firmware_part("xz60", 0x2EC01A, 22964),
    firmware_part("xz61", 0x2F19CE, 34616),
    firmware_part("xz62", 0x2FA106, 17448),
    firmware_part("xz63", 0x2FE52E, 14780),
    firmware_part("xz64", 0x301EEA, 4824),
    firmware_part("xz65", 0x3031C2, 19040),
    firmware_part("xz66", 0x307C22, 22628),
    firmware_part("xz67", 0x30D486, 21988),
    firmware_part("xz68", 0x312A6A, 23636),
    firmware_part("xz69", 0x3186BE, 22696),
    firmware_part("xz70", 0x31DF66, 1124),
    firmware_part("xz71", 0x31E3CA, 26400),
    firmware_part("xz72", 0x324AEA, 9704),
    firmware_part("xz73", 0x3270D2, 14944),
    firmware_part("xz74", 0x32AB32, 32800),
    firmware_part("xz75", 0x332B52, 784),
    firmware_part("xz76", 0x332E62, 17936),
    firmware_part("xz77", 0x337472, 25024),
    firmware_part("xz78", 0x33D632, 25140),
    firmware_part("xz79", 0x343866, 24472),
    firmware_part("xz80", 0x3497FE, 28164),
    firmware_part("xz81", 0x350602, 27360),
    firmware_part("xz82", 0x3570E2, 20920),
    firmware_part("xz83", 0x35C29A, 18724),
    firmware_part("xz84", 0x360BBE, 9124),
    firmware_part("xz85", 0x362F62, 11628),
    firmware_part("xz86", 0x365CCE, 15200),
    firmware_part("xz87", 0x36982E, 23956),
    firmware_part("xz88", 0x36F5C4, 1668),
    firmware_part("xz89", 0x36FC4A, 1652),
    firmware_part("xz90", 0x3702C0, 3724),
    firmware_part("xz91", 0x37114E, 580),
    firmware_part("xz92", 0x371394, 152),
    firmware_part("xz93", 0x371436, 884),
    firmware_part("squashfs0", 0x3D0000, 3225548),
    firmware_part("gzip1", 0x6E3CCC, 53568),
    firmware_part("jffs0", 0x770000, 491532)
]

class extractor:
    def __init__(self):
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

    def start(self, parts):
        if (self.op == "unpack"):
            file_in = open(self.file, 'rb')
            for part in parts:
                file_out = open(self.path + "/" + part.name, 'wb')
                file_in.seek(part.offset, 0)
                data = file_in.read(part.size)
                file_out.write(data)
                file_out.close()
            file_in.close()
        elif (self.op == "pack"):
            file_out = open(self.file, 'wb')
            for i in range(0, len(parts) - 1):
                part_curr = parts[i]
                part_next = parts[i+1]
                file_in = open(self.path + "/" + part_curr.name, 'rb')
                data = file_in.read(part_curr.size)
                file_out.write(data)
                padding = (part_next.offset - (part_curr.offset + part_curr.size))
                file_out.write(b'\xff' * padding)
                print(f"Padding {part_curr.name} - {hex(padding)}")
                file_in.close()
            file_in = open(self.path + "/" + parts[len(parts)-1].name, 'rb')
            data = file_in.read(parts[len(parts)-1].size)
            file_out.write(data)
            file_in.close()
            padding = (8388688 - (parts[len(parts)-1].offset + parts[len(parts)-1].size))
            file_out.write(b'\xff' * padding)
            print(f"Padding {part_curr.name} - {hex(padding)}")
            file_out.close()

    def help(self):
        print("Usage: python extract.py <operation: (pack/unpack)> <bin-file> <exctraction-path>")

    def print_settings(self):
        print("Operation: " + self.op)
        print("File: " + self.file)

dev = extractor()

#dev.print_settings()
dev.start(firmware_parts)
