#!/usr/bin/env python3


class MathSet(object):
  """
  MathSet is a representation of a mathematical set from naive set theory. 
  It has the same set of properties and functions as the mathematical prototype.
  
  MathSet has three main arguments:
  - name: The name of set that allow us to identify it;
  - inf: The infinity parameter, which tells whether the set is infinite or not;
  - inner: The values that MathSet contains.

  MathSet is the main data structure on the basis of which the rest of the abstractions are implemented.
  """
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
  """
  MathSubset is a representation of a mathematical subset from naive set theory.
  It is based on MathSet because have a lot of behaviour features in common.

  But MathSubset has its own special arguments:
  - parent: This field contains a reference to the set from which this subset originated.

  """
  def __init__(self, parent):
    super().__init__()
    self.parent = parent

def createSchema(new):
  """
  createSchema method is build to parse the commands and store data in schematic.
  Here is a reference of some fields that schematic constains:
  - command: Instruction that will allow us to identify which behaviour of programm user waiting;
  - name: The name of object that we operates with;
  - infinity: The infinity digit, that shows if object is infinite or not;
  - parent: The parent value shows if object have origin or no;
  - length: Length used for sorted sets for identify the length of set.
  """
  new = new.split()
  command = new[0]
  matchName = [s for s in new if "name" in s]
  matchInf = [s for s in new if "inf" in s]
  matchParent = [s for s in new if "isinstanceof" in s]

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
