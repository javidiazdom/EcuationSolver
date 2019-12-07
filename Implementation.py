import math
import itertools

def BruteForce(n,coeff,rhs):
   4

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

def BruteForceIterator(n,coeff,rhs):
   def product(array, n):
    # product('ABCD', 'xy') --> Ax Ay Bx By Cx Cy Dx Dy
    # product(range(2), repeat=3) --> 000 001 010 011 100 101 110 111
    pools = [tuple(array)] * n
    result = [[]]
    for pool in pools:
        result = [x+[y] for x in result for y in pool]
    for prod in result:
        yield tuple(prod)

   validCombinations = 0
   table = []
   for i in range(0,rhs+1):
      table.append(i)
   for i in product(table,n+1):
      res = 0
      for k,j in zip(coeff,i):
         res += k*j
      if res == rhs:
         validCombinations+=1
   return validCombinations

def BackTracking(n,coeff,rhs):
   
   return res

def BackTrackingIterator(n,coeff,rhs):
   return 0
