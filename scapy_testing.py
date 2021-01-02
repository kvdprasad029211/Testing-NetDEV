import scapy.all as scapy
import sys
import ipaddress

# for i in ipaddress.IPv4Network('8.8.8.0/24'):
for ip in range(256):	
	host = "192.168.43.%d" % (ip)
	# print (host)
	# scapy.sr(scapy.IP(src="192.168.43.181", dst=host/scapy.ICMP())
	scapy.sr(scapy.srloop(scapy.IP(dst="192.168.43.1")/scapy.TCP()))
	scapy.send(sr)