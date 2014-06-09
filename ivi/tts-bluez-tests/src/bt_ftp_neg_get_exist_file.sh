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

#set -x

cd `dirname $0`
. ./data/bluetooth_env

ret=1
adapter_init
auto_pair
agent_setup

filename="subdir1_test_file1.txt" 
md5string="838d95ab225a57b134bcaf5a2ca0a38e"
touch ${filename}
${FTP_CLIENT} -d $SERV_BD_ADDR -c "subdir1" -g ${filename}
md5string_local=`md5sum $filename |awk '{print $1}'`

# Check if the original file is covered.
if [ "$md5string_local" != "$md5string" ]; then
    echo "[FAIL] Check FTP get exist file:Failed!"
else
    echo "[PASS] Check FTP get exist file:Successfuly!"
fi

rm -r ${filename}
exit ${ret}
