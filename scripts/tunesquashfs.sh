#!/bin/bash

if [ $# -ne 5 ]; then
    echo "Usage tunesquashfs.sh <squashfs-root-dir> <block-size> <compression> <expected-size> <squashfs-output>"
    exit
fi

while true; do
    rm -rf ${5} 2> /dev/null
    mksquashfs ${1} ${5} -comp ${3} -b ${2} -no-exports -noappend

    random=$(tr -dc A-Za-z0-9 < /dev/urandom | head -c 13; echo)
    size=$(unsquashfs -s ${5} | grep "Filesystem size" | grep -oE "[0-9]+{6}")
    temp=2

    if [ ${size} -eq ${4} ]; then
        echo "Equal"
        rm -rf 2 2> /dev/null
        exit
    elif [ ${size} -lt ${4} ]; then
        echo "Add"
        echo ${random} >> squashfs-root/lib/audio/Red_Alert.g711
    elif [ ${size} -gt ${4} ]; then
        echo "Remove"
        head -c -7 squashfs-root/lib/audio/Red_Alert.g711 > 2
        cat 2 > squashfs-root/lib/audio/Red_Alert.g711
    fi

    echo "Current size = ${size}"
    sleep 0.2
done
