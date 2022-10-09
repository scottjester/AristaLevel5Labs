import yaml
from cvplibrary import CVPGlobalVariables, GlobalVariableNames
hostname = CVPGlobalVariables.getValue(GlobalVariableNames.CVP_SERIAL)
config = """
leaf1-DC1:
  interfaces:
    loopback0:
      ipv4: 10.1.0.11
    loopback1:
      ipv4: 10.1.1.11
  spine_peers:
    - 10.1.0.101
    - 10.1.0.102
    - 10.1.0.103
  leaf_peers: 10.1.0.12
  bgpasn: 65101  
leaf2-DC1:
  interfaces:
    loopback0:
      ipv4: 10.1.0.12
    loopback1:
      ipv4: 10.1.1.11
  spine_peers:
    - 10.1.0.101
    - 10.1.0.102
    - 10.1.0.103
  leaf_peers: 10.1.0.11
  bgpasn: 65101     
leaf3-DC1:
  interfaces:
    loopback0:
      ipv4: 10.1.0.13
    loopback1:
      ipv4: 10.1.1.13
  spine_peers:
    - 10.1.0.101
    - 10.1.0.102
    - 10.1.0.103
  leaf_peers: 10.1.0.14
  bgpasn: 65102  
leaf4-DC1:
  interfaces:
    loopback0:
      ipv4: 10.1.0.14
    loopback1:
      ipv4: 10.1.1.13
  spine_peers:
    - 10.1.0.101
    - 10.1.0.102
    - 10.1.0.103
  leaf_peers: 10.1.0.13
  bgpasn: 65102  
borderleaf1-DC1:
  interfaces:
    loopback0:
      ipv4: 10.1.0.21
    loopback1:
      ipv4: 10.1.1.21
  spine_peers:
    - 10.1.0.101
    - 10.1.0.102
    - 10.1.0.103
  leaf_peers: 10.1.0.22
  bgpasn: 65103  
borderleaf2-DC1:
  interfaces:
    loopback0:
      ipv4: 10.1.0.22
    loopback1:
      ipv4: 10.1.1.21
  spine_peers:
    - 10.1.0.101
    - 10.1.0.102
    - 10.1.0.103
  leaf_peers: 10.1.0.21
  bgpasn: 65103           
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
#BGP ASN
bgpasn = switches[hostname]['bgpasn']
print("router bgp %s" % bgpasn)
#Loopback0 IP  
l0ip = switches[hostname]['interfaces']['loopback0']['ipv4']
print(" router-id %s") % l0ip
print(" no bgp default ipv4-unicast")
print(" maximum-paths 3")
print(" distance bgp 20 200 200")
print(" neighbor SPINE_Overlay peer group")
print(" neighbor SPINE_Overlay remote-as 65000")
print(" neighbor SPINE_Overlay send-community")
print(" neighbor SPINE_Overlay maximum-routes 0")
print(" neighbor SPINE_Overlay ebgp-multihop")
for speer in switches[hostname]['spine_peers']:
#Iterate through all spine peers
  print("  neighbor %s peer group SPINE_Overlay" % speer)
print(" neighbor LEAF_Peer peer group")
#leaf BGP ASN
lbgpasn = switches[hostname]['bgpasn']
print(" neighbor LEAF_Peer remote-as %s" % lbgpasn)
print(" neighbor LEAF_Peer next-hop-self")
print(" neighbor LEAF_Peer maximum-routes 12000")
#leaf BGP peer
lpeer = switches[hostname]['leaf_peers']
print(" neighbor %s peer group LEAF_Peer" % lpeer)
print(" redistribute connected route-map LOOPBACK")
print(" address-family ipv4")
print("  neighbor LEAF_Peer activate")
print("  redistribute connected route-map LOOPBACK")
print(" address-family evpn")
print("  neighbor SPINE_Overlay activate")
print(" vlan-aware-bundle leaf-vlans")
#Loopback1 IP  
l1ip = switches[hostname]['interfaces']['loopback1']['ipv4']
print("  rd %s:100" % l1ip)
print("  route-target both 100:100")
print("  redistribute learned")
print("  vlan 100")
print(" vrf leaf-VRF")
#Loopback1 IP  
l1ip = switches[hostname]['interfaces']['loopback1']['ipv4']
print("  rd %s:200" % l1ip) 
print("  route-target import evpn 200:200")
print("  route-target export evpn 200:200")
print("  redistribute connected")
print("  redistribute static")