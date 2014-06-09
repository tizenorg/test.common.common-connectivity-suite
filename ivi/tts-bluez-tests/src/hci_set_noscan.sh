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

parameter="noscan"
ret=1

adapter_init

${HCICONFIG} ${adapter} ${parameter}
${HCICONGIH} > ${tmp_file}
grep -w "PSCAN ISCAN" ${tmp_file}
ret=$?


if [ ${ret} -ne 0 ];then
    echo "[PASS] Set ${parameter} successfuly!"
else
    echo "[FAIL] Set ${parameter} fail! "
    ret=1
fi

${HCICONFIG} ${adapter} piscan
rm -r ${tmp_file}
exit ${ret} 
