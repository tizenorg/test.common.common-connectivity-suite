#!/usr/bin/python
import sys
import os
import subprocess
dir=os.path.dirname(sys.argv[0])+"/common"
sys.path.append(dir)
from common import *

#Created By JH
proc = subprocess.Popen("./simple-agent Name=%s Passphrase=%s" %(cm_isolate_ap["name"], cm_isolate_ap["password"]), shell=True)
dev = WiFiDevice()
try:
    dev.Connect(cm_isolate_ap["name"])
finally:
    proc.kill()
EXIT(dev.IsConnected())

sev = dev.GetService()
EXIT(svc.GetProperty("State") == "ready")
