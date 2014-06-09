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


cd `dirname $0`
. ./data/bluetooth_env

adapter_init
auto_pair
agent_setup

subdir="subdir1"
tmp_folder_name="tmp_folder_name1"
tmp_file_name="tmp_ftp"
tmp1_file_name="tmp_file"

${FTP_CLIENT} -d $SERV_BD_ADDR -C $tmp_folder_name

${FTP_CLIENT} -d $SERV_BD_ADDR -l > tmp_ftp_folder.log
created=`grep "$tmp_folder_name" ./tmp_ftp_folder.log -c`
if [ $created -le 0 ]; then
    echo "The folder $tmp_folder_name is not created!"
    echo "Check FTP folder create: Failed"
    rm -rf ./tmp_ftp_folder.log
    exit 1
fi

echo "This is a temporary file used to test FTP file remove under new folder."> $tmp_file_name

${FTP_CLIENT} -d $SERV_BD_ADDR -c $tmp_folder_name -p `pwd`/$tmp_file_name

${FTP_CLIENT} -d $SERV_BD_ADDR -c $tmp_folder_name -l > tmp_ftp_folder.log
exist=`grep "$tmp_file_name" ./tmp_ftp_folder.log -c`
if [ $exist -ne 1 ]; then
    echo "Failed to create the file $tmp_file_name under folder $tmp_folder_name!"
    rm -rf ./tmp_ftp_folder.log
    exit 1
fi

${FTP_CLIENT} -d $SERV_BD_ADDR -c $tmp_folder_name -r $tmp1_file_name

${FTP_CLIENT} -d $SERV_BD_ADDR -c $tmp_folder_name -l > tmp_ftp_folder.log
exist=`grep "$tmp_file_name" ./tmp_ftp_folder.log -c`
if [ $exist -gt 0 ]; then
    echo "Can not  delete the file $tmp1_file_name under folder $tmp_folder_name!"
    echo "[PASS] Check FTP noexist file remove: successfuly"
    rm -rf ./tmp_ftp_folder.log
    rm -r $tmp_file_name
    exit 0
fi

rm -rf ./tmp_ftp_folder.log
rm -f $tmp_file_name

echo "[FAIL] Check FTP noexist file remove: Failed"
exit 0
