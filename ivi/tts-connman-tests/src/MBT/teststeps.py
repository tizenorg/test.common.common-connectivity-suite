"""
This library implements test steps for ConnMan models.
"""

import dbus
import fmbt
import time

bus = dbus.SystemBus()

manager = dbus.Interface(bus.get_object("net.connman", "/"),
                         "net.connman.Manager")

known_wifis = set([])

known_bluetooth = set([])

# connected_services is a map:
#     technology_name -> service_path
# that contain latest connected technologies and services
connected_services = {}

g_last_powerup = time.time()

def addWifi(wifi_name):
    global known_wifis
    known_wifis.add(wifi_name)

def addBt(bt_name):
    global known_bluetooth
    knwn_bluetooth.add(bt_name)

def iPowerUp(techname):
    global g_last_powerup
    RETRY_LIMIT = 5
    tech = dbus.Interface(bus.get_object("net.connman", "/net/connman/technology/" + techname),
                          "net.connman.Technology")
    counter = 0
    while 1:
        try:
            tech.SetProperty("Powered", True)
            break # if no exceptions
        except Exception, e:
            fmbt.adapterlog("Got exception: %s" % (e,))
            if not ("InvalidArguments" in str(e) or "InvalidProperty" in str(e)):
                fmbt.adapterlog("BUG: undocumented exception")
        counter += 1
        time.sleep(1)
        assert counter < RETRY_LIMIT, "Maximum number of retries"
    time.sleep(3)
    fmbt.adapterlog("tech.GetProperties()['Powered'] = %s" % (tech.GetProperties()["Powered"],))
    assert tech.GetProperties()["Powered"], "Powered == False according to properties"
    g_last_powerup = time.time()

def iPowerDown(techname):
    tech = dbus.Interface(bus.get_object("net.connman",
                                         "/net/connman/technology/" + techname),
                          "net.connman.Technology")
    tech.SetProperty("Powered", False)

def iScan(techname):
    tech = dbus.Interface(bus.get_object("net.connman",
                                         "/net/connman/technology/" + techname),
                          "net.connman.Technology")
    if g_last_powerup + 5 > time.time():
        time.sleep(g_last_powerup + 5 - time.time())
    tech.Scan()

def iConnect(techname):
    RETRY_LIMIT = 5
    if techname == "wifi":
        can_connect = known_wifis
    elif techname == "bluetooth":
        can_connect = known_bluetooth
    else:
        fmbt.adapterlog("Don't know which services to connect via tech %s." % (techname,))

    # Look for a suitable service (one of known_*)
    connect_me = None
    counter = 0
    while 1:
        found_services = manager.GetServices()
        for service_path, properties in found_services:
            fmbt.adapterlog("    GetServices(): %s (%s)" % (service_path, properties["Name"]))
            if str(service_path).split("/")[-1].startswith(techname) and properties["Name"] in can_connect:
                connect_me = service_path
                break
        if connect_me != None:
            break
        counter += 1
        assert counter < RETRY_LIMIT, "Maximum number of retries"
        fmbt.adapterlog("Known services not found, retrying after 2 second...")
        time.sleep(2)

    # Connect to the found service
    fmbt.adapterlog('Connecting to service "%s"' % (properties["Name"],))
    service = dbus.Interface(bus.get_object("net.connman", service_path),
                             "net.connman.Service")
    service.Connect(timeout=5000)
    connected_services[techname] = service_path

def iDisconnect(techname):
    if techname in connected_services:
        service = dbus.Interface(bus.get_object("net.connman", connected_services[techname]),
                                 "net.connman.Service")
        service.Disconnect()

def iConnected(techname):
    for service_path, properties in manager.GetServices():
        if properties["Type"] == techname and properties["State"] in ["ready", "online"]:
            return True
    return False
