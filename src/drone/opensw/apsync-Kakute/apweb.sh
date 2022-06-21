#!/bin/bash

set -e
set -x

rm -rf APWeb

sudo apt install python-pip libtalloc-dev -y
pip2 install future --user

[ -d ~/APWeb ] || {
    git clone -b video_streaming https://github.com/shortstheory/APWeb.git
}
pushd ~/APWeb
 git submodule update --init --recursive
 make CFLAGS=-Wno-error
popd

sudo cp ~/apsync-Kakute/APWeb.service /etc/systemd/system/APWeb.service
sudo systemctl enable APWeb.service
sudo systemctl start APWeb.service
