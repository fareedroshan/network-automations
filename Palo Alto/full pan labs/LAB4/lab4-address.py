#!/usr/bin/env python
import ssl
import urllib3
import requests
import sys
import xml.etree.ElementTree as ET

if __name__ == '__main__':
  
  #---------------------------------------------------------------------------------------------------------------------------------------------------
  # Put your API_KEY , FIREWALL IP , ADDRESS OBJECT & ADDRESS IP 
  api_key      = "PUT YOUR API KEY HERE"
  firewall_ip  = "PUT YOUR FIREWALL IP KEY HERE"
  address_obj  = [ ["network_1","192.168.1.0/24"], 
                   ["network_2","192.168.2.0/24"], 
                   ["network_3","192.168.3.0/24"], 
                   ["network_4","192.168.4.0/24"], 
                   ["network_5","192.168.5.0/24"]]
  #---------------------------------------------------------------------------------------------------------------------------------------------------

try:
  
  for address_name, address_value in address_obj:
    #---------------------------------------------------------------------------------------------------------------------------------------------------
    # XPATH & ELEMENT TO CREATE ADDRESS OBJECT
    xpath             = "/config/devices/entry[@name='localhost.localdomain']/vsys/entry[@name='vsys1']/address/entry[@name='"+address_name+"']"
    element           = "<ip-netmask>"+address_value+"</ip-netmask>"
    #---------------------------------------------------------------------------------------------------------------------------------------------------
    
    api_url = "https://"+firewall_ip+"/api/?type=config&action=set&xpath="+xpath+"&element="+element+"&key="+api_key
    urllib3.disable_warnings()
    api_request       = requests.get(url=api_url,verify=False)
    api_response      = api_request.text
    xml_tree_root     = ET.fromstring(api_response)
    print(address_name + " API RESPONSE ->" + str(api_response))
except:
  print("ERROR   : Connecting to "+firewall_ip+". Check the Firewall IP address and API Key.")
  sys.exit(0)	