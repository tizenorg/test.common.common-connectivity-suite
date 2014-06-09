#!/usr/bin/python
import sys
import os
import subprocess
dir=os.path.dirname(sys.argv[0])+"/common"
sys.path.append(dir)
from common import *

#Created By JH
os.chdir(os.path.dirname(sys.argv[0]))
proc = subprocess.Popen("./simple-agent Name=%s Passphrase=%s" %(cm_available_ap["name"], cm_available_ap["password"]), shell=True)
os.chdir(os.getcwd())
dev = WiFiDevice()
try:
    dev.Connect(cm_available_ap["name"])
finally:
    proc.kill()
EXIT(dev.IsConnected())

sev = dev.GetService()
EXIT(svc.GetProperty("State") == "online")
