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
# Description: CM_WS_WEP_Download
#

import sys
import os
dir=os.path.dirname(sys.argv[0])+"/common"
sys.path.append(dir)
from common import *

#manager.Startup3G()
dev = C3GDevice()
if dev.device == None:
    print "No 3G Device!"
    #manager.Cleanup()
    EXIT(False)
dev.Connect()
if dev.IsConnected() == False:
    print 'The 3G service is not connected'
    #manager.Cleanup()
    EXIT(False)
props=dev.GetService().GetProperties()
name = props["Name"]
ret = commands.getstatusoutput("/opt/tts-connman-tests/common/bearer.sh " + name +" Disconnect")
print ret[1]
EXIT(dev.IsConnected() == False)
ret=(dev.IsConnected() == False)
#manager.Cleanup()
EXIT(ret)
