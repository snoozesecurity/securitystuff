# Prerequisite: pip install netaddr
# Create a file called ip_list.txt and define its path below.
# Put a list of IP addresses and their subnet mask in CIDR notation
# in this file and save it.  Then run this script using the following syntax:
# python print_ip.py /path/to/ip_list.txt

from netaddr import * 

with open('/path/to/ip_list.txt') as f:
     content = f.readlines()
content = [x.strip() for x in content]

for i in content:
     for ip in IPNetwork(i).iter_hosts():
          print '%s' %ip