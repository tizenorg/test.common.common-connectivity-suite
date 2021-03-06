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
# Description: CM_Stress_Flight
#

import sys
import os
import time
dir=os.path.dirname(sys.argv[0])+"/common"
sys.path.append(dir)
from common import *

if (len(sys.argv) != 2):
    print "Usage: %s <Flight On/Off number> ... " % (sys.argv[0])
    EXIT(False)
round = int(sys.argv[1])

btdev = BTDevice()
if not btdev :
    print "No Bluetooth device, case fails"
    EXIT(False)
btdev.Enable()
btdev.Connect()
if not btdev.IsConnected():
    print "Bluetooth device is not connected, case fails"
    EXIT(False)
wifidev = WiFiDevice()
if not wifidev :
    print "No WiFi device, case fails"
    EXIT(False)
wifidev.Enable()
wifidev.Connect(cm_open_ap_essid)
if not wifidev.IsConnected():
    print "WiFi device is not connected, case fails"
    EXIT(False)

count=1

while count <= round:
    print "At the %s round" % (count)
    print "offline on"
    manager.Offline()
    time.sleep(10)
    print "offline off"
    manager.Online()
    time.sleep(10)
    count += 1
 
print "Now final check WiFi/Bluetooth status"   
btdev.Connect()
if not btdev.IsConnected():
    print "Bluetooth device is not connected, case fails"
    EXIT(False)
wifidev.Connect(cm_open_ap_essid)
if not wifidev.IsConnected():
    print "WiFi device is not connected, case fails"
    EXIT(False)
EXIT(True)

