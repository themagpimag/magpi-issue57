from scapy.all import *

def arp_detect(pkt):
 if pkt[ARP].op == 1: #network request
 if pkt[ARP].hwsrc == 'xx:xx:xx:xx:xx:xx'
 return "Button detected!"

print sniff(prn=arp_display, filter="arp", store=0)