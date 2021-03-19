#!/usr/bin/python3

# Made by: n0nuser
## https://github.com/n0nuser/RubberSpark

import sys
from core import tools, cli
from core.duckFiles import *

def outputDir():
    output = input("\nFolder to save the script: ")
    while not(output): 
        output = input("\nCan't Leave it in blank!.\nFolder to save the script: ")
    return output

def main():
  # Validate Python3
  PY3 = sys.version_info[0] == 3
  if (PY3 is False):
    print("Usage: python3 duckyScripts.py")
    exit()

  cli.menu()

while True:
  main()