no spanning-tree vlan-id 4094
!
vlan 4094
   name MLAG
   trunk group mlagpeer
!
interface Ethernet1
   channel-group 10 mode active
!
interface Ethernet2
   channel-group 10 mode active
!
interface Port-Channel10
   switchport mode trunk
   switchport trunk group mlagpeer
!
interface Vlan4094
   ip address 192.168.255.1/30
   no autostate
!
mlag configuration
   domain-id MLAG-DOMAIN
   local-interface Vlan4094
   peer-address 192.168.255.2
   peer-link Port-Channel10