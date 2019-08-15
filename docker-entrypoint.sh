#!/usr/bin/env bash
exec python3 /usr/src/ioiprint/run.py


# added by Emil Abbasov (IOI2019) to fix the container timezone issue
export DEBIAN_FRONTEND=noninteractive

ln -fs /usr/share/zoneinfo/Asia/Baku /etc/localtime
apt-get install -y tzdata
dpkg-reconfigure --frontend noninteractive tzdata