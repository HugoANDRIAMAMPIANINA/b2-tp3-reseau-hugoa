from socket import gethostbyname
from sys import argv
from os import system
from psutil import net_if_addrs
import platform
import re

def lookup(domain_name: str) -> str:
    try:
        return gethostbyname(domain_name)
    except:
        return f"{domain_name} isn't a valid domain name"

def ping(ipaddr: str) -> str:
    command = ""

    if platform.system() == "Windows":
        command = f"ping -n 1 -w 3 {ipaddr} > NUL"
    elif platform.system() == "Linux":
        command = f"ping -c 1 -w 3 -q {ipaddr} > /dev/null"
        
    res = system(command)

    if res == 0:
        return "UP !"
    
    return "DOWN !"

def ip() -> str:
    if platform.system() == "Windows":
        for sniaddr in net_if_addrs()["Wi-Fi"]:
            ipaddr = re.search(r"^((25[0-5]|(2[0-4]|1\d|[1-9]|)\d)(\.(?!$)|$)){4}$",sniaddr[1])
            if ipaddr != None:
                return sniaddr[1]
    elif platform.system() == "Linux":
        i = 0
        for key, value in net_if_addrs().items():
            if i == 1:
                for sniaddr in value:
                    ipaddr = re.search(r"^((25[0-5]|(2[0-4]|1\d|[1-9]|)\d)(\.(?!$)|$)){4}$",sniaddr[1])
                    if ipaddr != None:
                        return sniaddr[1]
            i+=1

output = ""

if len(argv) > 2:
    try:
        output = globals()[argv[1]](argv[2])
    except:
        output = f"'{argv[1]}' is not an available command. Déso."
else:
    try:
        output = globals()[argv[1]]()
    except:
        output = f"'{argv[1]}' is not an available command. Déso."
    
print(output)