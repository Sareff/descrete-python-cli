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
  def __init__(self, name, inf, parent, inner):
    self.parent = parent
    super(MathSubset, self).__init__(name, inf, inner)


def findString(arr, name):
  """
  This method allow us to find string in array even if this string have any other characters around.
  """
  return [s for s in arr if name in s]

def generateName(pattern):
  """
  This method will generate a name for object and store this name in global name heap to avoid duplication.
  """
  global nameHeap
  global nameIndex
  name = pattern + str(nameIndex)
  nameIndex += 1
  return name


def safeCast(value, toType, default=None):
  """
  safeCast is a method to safely cast any value to any type, wether it is string to int casring or something else.
  """
  try:
    return toType(value)
  except (ValueError, TypeError):
    return default

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
  value = new[-1]

  # Searching for arguments.
  # If argument is represented in command, the value of match* will be empty list [].
  matchName = findString(new, "name") 
  matchInf = findString(new, "inf") 
  matchParent = findString(new, "isinstanceof")
  matchLength = findString(new, "length")

  #Making empty arguments to have default values.
  if len(matchName) < 1:
    match command:
      case "create-set":
        namePattern = "S"
      case "create-subset":
        namePattern = "SubS"
      case "create-pair":
        namePattern = "P"
      case "create-sortset":
        namePattern = "SS"
      case _:
        namePattern = "Obj"
    matchName = generateName(namePattern)
  else:
    matchName = matchName[0].split("=")[1]

  if len(matchInf) < 1:
    matchInf = False
  elif len(matchInf) > 1 and matchInf[0].split("=")[1] in ("1", "True", "true"):
    matchInf = True
  else:
    matchInf = False

  if len(matchParent) < 1:
    matchParent = ""
  else:
    matchParent = matchParent[0].split("=")[1]

  if len(matchLength) < 1:
    matchLength = ""
  else:
    matchLength = safeCast(matchLength[0].split("=")[1], int, "") 
  
  schematic =  {"command": command, 
                "name": matchName,
                "infinity": matchInf, 
                "parent": matchParent,
                "length": matchLength,
                "value": value}
  return schematic

def showManual(command):
  match command:
    case "create-set":
      return "Create-set command as it follows from name - creates the set.\nYou can specify certain set's options such as:\n-name=<name>\n-inf=<1, 0>\n"
    case "create-subset":
      return "Create-subset command creates the subset of certain set, that you must specify with \"-isinstanceof\" argument. Here is other options that you can specify in Subset creation:\n-name=<name>\n-inf=<1, 0>\n-isinstanceof=<Name of Parent-Set>\n"
    case "create-sortset":
      return "Create-sortset command creates the sorted set of objects with constant length that you must specify with \"-length\" argument. Other optional arguments that you can use:\n-name=<name>\n-length=<length of your sorted set>"
    case "create-pair":
      return "Create-pair command create the pair of two objects that sorted in order that you specified on creation. Optional arguments:\n-name=<name>"

def readCommand(new):
  global ObjList

  cmd = new.split()
  if cmd[0] == cmd[-1]:
    match cmd[0]:
      case "help":
        return """CLI usage page:\n1. Object creation\n- create-set: Creates a set with value that has to be in curly brackets;
- create-subset: Creates a subset of existing set that you must point to with argument "-isinstanceof";
- create-sortset: Creates a sorted set that must to have "-length" argument;
- create-pair: Creates a simple pair with fixed value positions.
2. Object interaction
- I haven't implemented it yet :P"""

      case _:
        return "No such command, please visit \"help\" page."

  if cmd[0] == "help":
    return showManual(cmd[1])

  schematics = createSchema(new)
  name = schematics["name"]

  match schematics["command"]:
    case "create-set":
      ObjList[name] = MathSet(name, schematics["infinity"], schematics["value"])
      return (ObjList, schematics) 
    case "create-subset":
      ObjList[name] = MathSubset(name, schematics["infinity"], schematics["parent"], schematics["value"])
      return (ObjList, schematics)
    case "create-sortset":
      pass
    case _:
      return "No such command"

if __name__ == "__main__":

  ObjList = dict()
  nameHeap = []
  nameIndex = 0
  acceptedCommands = ("create-set", "create-subset", "create-pair", "create-sortset")
  while (b := input("[CMD] ")) != "exit":
    print(readCommand(b))
