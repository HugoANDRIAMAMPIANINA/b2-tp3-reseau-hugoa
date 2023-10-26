from psutil import net_if_addrs

networks = net_if_addrs()["Wi-Fi"][1][1]
print(networks)