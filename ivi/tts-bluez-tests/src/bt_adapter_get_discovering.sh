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

ret=0

# Get local hci0's discovering status, 0 for Not discovering, 
# 1 for adapter is in discovering.
hcitool scan > /dev/null &
discovering=`${TEST_ADAPTER} discovering`

if [ $discovering -ne 1 ]; then
    echo "[FAIL] Bluetooth Adapter is in discovering, but discovering status is: $discovering"
    ret=1
else
    echo "[PASS] Bluetooth Adapter is in discovering, status is: 1"
fi

exit $ret
