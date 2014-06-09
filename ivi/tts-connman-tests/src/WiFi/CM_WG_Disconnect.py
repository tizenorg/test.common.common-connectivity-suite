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
# Description: CM_WG_Disconnect
#

import sys
import os
dir=os.path.dirname(sys.argv[0])+"/common"
sys.path.append(dir)
from common import *

dev = WiFiDevice()
dev.Connect(cm_open_ap_essid)
if dev.IsConnected() == False:
    print 'The Wifi is not connected'
    Exit(False)

svc = dev.GetService()
svc.Disconnect()
EXIT(dev.IsConnected() == False)
