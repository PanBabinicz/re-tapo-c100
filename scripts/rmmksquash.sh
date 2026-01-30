#!/bin/bash

rm -rf squashfs0
mksquashfs squashfs-root/ squashfs0 -comp xz -b 65536
binwalk squashfs0
