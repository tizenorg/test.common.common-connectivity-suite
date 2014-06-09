#!/bin/sh
set -x
#DESCR: Check OPP (Objects Push Profile) by putting files to OPP server
# Copyright (C) 2010 Intel Corporation
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
# Date Created: 2010/12/23
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

# Get the last opp test file number on server root dir.
oldfilecount=`${FTP_CLIENT} -d $SERV_BD_ADDR -l | grep -c "tmp_opp_send"`
opp_lastfile_number=`${FTP_CLIENT} -d $SERV_BD_ADDR -l | grep "tmp_opp_send" | awk -v max=0 -F"_" '{if($NF>max) {max=$NF ; print max}}' | tail -n 1`

# Create 3 temporary files, whose suffix number is bigger than last file number
temp_number=3

i=0
while [ $i -lt $temp_number ]; 
do
    temp_file="tmp_opp_send_`expr ${opp_lastfile_number} + 1`"
    cp ${DATA_DIR}/object $temp_file   
    ${DATA_DIR}/opp-client -d $SERV_BD_ADDR -s $temp_file
    ((i++))
    ((opp_lastfile_number++))
done

# Upload this file to FTP server, if the file is not text, server will use 
# OPP (channel 9) to receive

rm -rf tmp_opp_send_*
 
# Try to get the file count of the folder we just pushed.
newfilecount=`${FTP_CLIENT} -d $SERV_BD_ADDR -l | grep -c "tmp_opp_send"`

if [ $newfilecount -ne `expr $oldfilecount + $temp_number` ]; then
    echo "Failed to upload files tmp_opp_send_* to OPP server!"
    echo "[FAIL] Check OPP file put: Failed"
    exit 1
fi

echo "[PASS] Check OPP files put: successfully"
exit 0
