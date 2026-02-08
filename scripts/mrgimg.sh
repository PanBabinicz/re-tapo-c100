#!/bin/bash

if [ $# -ne 4 ]; then
    echo "Usage mrgimg.sh <part-to-merge> <original-img> <size> <output-img>"
    exit
fi

cp ${2} cpy

echo "Start merging image process..."
echo -ne "                          (0%)\r"
dd if=cpy of=${4} bs=1 count=${3} status=none
echo -ne "##########                (50%)\r"
dd if=${1} of=${4} bs=1 seek=${3} status=none
echo -ne "####################      (100%)"
echo "    Done"

rm -rf cpy
