import math

def f(x) :
  return math.floor(2**(30.403243784-x*x)) * 10**-9

u = -1
for i in range(1,2000) :
  print u + f(u)
  u = f(u)
