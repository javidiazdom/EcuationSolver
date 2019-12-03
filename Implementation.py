def BruteForce(n,coeff,rhs):
   if (rhs == 0):
      return 1
   if (n < 0 or rhs < 0):
      return 0
   res = 0
   for i in range(0,rhs+1):
      res += BruteForce(n-1,coeff,rhs-i*coeff[n])
   return res

