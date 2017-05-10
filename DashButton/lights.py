from scapy.all import *
from lifxlan import *

#Buttons
andrex = 'xx:xx:xx:xx:xx:xx'

#Lights
bedroom = Light('xx:xx:xx:xx:xx:xx', '192.168.1.xxx')
second_arp = False

def arp_detect(pkt):
 if pkt[ARP].op == 1: #network request
 if pkt[ARP].hwsrc == andrex:
 current_state = bedroom.get_power()
 if current_state == 0:
 bedroom.set_power("on")
 else:
 bedroom.set_power("off")

if second_arp == False:
 sniff(prn=arp_detect, filter="arp", store=0)
 second_arp = True
else:
 second_arp = False