#!/bin/sh
wget -q -O tmp.zip http://dist.sensapex.com/misc/um-sdk/archive/umsdk-1_022-src.zip \
    && unzip tmp.zip \
    && rm tmp.zip

cd umsdk-1_022/src/lib/ \
    && make -f Makefile.linux

sudo make -f Makefile.linux install
echo $PWD
