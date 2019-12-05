def BruteForce(n,coeff,rhs):
   if (rhs == 0):
      return 1
   if (n < 0 or rhs < 0):
      return 0
   res = 0
   for i in range(0,rhs+1):
      res += BruteForce(n-1,coeff,rhs-i*coeff[n])
   return res

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

   for i in range (0,n+1):
      table.append([])
      for j in range (0,rhs+1):
         table[i].append(0)
      table[i][0] = 1
   
   for k in range (1, n+1):
      for r in range (1, rhs+1):
         for i in range (0,rhs+1):
            table[k][r] += accessTable(k-1,r - i*coeff[k])
   print(table)
   return table[n][rhs]
