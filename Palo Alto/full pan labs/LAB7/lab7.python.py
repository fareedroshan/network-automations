#!/usr/bin/env python

my_firewall  = [ ["LAN-FW-3","10.10.46.43","PA220"], 
                 ["LAN-FW-4","10.10.46.44","PA5220"], 
                 ["LAN-FW-5","10.10.46.45","PA220"] ]

for fw_host, fw_ip, fw_type in my_firewall:
  if fw_type == "PA220":
    url="https://"+fw_ip+"/html/?hostname="+fw_host
    print(url)


