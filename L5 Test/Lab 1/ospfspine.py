import yaml
from cvplibrary import CVPGlobalVariables, GlobalVariableNames
hostname = CVPGlobalVariables.getValue(GlobalVariableNames.CVP_SERIAL)
config = """
spine1-DC1:
  loopback0:
    ipv4: 192.168.101.101
    mask: 32
spine2-DC1:
  loopback0:
    ipv4: 192.168.101.102
    mask: 32
spine3-DC1:
  loopback0:
    ipv4: 192.168.101.103
    mask: 32
spine1-DC2:
  loopback0:
    ipv4: 192.168.201.101
    mask: 32
spine2-DC2:
  loopback0:
    ipv4: 192.168.201.102
    mask: 32
spine3-DC2:
  loopback0:
    ipv4: 192.168.201.103
    mask: 32          
"""
switches = yaml.safe_load(config)

l0 = switches[hostname]['loopback0']['ipv4']
l0mask = switches[hostname]['loopback0']['mask']
print("interface loopback0")
print(" ip address %s/%s" % (l0, l0mask))
rid = switches[hostname]['loopback0']['ipv4']
print("router ospf 100")
print(" router-id %s") % rid