>>> for service in dbus.SystemBus().list_names():
...    print(service)
...
org.freedesktop.DBus
org.freedesktop.login1
:1.61
org.freedesktop.systemd1
com.redhat.tuned
org.freedesktop.PolicyKit1
:1.10
org.freedesktop.NetworkManager
:1.0
:1.1
com.redhat.ifcfgrh1
:1.2
:1.3
:1.19
:1.6



import dbus
from xml.etree import ElementTree

def rec_intro(bus, service, object_path):
    print(object_path)
    obj = bus.get_object(service, object_path)
    iface = dbus.Interface(obj, 'org.freedesktop.DBus.Introspectable')
    xml_string = iface.Introspect()
    for child in ElementTree.fromstring(xml_string):
        if child.tag == 'node':
            if object_path == '/':
                object_path = ''
            new_path = '/'.join((object_path, child.attrib['name']))
            rec_intro(bus, service, new_path)

bus = dbus.SystemBus()
rec_intro(bus, 'org.freedesktop.DBus', '/org/freedesktop/DBus')
rec_intro(bus, 'org.freedesktop.systemd1', '/org/freedesktop/systemd1/unit')
# /org/freedesktop/systemd1/unit/iptables_2eservice


    sysbus = dbus.SystemBus()


systemd1 = sysbus.get_object('org.freedesktop.systemd1', '/org/freedesktop/systemd1')

manager = dbus.Interface(systemd1, 'org.freedesktop.systemd1.Manager')


manager.ListUnits()

from systemd_dbus.manager import Manager
manager = Manager()
unit = manager.get_unit('crond.service')
unit = manager.get_unit('iptables.service')
print(unit.properties.LoadState, unit.properties.ActiveState, unit.properties.SubState)
(dbus.String(u'loaded', variant_level=1), dbus.String(u'active', variant_level=1), dbus.String(u'exited', variant_level=1))
print(unit.properties.LoadState, unit.properties.ActiveState, unit.properties.SubState)
(dbus.String(u'loaded', variant_level=1), dbus.String(u'active', variant_level=1), dbus.String(u'exited', variant_level=1))



unit = manager.get_unit('iptables.service')
print(unit.properties.LoadState, unit.properties.ActiveState, unit.properties.SubState)
(dbus.String(u'loaded', variant_level=1), dbus.String(u'inactive', variant_level=1), dbus.String(u'dead', variant_level=1))
print(unit.properties.ActiveState)
inactive


print(unit.properties.ActiveState)
inactive



dbus.Interface(sysbus.get_object('org.freedesktop.systemd1', u), 'org.freedesktop.systemd1.Unit')
dbus.Struct((dbus.String(u'iptables.service'), dbus.String(u'IPv4 firewall with iptables'),
 dbus.String(u'loaded'), dbus.String(u'active'), dbus.String(u'exited'),
 dbus.String(u''), dbus.ObjectPath('/org/freedesktop/systemd1/unit/iptables_2eservice'),
 dbus.UInt32(0L), dbus.String(u''), dbus.ObjectPath('/')), signature=None)


import dbus
sysbus = dbus.SystemBus()
systemd1 = sysbus.get_object('org.freedesktop.systemd1', '/org/freedesktop/systemd1/unit/iptables_2eservice')
#proxy = sysbus.get_object('org.freedesktop.systemd1', '/org/freedesktop/systemd1')
manager = dbus.Interface(systemd1, 'org.freedesktop.systemd1')
tables = manager.GetUnit('iptables.service')
crate = sysbus.get_object('org.freedesktop.systemd1', tables)

from dbus import SystemBus
from dbus import Interface
bus = SystemBus()
systemd = bus.get_object('org.freedesktop.systemd1', '/org/freedesktop/systemd1')
manager = Interface(systemd, 'org.freedesktop.systemd1.Manager')
crate_unit = systemd.LoadUnit('iptables.service')
crate = bus.get('.systemd1', crate_unit[0])
crate.Get('org.freedesktop.systemd1.Unit', 'ActiveState')

