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

# Enter the case folder
cd `dirname $0`
. ./data/bluetooth_env

# Init BT adapter to up and piscan
adapter_init

# Make a pairing with the server
auto_pair

ret=0

# Local device should support SDP Client, it should be able to browse remote SDP Server.
service_record=`sdptool browse ${SERV_BD_ADDR} | grep "Service Name"`
line=`echo $service_record | wc -l`
if [ 0 -eq $line ]; then
    echo "[FAIL] No SDP Client support"
    ret=1
else
    echo "[PASS] Device support SDP Client, remote server's service list is:"
    echo "$service_record"
fi

exit $ret
