import yaml
from cvplibrary import CVPGlobalVariables, GlobalVariableNames
hostname = CVPGlobalVariables.getValue(GlobalVariableNames.CVP_SERIAL)
config = """
spine1-DC1:
  loopback0:
    ipv4: 10.1.0.101
    mask: 32
spine2-DC1:
  loopback0:
    ipv4: 10.1.0.102
    mask: 32
spine3-DC1:
  loopback0:
    ipv4: 10.1.0.103
    mask: 32
"""

switches = yaml.safe_load(config)

print("service routing protocols model multi-agent")
print("ip prefix-list LOOPBACK")
print(" seq 10 permit 10.1.0.0/24 eq 32")
print(" seq 20 permit 10.1.1.0/24 eq 32")
print(" seq 30 permit 10.2.0.0/24 eq 32")
print(" seq 40 permit 10.2.1.0/24 eq 32")
print("route-map LOOPBACK permit 10")
print(" match ip address prefix-list LOOPBACK")
print("peer-filter LEAF-AS-RANGE")
print(" 10 match as-range 65000-65535 result accept")
print("router bgp 65000")
#Loopback0 IP  
ip = switches[hostname]['interfaces']['loopback0']['ipv4']
print(" router-id %s") % ip
print(" no bgp default ipv4-unicast")
print(" maximum-paths 3")
print(" distance bgp 20 200 200")
print("bgp listen range 10.0.0.0/8 peer-group LEAF_Overlay peer-filter LEAF-AS-RANGE")
print("neighbor LEAF_Overlay peer group")
print("neighbor LEAF_Overlay send-community")
print("neighbor LEAF_Overlay maximum-routes 0")
print("neighbor LEAF_Overlay ebgp-multihop")
print(" redistribute connected route-map LOOPBACK")
print(" address-family ipv4")
print("  neighbor LEAF_Overlay activate")
print("  redistribute connected route-map LOOPBACK)
print(" address-family evpn")
print("  bgp next-hop-unchanged")
print("  neighbor LEAF_Overlay activate")