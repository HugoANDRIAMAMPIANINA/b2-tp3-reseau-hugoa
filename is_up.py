from sys import argv
from os import system
import platform

command = ""

if platform.system() == "Windows":
    command = f"ping -n 1 -w 3 {argv[1]} > NUL"
elif platform.system() == "Linux":
    command = f"ping -c 1 -w 3 -q {argv[1]} > /dev/null"

res = system(command)

if res == 0:
    print("UP !")
else:
    print("DOWN !")