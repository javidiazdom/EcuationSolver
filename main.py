import sys
import re
import Implementation as imp

def inlineEcuation():
    if (len(sys.argv) > 2):
        print("Error: Too many parameters. Needed: 1")
        exit(1)

    if (re.search("([1-9]+[a-z]?[+-])*[1-9]+[a-z]+=[1-9]+",sys.argv[1])):
        matches = re.findall("[1-9]*[a-z]",sys.argv[1])
        coeff = []
        for match in matches:
            coeff.append(int(re.findall("[0-9]+", match)[0]))
        rhs=int(re.findall("[1-9]+",re.findall("=[1-9]+",sys.argv[1])[0])[0])
        return coeff,rhs

    else:
        print("Bad parameter: The ecuation has not a valid format")
        return None

def switch(i):
   switcher={
      "-h":showHelp,
      "-di":displayInput,
      "-do":displayOutput,
      "-dt":displaySeconds,
      "-f":getFromFile
   }
   func=switcher.get(i,default)
return func()

def default():
   print("Invoke error: bad parameter \n Type Main.py -h for help")
   exit(-1)

def showHelp():
   file = open("./Help.txt","r")
   print(file.read())
   exit()

def displayInput():
   global di
   di = True
   sys.argv.pop(0)

def displayOutput():
   global do
   do = True
   sys.argv.pop(0)

def getFromFile():
    