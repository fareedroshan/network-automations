#!/usr/bin/env python
import ssl
import urllib3
import requests
import sys
import xml.etree.ElementTree as ET

if __name__ == "__main__":
  
  #---------------------------------------------------------------------------------------------------------------------------------------------------
  # Put your API_KEY , FIREWALL IP , XML COMMAND and the XML ELEMENT  
  api_key         = "PUT YOUR API KEY HERE"
  xml_command     = "<show><system><info/></system></show>"
  xml_elements    = ["model" , "hostname", "sw-version"]
  fw_ip_address   = [ "PUT FIREWALL 1 IP HERE" , "PUT FIREWALL 2 IP HERE" , "PUT FIREWALL 3 IP HERE" , "PUT FIREWALL 4 IP HERE" ]
  #---------------------------------------------------------------------------------------------------------------------------------------------------

try:

  for ip in fw_ip_address:

    api_url           = "https://"+ip+"/api/?type=op&cmd="+xml_command+"&key="+api_key
    urllib3.disable_warnings()
    api_request       = requests.get(url=api_url,verify=False)
    api_response      = api_request.text
    xml_tree_root     = ET.fromstring(api_response)

    print("---------------------")
    print("Firewall: "+ip)
    print("---------------------")

    for tag in xml_elements:
      for leaf in xml_tree_root.iter(tag):
        if leaf.tag == tag:
          print(tag+" : "+leaf.text)

except:
  print("ERROR   : Connection Error. Check the Firewall IP Address List and API Key.")
  sys.exit(0)	
