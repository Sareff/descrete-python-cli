#!/usr/bin/env python3


class Set(object):
  inf = False
  name = ""
  inner = ""

  def __init__(self, name, inf, inner):
    self.name = name
    self.inf = inf
    self.inner = inner

  def __repr__(self):
    return str(self.inner) + " " + str(self.inf)

class Subset(Set):
  
  def __init__(self, parent):
    super().__init__()
    self.parent = parent


def readCommand(new):
  global ObjList
  new = new.split()
  command = new[0]

  if command in acceptedCommands:
    obj = new[-1]
    params = new[1:-1]
    name = params[0].split("=")[1]
    inf = params[1].split("=")[1]
    inf = True if inf == "true" else False
    ObjList[name] = Set(name, inf, obj)
  else:
    return "No such command"

  return ObjList
    

if __name__ == "__main__":

  ObjList = dict()
  acceptedCommands = ("/create-set", "/create-subset", "/create-pair", "/create-sortset")
  while (b := input("[CMD] ")) != "/exit":
    print(readCommand(b))
