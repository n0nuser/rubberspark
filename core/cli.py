import os
import time
import importlib
from core import tools

# Made by: n0nuser
## https://github.com/n0nuser/rubberspark

G = "\033[1;92m"
R = "\033[1;91m"
B = "\033[1;96m"
BOLD = "\033[1m"
N = "\033[0m"

def listItems(dir):
  baseDir = "core" + os.path.sep + "modules"
  if dir != "":
    directory = os.path.curdir + os.path.sep + baseDir + os.path.sep + dir
    return tools.table(tools.formatDir(directory,dir))
  else:
    dir = [ 'linux', 'windows' ]
    files = []
    for dir in dir:
      directory = os.path.curdir + os.path.sep + baseDir + os.path.sep + dir
      files = files + tools.formatDir(directory,dir)
    return tools.table(files)

def getModule(module):
  name = module.split(os.path.sep)
  #filename = os.path.curdir + os.path.sep + "core" + os.path.sep + "modules" + os.path.sep + name[0] + os.path.sep + name[1] + ".py"
  try:
    modulename = "core.modules." + name[0] + "." + name[1]
  except IndexError:
    return -1
  try:
    module = importlib.import_module(modulename)
    importlib.reload(module)
    info = getattr(module, "info")
    return info
  except ModuleNotFoundError:
    return -1

def use(module):
  info = getModule(module)
  try:
    moduleName = module.split(os.path.sep)[1]
  except IndexError:
    return format("\033[1;91mTry with the other backslash.\033[0m")
  if (info == -1):
    return format("\033[1;91mCouldn't found module.\033[0m")
  else:
    if not info.parameters:
      with open(moduleName + ".duck", mode="w") as f:
        f.write(info.content)
      f.close()
      return format("Content of %s written to \"%s.duck\"\nYou can now use it in RubberDucky or compile it for DigiSpark (`resources` folder)" % (moduleName, moduleName))
    else:
      print("These parameters are required:")
      for i in info.parameters:
        replace = str(input(str(i) + ": "))
        info.content = info.content.replace(i, replace)
      with open(moduleName + ".duck", mode="w") as f:
        f.write(info.content)
      f.close()
      return format("Content of %s written to \"%s.duck\"\nYou can now use it in RubberDucky or compile it for DigiSpark (`resources` folder)" % (moduleName, moduleName))

def code(module):
  info = getModule(module)
  if (info == -1):
    return format("\033[1;91mCouldn't found module.\033[0m")
  else:
    return format("\033[1mPayload:\033[0m %s\n\033[1mParameters:\033[0m %s\n\033[1mCode:\033[0m\n%s" % (name[1], str(info.parameters), info.content))
     

def show(module):
  info = getModule(module)
  if (info == -1):
    return format("\033[1;91mCouldn't found module.\033[0m")
  else:
    full_text = format("\033[1mPayload:\033[0m %s\n\033[1mAuthor:\033[0m %s\n\033[1mFunction:\033[0m %s\n\033[1mParameters:\033[0m %s" % (name[1], info.author, info.function, str(info.parameters)))
    return full_text

def help():
  help = '''\
Command           Description
-------           -----------
help              Shows this help menu.
list              Shows list of payloads, can be used with arguments. i.E.: list linux
clear             Clears the screen
banner            Display banner.
exit              Exit the framework\
'''
  print(help)

def menu():
  tools.banner()
  while True: 
    selection = str(input(BOLD + "RubberSpark" + N + " > "))
    selection = selection.split(" ")

    if selection[0].lower() == 'list':
      try:
        if selection[1].lower() == 'linux':
          print(listItems("linux"))
        elif selection[1].lower() == 'windows':
          print(listItems("windows"))
      except IndexError:
        print(listItems(""))
    elif selection[0].lower() == 'show':
      print(show(selection[1]))
    elif selection[0].lower() == 'use':
      print(use(selection[1]))
    elif selection[0].lower() == 'code':
      print(code(selection[1]))
    elif selection[0].lower() == 'clear':
      tools.clear()
    elif selection[0].lower() == 'help':
      help()
    elif selection[0].lower() == 'banner':
      tools.banner()  
    elif selection[0].lower() == 'exit': 
      exit()
    else: 
      print(R + " Unknown Option Selected!" + N)
      time.sleep(2)