#!/bin/sh
#DESCR: Check l2cap socket communication using l2ping
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
# Date Created: 2010/01/12
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

# Ping server for 4 times.
l2ping $SERV_BD_ADDR -c 4 > /tmp/l2ping.log

num_reply=`cat /tmp/l2ping.log | grep "44 bytes from $SERV_BD_ADDR" -c`

rm -rf /tmp/l2ping.log

if [ "$num_reply" -le 0 ]; then
    echo "no response recieved from adaptor $SERV_BD_ADDR"
    echo "[FAIL] Check l2cap socket communication using l2ping: Failed"
    exit 1
else
    echo "l2cap ping check passed, got $num_reply responses from $SERV_BD_ADDR"
    echo "[PASS] Check l2cap socket communication using l2ping: Successfully"
fi

exit 0
