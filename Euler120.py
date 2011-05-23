# Find the maximum remainder when (a-1)^n + (a+1)^n is divided by a^2

# Use binomial theorem to see that (a-1)^n + (a+1)^n
# is equal to n*a*(-1)^(n-1) + (-1)^n + n*a + 1 (mod a^2)
# which is equal to
#   2, if n is even
#   2 * n * a, if n is odd
# So, for each a, find the odd n that maximizes 2 * n * a mod a^2
# Which is the largest odd n such 

from useful import multMod

s = 0
for a in range(3,1001) :
  if a % 2 == 0 :
    n = a/2 - 1
  else :
    n = a/2
  rmax = 2 * n * a
  s += rmax

print s
