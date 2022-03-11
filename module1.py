#!/usr/bin/env python3

class MathSet(object):
  inf = False
  name = ""
  inner = ""

  def __init__(self, name, inf, inner):
    self.name = name
    self.inf = inf
    self.inner = inner

  def __repr__(self):
    return str(self.inner) + " " + str(self.inf)

class MathSubset(MathSet):
  
  def __init__(self, parent):
    super().__init__()
    self.parent = parent

def createSchema(new):
  new = new.split()
  command = new[0]
  matchName = [s for s in new if "name" in s]
  matchInf = [s for s in new if "inf" in s]
  value = new[-1]
  
  return {"command": command, "name": matchName[0].split("=")[1] if len(matchName) > 0 else "S1",
          "infinity": matchInf[0].split("=")[1] if (len(matchInf) > 0) else "0", "value": value}

def readCommand(new):
  global ObjList

  cmd = new.split()
  if cmd[0] == cmd[-1]:
    return "Command should use arguments"

  schematics = createSchema(new)

  match schematics["command"]:
    case "create-set":
      name = schematics["name"]
      ObjList[name] = MathSet(name, schematics["infinity"], schematics["value"])
      return ObjList 
    case "create-subset":
      name = schematics["name"]
      ObjList[name] = MathSubset(name, schematics["infinity"], schematics["value"])
      return ObjList 
    case _:
      return "No such command"

'''
  if command in acceptedCommands:

    obj = new[-1]
    params = new[1:-1]
    name = params[0].split("=")[1]
    inf = params[1].split("=")[1]
    inf = True if inf == "true" else False
    ObjList[name] = MathSet(name, inf, obj)
  else:
    return "No such command"
'''
#  return ObjList
    

if __name__ == "__main__":

  ObjList = dict()
  acceptedCommands = ("create-set", "create-subset", "create-pair", "create-sortset")
  while (b := input("[CMD] ")) != "exit":
    print(readCommand(b))
