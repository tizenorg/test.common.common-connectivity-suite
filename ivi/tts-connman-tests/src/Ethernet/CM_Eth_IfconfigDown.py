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
# Description: CM_Eth_IfconfigDown
#

import sys
import os
dir=os.path.dirname(sys.argv[0])+"/common"
sys.path.append(dir)
import time
from common import *
dev = EthDevice()
svc = dev.GetService()
if svc.BroadcastPing() != True:
    print 'Cannot ping'
    EXIT(False)
ret = dev.ifconfigDown()
if ret == False:
    print 'ifconfig down failure is not connman issue'
    EXIT(True)
time.sleep(2)
dev = EthDevice()
tech = dev.GetTechnology()
properties = tech.GetProperties()
print 'Device Status is now %s' % properties['State']
if properties['State'] == 'available':
    EXIT(False)
dev.ifconfigUP()
time.sleep(5)
EXIT(True)
