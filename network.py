from socket import gethostbyname
from sys import argv
from os import system
from psutil import net_if_addrs
import platform

def lookup(domain_name):
    return gethostbyname(domain_name)

def ping(ipaddr):
    command = ""

    if platform.system() == "Windows":
        command = f"ping -n 1 -w 3 {ipaddr} > NUL"
    elif platform.system() == "Linux":
        command = f"ping -c 1 -w 3 -q {ipaddr} > /dev/null"
        
    res = system(command)

    if res == 0:
        return "UP !"
    
    return "DOWN !"

def ip():
    if platform.system() == "Windows":
        return net_if_addrs()["Wi-Fi"][1][1]
    elif platform.system() == "Linux":
        wifi_network_adapter = ""
        try:
            return net_if_addrs()["enp0s3"][0][1]
        except:
            return net_if_addrs()["wlan0"][0][1]
    

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