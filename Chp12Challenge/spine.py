import yaml
config = """
DC1:
  spines:
    Spine1-DC1:
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
print(switches['DC1']['spines']['Spine1-DC1']['interfaces']['loopback0']['ipv4'])