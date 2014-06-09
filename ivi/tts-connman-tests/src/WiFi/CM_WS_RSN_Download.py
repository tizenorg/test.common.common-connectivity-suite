#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (C) 2010 Intel Corporation.
#
# This program is free software; you can redistribute it and/or modify it
# under the terms and conditions of the GNU General Public License,
# version 2, as published by the Free Software Foundation.
#
# This program is distributed in the hope it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License
# for more details.
#
# You should have received a copy of the GNU General Public License along with
# this program; if not, write to the Free Software Foundation, Inc., 59 Temple
# Place - Suite 330, Boston, MA 02111-1307 USA.
#
# Authors:
#       Jeff Zheng <jeff.zheng@intel.com>
#
# Description: CM_WS_RSN_Download
#

import sys
import os
import subprocess
dir=os.path.dirname(sys.argv[0])+"/common"
sys.path.append(dir)
from common import *

#Updated By JH

#dev = WiFiDevice()
#manager.ConnectAP(cm_ap_essid_rsn, cm_ap_rsn_key, 'rsn', 1, 0, 1)
#EXIT(dev.Download())
proc = subprocess.Popen("./simple-agent Name=%s Passphrase=%s" %(cm_wpa2_ap["name"], cm_wpa2_ap["password"]), shell=True)
dev = WiFiDevice()
dev.Connect(cm_wpa2_ap["name"])
proc.kill()
EXIT(dev.download())

