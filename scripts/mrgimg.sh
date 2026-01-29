#!/bin/bash

if [ $# -ne 4 ]; then
    echo "Usage mrgimg.sh <first-part> <size> <second-part> <output-img>"
    exit
fi

echo "Start merging image process..."
echo -ne "                          (0%)\r"
dd if=${1} of=${4} bs=1 count=${2} status=none
echo -ne "##########                (50%)\r"
dd if=${3} of=${4} bs=1 seek=${2} status=none
echo -ne "####################      (100%)"
echo "    Done"
