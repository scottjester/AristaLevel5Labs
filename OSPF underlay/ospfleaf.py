import yaml
from cvplibrary import CVPGlobalVariables, GlobalVariableNames
hostname = CVPGlobalVariables.getValue(GlobalVariableNames.CVP_SERIAL)
config = """
borderleaf1-DC1:
  loopback0:
    ipv4: 192.168.101.21
    mask: 32
  loopback1:
    ipv4: 192.168.102.21
    mask: 32  
borderleaf2-DC1:
  loopback0:
    ipv4: 192.168.101.22
    mask: 32
  loopback1:
    ipv4: 192.168.102.21
    mask: 32
leaf1-DC1
  loopback0:
    ipv4: 192.168.101.11
    mask: 32
  loopback1:
    ipv4: 192.168.102.11
    mask: 32
leaf2-DC1
  loopback0:
    ipv4: 192.168.101.12
    mask: 32
  loopback1:
    ipv4: 192.168.102.11
    mask: 32
leaf3-DC1
  loopback0:
    ipv4: 192.168.101.13
    mask: 32
  loopback1:
    ipv4: 192.168.102.13
    mask: 32
leaf4-DC1
  loopback0:
    ipv4: 192.168.101.14
    mask: 32
  loopback1:
    ipv4: 192.168.102.13
    mask: 32
borderleaf1-DC2:
  loopback0:
    ipv4: 192.168.201.21
    mask: 32
  loopback1:
    ipv4: 192.168.202.21
    mask: 32  
borderleaf2-DC2:
  loopback0:
    ipv4: 192.168.201.22
    mask: 32
  loopback1:
    ipv4: 192.168.202.21
    mask: 32
leaf1-DC2
  loopback0:
    ipv4: 192.168.201.11
    mask: 32
  loopback1:
    ipv4: 192.168.202.11
    mask: 32
leaf2-DC2
  loopback0:
    ipv4: 192.168.201.12
    mask: 32
  loopback1:
    ipv4: 192.168.202.11
    mask: 32
leaf3-DC2
  loopback0:
    ipv4: 192.168.201.13
    mask: 32
  loopback1:
    ipv4: 192.168.202.13
    mask: 32
leaf4-DC2
  loopback0:
    ipv4: 192.168.201.14
    mask: 32
  loopback1:
    ipv4: 192.168.202.13
    mask: 32                  
"""

switches = yaml.safe_load(config)

ip = switches['leaf4-DC2']['loopback0']['ipv4']
mask = switches['leaf4-DC2']['loopback0']['ipv4']['mask']
print("interface loopback0")
print("ip address %s/%s") % ip % mask
print("router ospf 100")
print(" router-id %s") % ip