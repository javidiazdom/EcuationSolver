import math

def BruteForce(n,coeff,rhs):
   rhsIni = rhs
   def BruteForceAux (n,coeff,rhs):
      if (rhs == 0):
         return 1
      if (n < 0):
         return 0
      res = 0
      for i in range(0,rhsIni+1):
         res += BruteForce(n-1,coeff,rhsIni-i*coeff[n])
      return res
   return BruteForceAux(n,coeff,rhs)
   
def Memoization(n,coeff,rhs):
   cache = {}
   def Memoization_aux(n,coeff,rhs):
      if (rhs==0):
         return 1
      if (n < 0 or rhs < 0):
            return 0
      key = str(n)+"-"+str(rhs)
      if (key not in cache):
         t = 0
         for i in range (0,rhs+1):
            t += Memoization_aux(n-1,coeff,rhs-i*coeff[n])
         cache[key] = t
      return cache[key]
   return Memoization_aux(n,coeff,rhs)

def Tabulation(n,coeff,rhs):
   table = [[]]
   def accessTable (x,y):
      if (y < 0):
         return 0
      else:
         return table[x][y]

   for i in range (0,n+2):
      table.append([])
      for j in range (0,rhs+1):
         table[i].append(0)
      table[i][0] = 1
   for k in range (1, n+2):
      for r in range (1, rhs+1):
         for i in range (0,rhs+1):
            table[k][r] += accessTable(k-1,r - i*coeff[k-1])
   return table[n+1][rhs]

def BackTracking(n,coeff,rhs):
   if (rhs == 0):
      return 1
   if (n < 0 or rhs < 0):
      return 0
   res = 0
   for i in range(0,rhs+1):
      res += BackTracking(n-1,coeff,rhs-i*coeff[n])
   return res

def BackTrackingIterator(n,coeff,rhs):
   def isValidSolution(arr):
      res = 0
      p = 0
      for i,j in zip(arr,coeff):
         res+= i*j
         if res > rhs:
            break
         p+=1
      if res == rhs:
         return 1
      if res > rhs:
         for i in range(p,n+1):
            combinations.currentComb[i]=rhs
      return 0
   nSolValidas = 0
   combinations = Combinations(rhs,n)
   for currentComb in iter(combinations):
      nSolValidas+=isValidSolution(currentComb)
   return nSolValidas

def BruteForceIterator(n,coeff,rhs):
   def isValidSolution(arr):
      res = 0
      for i,j in zip(arr,coeff):
         res+= i*j
      if res == rhs:
         return 1
      return 0
   combinations = Combinations(rhs,n)
   nSolValidas = 0
   for currentComb in iter(combinations):
      nSolValidas += isValidSolution(currentComb)
   return nSolValidas

class Combinations:
   def __init__(self,rhs,n):
      self.rhs=rhs
      self.n=n
   def __iter__(self):
      self.currentComb = [0]*(self.n+1)
      return self
   def __next__(self):
      self.currentComb[self.n] += 1
      for k in range(self.n,0,-1):
         if (self.currentComb[k] > self.rhs):
            self.currentComb[k] = 0
            self.currentComb[k-1] += 1
      if self.currentComb[0] > self.rhs:
            raise StopIteration
      return self.currentComb