#!/bin/sh
#DESCR: Check the remote device type after pairing with it.
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

ret=0 
# Get the paired computer type.
# class_number=`${TEST_DEVICE} class $SERV_BD_ADDR`
 Icon_device=`${TEST_DEVICE} Icon $SERV_BD_ADDR`

case $Icon_device in
#case $class_number in
  0) device_type="computer" ;;
  1) device_type="computer" ;;
  2) device_type="phone" ;;
  4) device_type="headset" ;;
  5) device_type="keyboard or mouse" ;;
  *) device_type="not captured" ;;
esac

if [ "${device_type}" = "${SERV_BD_TYPE}" ]; then
    echo "[PASS] Correct! The server device type is $device_type."
else
    if [ "$device_type" = "not captured" ]; then
        echo "[FAIL] Sorry, test case cannot judge what it is. Please inform case maker, thanks!"
    else
        echo "[FAIL] No, the server device is $device_type, but you assign ${SERV_BD_TYPE} in config file."
        ret=1
    fi 
fi

exit $ret
