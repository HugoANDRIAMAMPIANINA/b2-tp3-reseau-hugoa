from sys import argv
from os import system
import platform

command = ""

if platform.system() == "Windows":
    command = f"ping -n 1 -w 1 {argv[1]} > NUL"
elif platform.system() == "Linux":
    command = f"ping -c 1 -w 1 -q {argv[1]}"

res = system(command)

if res == 0:
    print("UP !")
else:
    print("DOWN !")