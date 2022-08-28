import yaml
config = """
Leaf1-DC1:
  interfaces:
    loopback0:
      ipv4: 192.168.101.11
      mask: 32
    loopback1:
      ipv4: 192.168.102.11
      mask: 32          
    Ethernet3:
      ipv4: 192.168.103.0
      mask: 31
    Ethernet4:
      ipv4: 192.168.103.2
      mask: 31
    Ethernet5:
      ipv4: 192.168.103.4
      mask: 31   
  bgp:
    asn: 65101
    spine_peers:
      - 192.168.103.1
      - 192.168.103.3
      - 192.168.103.5
"""

switches = yaml.safe_load(config)


print("ip prefix-list LOOPBACK")
#prefix-list loop
pl = ['192.168.101.0/24', '192.168.102.0/24', '192.168.201.0/24', '192.168.202.0/24']
for ip in pl:
    print(" permit %s" % ip)
print('route-map LOOPBACK permit 10')
print(' match ip address prefix-list LOOPBACK')
#BGP ASN
bgpasn = switches['Leaf1-DC1']['bgp']['asn']
print("router bgp %s" % bgpasn)
#Loopback0 IP  
ip = switches['Leaf1-DC1']['interfaces']['loopback0']['ipv4']
print(" router-id %s" % ip )
print(' no bgp default ipv4-unicast')
print(' maximum-paths 3')
print(' distance bgp 20 200 200')
print(' neighbor SPINE_Underlay peer group')
print(' neighbor SPINE_Underlay remote-as 65100')
print(' neighbor SPINE_Underlay send-community')
print(' neighbor SPINE_Underlay maximum-routes 12000')
print(' neighbor LEAF_Peer peer group')
print(' neighbor LEAF_Peer remote-as 65101')
print(' neighbor LEAF_Peer next-hop-self')
print(' neighbor LEAF_Peer maximum-routes 12000')
print(' neighbor 192.168.101.102 peer-group SPINE_Underlay')
print(' neighbor 192.168.101.103 peer-group SPINE_Underlay')
print(' address-family ipv4')
print('  neighbor 192.168.101.11 peer-group LEAF_Peer')
print('  neighbor 192.168.101.12 peer-group LEAF_Peer')
print('  neighbor 192.168.101.13 peer-group LEAF_Peer')
print('  neighbor 192.168.101.14 peer-group LEAF_Peer')
print('  redistribute connected route-map LOOPBACK')