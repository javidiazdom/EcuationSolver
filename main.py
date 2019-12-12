import sys
import re
import Implementation as imp
import time

def missing():
   print("Missing desired algorythm")

algorythm = 0
algorythms = [False,False,False,False,False,False]
di, do, dt = (False,)*3
coeffs = []
rhss = []

def switch(i):
   switcher={
      "-h":showHelp,
      "-di":displayInput,
      "-do":displayOutput,
      "-dt":displayTime,
      "-f":getFromFile,
      "-ec":inlineEcuation,
      "-o":selectAlgorythm
   }
   func=switcher.get(i,default)
   func()

def default():
   print("Invoke error: bad parameter \n Type Main.py -h for help")
   exit(-1)

def selectAlgorythm():
   sys.argv.pop(0)
   global algorythm
   options = sys.argv.pop(0)
   algorythm = 1
   for j in range(0,6):
      if (re.search(str(j),options)):
         algorythms[j] = True
      


def showHelp():
   file = open("./Help.txt","r")
   print(file.read())
   exit(0)

def displayInput():
   global di
   di = True
   sys.argv.pop(0)

def displayOutput():
   global do
   do = True
   sys.argv.pop(0)

def displayTime():
    global dt
    dt = True
    sys.argv.pop(0)

def getFromFile():
   sys.argv.pop(0)
   file = sys.argv.pop(0)
   f = open(file,'r')
   global rhss
   global coeffs
   for line in f:
      t = line.split('=')
      rhss.append(int(t[1]))
      coefst = []
      for letter in t[0].split(','):
         coefst.append(int(letter))
      coeffs.append(coefst)

def inlineEcuation():
   sys.argv.pop(0)
   ecuation = sys.argv.pop(0)
   if (re.search("([1-9]+[a-z]?[+-])*[1-9]+[a-z]+=[1-9]+",ecuation)):
      matches = re.findall("[1-9]*[a-z]",ecuation)
      coefftemp = []
      for match in matches:
         coefftemp.append(int(re.findall("[0-9]+", match)[0]))
      global coeffs
      coeffs.append(coefftemp)
      global rhss
      rhss.append(int(re.findall("[1-9]+",re.findall("=[1-9]+",ecuation)[0])[0]))
   else:
      print("Bad parameter: The ecuation has not a valid format")
      exit(-1)


sys.argv.pop(0)
while len(sys.argv)> 0:
    switch(sys.argv[0])


if (di):
   for i,j in zip(coeffs,rhss):
      print(i,"=",j)
   print("\n------\n")

if algorythm == 0 or algorythms[0]:
   for coef,rhs in zip(coeffs,rhss):
      start=time.time()
      res = imp.BruteForce(len(coef)-1,coef,rhs)
      tiempo=time.time() - start
      print(coef,"=",rhs,"Tiempo de ejecución para Brute Force:",tiempo,"segundos")
      print("------")
      if (do):
         print("Numero de soluciones:",res)
   print("\n")

if algorythm == 0 or algorythms[1]:
   for coef,rhs in zip(coeffs,rhss):
      start=time.time()
      res = imp.BruteForceIterator(len(coef)-1,coef,rhs)
      tiempo=time.time() - start
      print(coef,"=",rhs,"Tiempo de ejecución para Brute Force Iterativo:",tiempo,"segundos")
      print("------")
      if (do):
         print("Numero de soluciones:",res)
   print("\n")

if algorythm == 0 or algorythms[2]:
   for coef,rhs in zip(coeffs,rhss):
      start=time.time()
      res = imp.Memoization(len(coef)-1,coef,rhs)
      tiempo=time.time() - start
      print(coef,"=",rhs,"Tiempo de ejecución para Memoization:",tiempo,"segundos")
      print("------")
      if (do):
         print("Numero de soluciones:",res)
   print("\n")

if algorythm == 0 or algorythms[3]:
   for coef,rhs in zip(coeffs,rhss):
      start=time.time()
      res = imp.Tabulation(len(coef)-1,coef,rhs)
      tiempo=time.time() - start
      print(coef,"=",rhs,"Tiempo de ejecución para Tabulation:",tiempo,"segundos")
      print("------")
      if (do):
         print("Numero de soluciones:",res)
   print("\n")

if algorythm == 0 or algorythms[4]:
   for coef,rhs in zip(coeffs,rhss):
      start=time.time()
      res = imp.BackTracking(len(coef)-1,coef,rhs)
      tiempo=time.time() - start
      print(coef,"=",rhs,"Tiempo de ejecución para Backtracking:",tiempo,"segundos")
      print("------")
      if (do):
         print("Numero de soluciones:",res)
   print("\n")

if algorythm == 0 or algorythms[5]:
   for coef,rhs in zip(coeffs,rhss):
      start=time.time()
      res = imp.BackTrackingIterator(len(coef)-1,coef,rhs)
      tiempo=time.time() - start
      print(coef,"=",rhs,"Tiempo de ejecución para Backtracking iterativo:",tiempo,"segundos")
      print("------")
      if (do):
         print("Numero de soluciones:",res)


