#!/bin/bash

while true; do
    rm -rf squashfs0_test7
    mksquashfs squashfs-root/ squashfs0_test7 -comp xz -b 65536

    random_num=$(tr -dc 0-9 < /dev/urandom | head -c 1; echo)
    random=$(tr -dc A-Za-z0-9 < /dev/urandom | head -c 13; echo)
    size=$(unsquashfs -s squashfs0_test7 | grep "Filesystem size" | grep -oE "[0-9]+{6}")
    temp=2

    if [ ${size} -eq 3225548 ]; then
        echo "Equal"
        exit
    elif [ ${size} -lt 3225548 ]; then
        echo "Add"
        echo ${random} >> squashfs-root/lib/audio/Red_Alert.g711
    elif [ ${size} -gt 3225548 ]; then
        echo "Remove"
        head -c -1 squashfs-root/lib/audio/Red_Alert.g711 > 2
        cat 2 > squashfs-root/lib/audio/Red_Alert.g711
    fi

    echo ${size}

    sleep 0.2
done
