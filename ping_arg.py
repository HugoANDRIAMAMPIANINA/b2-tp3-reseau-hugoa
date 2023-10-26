from sys import argv
from os import system

command = f"ping {argv[1]}"

system(command)