#!/bin/bash

if [ $# -ne 3 ]; then
    echo "Usage mrgimg.sh <part-to-merge> <size> <output-img>"
    exit
fi

cp t48_first_dump.bin cpy

echo "Start merging image process..."
echo -ne "                          (0%)\r"
dd if=cpy of=${3} bs=1 count=${2} status=none
echo -ne "##########                (50%)\r"
dd if=${1} of=${3} bs=1 seek=${2} status=none
echo -ne "####################      (100%)"
echo "    Done"

rm -rf cpy
