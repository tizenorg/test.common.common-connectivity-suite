#!/bin/sh
#DESCR: Check FTP (File transfer profile) folder navigation from FTP client.
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
# Date Created: 2010/01/18
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

# Change to the sub directory just selected and browse the content of it
${FTP_CLIENT} -d $SERV_BD_ADDR -c "subdir1" -l > /tmp/tmp_folder_nav.log

# Check file count property of the sub directory
row_count=`wc -l /tmp/tmp_folder_nav.log | awk '{print $1}'`

# Compare the server info file and folder count we get
if [ "$row_count" -ne 2 ]; then
    echo "[FAIL] Check folder navigation and browse: Failed"
    exit 1
fi

# Delete the temporary files
rm -rf /tmp/tmp_folder_nav.log

echo "[PASS] Check folder navigation and browse: Successful"
exit 0
