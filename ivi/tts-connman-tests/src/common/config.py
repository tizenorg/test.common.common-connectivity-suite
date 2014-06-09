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
# Description: common code to check the value of a property 
#

# The control server that connects to AP, so that test script can
# set AP parameters through apset script
cm_apset_server = "192.168.x.x"

# The full path of the apset script in control server
cm_apset_server_path= "/usr/local/bin/apset/cisco/apset"

cm_apset_ap_essid = "test-apset-ap"

# The essid of AP, this must be same as in apset script
cm_open_ap_essid = 'test-ivi-open-ap'
cm_wep_ap = {"name" : "test-ivi-wep-ap", "password" : "1234567890"}
cm_wpa2_ap = {"name" : "test-ivi-wpa2-ap", "password" : "12345678"}
cm_isolate_ap = {"name" : "test-ivi-isolate-ap", "password" : "12345678"}
cm_available_ap = {"name" : "test-ivi-avalible-ap", "password" : "12345678"}


# For data transfer testing, we need a peer machine for upload/download
# Since different test environment has different upload/download method
# this test suite just defines configurable varibles for each technology
# Tester should re-configure these varibles, otherwise the result is wrong
# Data Server(peer machin) IP address
cm_data_server_ip_bt='192.168.x.x'
cm_data_server_ip_wifi='192.168.x.x'
#cm_data_server_ip_eth='192.168.x.x'
cm_data_server_ip_eth='192.168.x.x'

#cm_bt_download = 'scp 192.168.x.x:/usr/share/tts-connman-tests/10M /tmp'
#cm_bt_upload = 'scp /usr/share/tts-connman-tests/10M 192.168.x.x:/tmp'
#cm_bt_download = 'scp 127.0.0.1:/usr/share/tts-connman-tests/10M /tmp'
#cm_bt_upload = 'scp /usr/share/tts-connman-tests/10M 127.0.0.1:/tmp'
cm_bt_download = 'scp ' + cm_data_server_ip_bt + ':/usr/share/tts-connman-tests/10M /tmp'
cm_bt_upload = 'scp /usr/share/tts-connman-tests/10M ' + cm_data_server_ip_bt + ':/tmp'

cm_eth_download = 'scp ' + cm_data_server_ip_eth + ':/opt/tts-connman-tests/data/apset.tgz /tmp'
cm_eth_upload = 'scp /opt/tts-connman-tests/data/apset.tgz ' + cm_data_server_ip_eth + ':/tmp'
#cm_eth_download = 'scp 192.168.x.x:/usr/share/tts-connman-tests/10M /tmp'
#cm_eth_upload = 'scp /usr/share/tts-connman-tests/10M 192.168.x.x:/tmp'
# For 3G, We will directly connect to Internet. So we can download
# from Internet. But tester need find a way to upload to Internet so 
# that upload test case works
# Download from Internet, ChangeLog-2.6.33 is about 7.5MB
cm_3g_download = 'wget --no-proxy http://www.kernel.org/pub/linux/kernel/v2.6/ChangeLog-2.6.33'
# Upload to local, please revise accordingly so that to upload
# to Internet automatically
cm_3g_upload = 'curl -x "" --ftp-pasv -v -T /usr/share/tts-connman-tests/10M ftp://anonymous:tizen3gtest@ftp.x.x/pub/incoming/'

# For WiFi, we test data transfer for WEP and PSK. These essids are only used
# for data transfer. Test cases in test set WiFiFeature still need a cisco AP
cm_ap_essid_wep64 = 'test-ivi-wep64-ap' # AP set to shared hidden wep64
cm_ap_wep64_key = '1111111111'
cm_ap_essid_psk = 'test-ivi-psk-ap' # AP set to open broadcast RSN PSK
cm_ap_psk_key = '1111111111'
#cm_wifi_download = 'scp 192.168.x.x:/usr/share/tts-connman-tests/10M /tmp'
#cm_wifi_upload = 'scp /usr/share/tts-connman-tests/10M 192.168.x.x:/tmp'
cm_wifi_download = 'scp ' + cm_data_server_ip_wifi + ':/opt/tts-connman-tests/data/apset.tgz /tmp'
cm_wifi_upload = 'scp /opt/tts-connman-tests/data/apset.tgz ' + cm_data_server_ip_wifi + ':/tmp'

# Give one IP address that in the same network with test devices and AP, using Ping command to check network is accessible
cm_ping_server_ip = '192.168.x.x'

# For testing whether scp network is workable
cm_scp_download = 'scp test@x.x.x:1M /tmp/1M.1'
cm_scp_upload = 'scp /tmp/1M.1 test@x.x.x:/tmp/1M.2'
cm_ssh_rm = 'ssh test@x.x.x rm /tmp/1M.2'
cm_rm = 'rm /tmp/1M.1'
