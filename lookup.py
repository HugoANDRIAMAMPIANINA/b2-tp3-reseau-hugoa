from socket import gethostbyname
from sys import argv

ipaddr = gethostbyname(argv[1])

print(ipaddr)