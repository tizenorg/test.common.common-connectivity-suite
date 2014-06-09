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


cd `dirname $0`
. ./data/bluetooth_env

ret=1
adapter_init
auto_pair
agent_setup

subdir="subdir1"
wrong_folder="subdir4"

echo "This is a temporary file."> /tmp/tmp_ftp_put.log

${FTP_CLIENT} -d $SERV_BD_ADDR -c $wrong_folder -p /tmp/tmp_ftp_put.log
ret=$?

if [ ${ret} -eq 0 ] ; then
    echo "Can not put this file because the folder is wrong!"
    echo "[PASS] Check FTP put wrong folder:Successfuly!"
    rm -rf /tmp/tmp_ftp_put.log
else
    echo "[FAIL] Check FTP put wrong folder:Failed!"
fi 
exit ${ret}
