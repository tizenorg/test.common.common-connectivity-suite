#!/bin/sh
#DESCR: Check FTP (File Transfer Profile) put file
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

subdir="subdir1"

# Create a temporary file
echo "This is a temporary file."> /tmp/tmp_ftp_put.log

# Upload this file to FTP server
${FTP_CLIENT} -d $SERV_BD_ADDR -c $subdir -p /tmp/tmp_ftp_put.log

rm -rf /tmp/tmp_ftp_put.log
 
# Try to get the file count of the folder we just pushed.
newfilecount=`${FTP_CLIENT} -d $SERV_BD_ADDR -c $subdir -l | wc -l`

if [ "$newfilecount" -ne 3 ]; then
    echo "Failed to upload file tmp_ftp_put.log to FTP server!"
    echo "[FAIL] Check FTP file put: Failed"
    exit 1
fi

# remove the file we just pushed
${FTP_CLIENT} -d $SERV_BD_ADDR -c $subdir -r tmp_ftp_put.log

echo "[PASS] Check FTP file put: successfully"
exit 0
