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
# Description: CM_WA_RememberPasswd
#

import sys
import os
import subprocess
dir=os.path.dirname(sys.argv[0])+"/common"
sys.path.append(dir)
from common import *

#Updated By JH
#manager.RequestScan()
#svc = manager.GetServiceByName(cm_wpa2_ap["name"])
#if svc == None:
#    print "There is no AP named %s" % cm_wpa2_ap["name"]
#    EXIT(False)
#try:
#    if svc.GeProperty("Favorite"):
#        svc.Remove()
#except dbus.DBusException, error:
#    pass
os.chdir(os.path.dirname(sys.argv[0]))
proc = subprocess.Popen("./simple-agent Name=%s Passphrase=%s" % (cm_wpa2_ap["name"], cm_wpa2_ap["password"]), shell=True)
os.chdir(os.getcwd())
dev = WiFiDevice()
try:
    dev.Connect(cm_wpa2_ap["name"])
finally:
    proc.kill()

if not dev.IsConnected():
    print "Can't connected to %s with password: %s"  % (cm_wpa2_ap["name"], cm_wpa2_ap["password"])
    EXIT(False)
try:
    dev.Disconnect()
except dbus.DBusException, error:
    pass
if dev.IsConnected():
    print "Can't disconnected %s" % cm_wpa2_ap["name"]

dev.Connect(cm_wpa2_ap["name"])
EXIT(dev.IsConnected())


#if manager.ConnectWiFi('1111000000', 'wep64', 1, 0, 1) == False:
#    print 'Cannot access WiFi'
#    EXIT(False)
#svc = manager.GetServiceByName('shz13-otc-cisco-cm')
#if svc == None:
#    print 'There is no AP named shz13-otc-cisco-cm'
#    EXIT(False)
#try:
#    svc.Disconnect()
#except dbus.DBusException, error:
#    pass
#
#print 'Connecting to Guest Network'
#dev = WiFiGuestDevice()
#svc1 = dev.GetService()
#props = svc1.GetProperties()
#print 'name is %s' % props['Name']
#if svc1.BroadcastPing(1400):
#    print 'Connected'
#else:
#    print 'Not connected'
#    EXIT(False)
#
#del manager
#manager = Manager()
#svc = manager.GetServiceByName('shz13-otc-cisco-cm')
#if svc == None:
#    print 'There is no AP named shz13-otc-cisco-cm'
#    EXIT(False)
#print 'Connecting to first AP without providing password'
#svc.Connect()
#if svc.BroadcastPing(1400):
#    print 'Connected'
#else:
#    print 'Not connected'
#    EXIT(False)
#
#EXIT(True)
