import os
import random
from core import cli

# Made by: n0nuser
## https://github.com/n0nuser/RubberSpark

def filename(name):
  """
  Returns file name to write content in it.
  """
  if name:
    if not os.path.exists(name):
      os.makedirs(name)
    return(name + os.path.sep + name)

def banner():
  clear()
  file = os.path.curdir + os.path.sep + "core" + os.path.sep + "modules" + os.path.sep + "banner.txt"
  with open(file) as file:
    num = random.randint(91,96)
    print("\033[1;%dm" % (num) + file.read() + cli.N, end="")
  print("   by n0nuser\n")
  print("Tool to create various scripts for the Digispark!\nWrite \"\033[1mhelp\033[0m\" to list commands")

def table(list):
  """
  From list to formatted table. Returns string. 
  """
  ext = ".py"
  j = 0
  txt = " #   | Name\n"
  txt += "-----+"
  for x in range(21): txt += "-"
  txt += "\n"
  for i in list:
    if not i.endswith(ext):
      list.remove(i)
      continue
    j += 1
    i = i.split(ext)
    txt += " %-4d| %-20s\n" % (j, i[0])
  return txt

def formatDir(directory,dir):
  """
  Formats file names to have directory at the beginning.
  """
  files = []
  dirFiles = os.listdir(directory)
  dirFiles.remove('__init__.py')
  for x in dirFiles:
    files = files + ['{0}{1}{2}'.format(dir,os.path.sep,x)]
  return files

def clear():
  """
  Clears the terminal.
  """
  os.system('cls' if os.name == 'nt' else 'clear')
