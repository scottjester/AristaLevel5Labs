import yaml
from cvplibrary import CVPGlobalVariables, GlobalVariableNames
hostname = CVPGlobalVariables.getValue(GlobalVariableNames.CVP_SERIAL)
config = """
spine1-DC1:
  interfaces:
    loopback0:
      ipv4: 192.168.101.101
      mask: 32
    Ethernet2:
      ipv4: 192.168.103.1
      mask: 31
    Ethernet3:
      ipv4: 192.168.103.7
      mask: 31
    Ethernet4:
      ipv4: 192.168.103.13
      mask: 31
    Ethernet5:
      ipv4: 192.168.103.19
      mask: 31
    Ethernet6:
      ipv4: 192.168.103.25
      mask: 31
    Ethernet7:
      ipv4: 192.168.103.31
      mask: 31     
  bgp:
    asn: 65100
"""

switches = yaml.safe_load(config)


print("service routing protocols model multi-agent")
print("ip prefix-list LOOPBACK")
#prefix-list loop
pl = ['192.168.101.0/24', '192.168.102.0/24', '192.168.201.0/24', '192.168.202.0/24']
for ip in pl:
    print(" permit %s" % ip)
print("route-map LOOPBACK permit 10")
print("match ip address prefix-list LOOPBACK")
print("peer-filter LEAF-AS-RANGE")
print("10 match as-range 65000-65535 result accept")
#BGP ASN
bgpasn = switches[hostname]['bgp']['asn']
print("router bgp %s") % bgpasn
#Loopback0 IP  
ip = switches[hostname]['interfaces']['loopback0']['ipv4']
print(" router-id %s") % ip
print(" no bgp default ipv4-unicast")
print(" maximum-paths 3")
print(" distance bgp 20 200 200")
print(" bgp listen range 192.168.0.0/16 peer-group LEAF_Underlay peer-filter LEAF-AS-RANGE")
print(" neighbor LEAF_Underlay peer group")
print(" neighbor LEAF_Underlay send-community")
print(" neighbor LEAF_Underlay maximum-routes 12000")
print(" redistribute connected route-map LOOPBACK")
print(" address-family ipv4")
print("  neighbor LEAF_Underlay activate")
print("  redistribute connected route-map LOOPBACK")