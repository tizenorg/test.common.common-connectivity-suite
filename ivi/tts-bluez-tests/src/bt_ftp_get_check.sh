#!/bin/sh
#DESCR: Check FTP (File Transfer Profile) file get
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

# after obexd-0.42, the obexd related operation needs an agent in background.
agent_setup

# get subdir1/subdir1_test_file1.txt
filename="subdir1_test_file1.txt" 
md5string="838d95ab225a57b134bcaf5a2ca0a38e"
${FTP_CLIENT} -d $SERV_BD_ADDR -c "subdir1" -g ${filename}

if [ ! -f $filename ]; then
    echo "[FAIL] Test file not got!"
    exit 1
fi

md5string_local=`md5sum $filename | awk '{print $1}'`

if [ "$md5string" != "$md5string_local" ]; then
    echo "[FAIL] md5 string mismatch."
    rm -rf "$filename"
    exit 1
fi

echo "md5 strings are same, file get checking successfully!"
echo "[PASS] Check FTP get file: Successful"

rm -rf "$filename"
exit 0
