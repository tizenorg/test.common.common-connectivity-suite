#!/bin/sh
#DESCR: Check to get MAC address of the local adapter.
# Copyright (C) 2010 Intel Corporation
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
#
# Authors:
#       Zhang Jingke  <jingke.zhang@intel.com>
# Date Created: 2011/03/24
#
# Modifications:
#          Modificator  Date
#          Content of Modification
#



cd `dirname $0`
. ./data/bluetooth_env

adapter_init


sdptool add --handle=0x10000 FTP
service=`sdptool get 0x10000 |grep "Service Name"`

if [ -n "$service" ]; then
    echo "[PASS] Get local 0x10000 service:Successfuly!"
else
    echo "[FAIL] Get local 0x10000 service:Failed! "
    exit 1
fi


