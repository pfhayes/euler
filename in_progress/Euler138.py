# We want to find all isoceles triangles with integral side lengths
# where the height is equal to the base +/- 1

# Generate all primitive pythagorean triples using the formula
# x = m^2 - n^2, y = 2mn, z = m^2 + n^2

# We also make the observation that, whenever we obtain a solution
# from (m,n) = (a,b), then the next solution will have n = a. Furthermore,
# we observe that m must be at least 4*n, so as soon as we find the first
# solution, we can generate the next value of n, and a lower bound for m,
# and proceed to check solutions from there

from math import sqrt
from useful import gcd

count = 0
total = 0
m = 1
n = 1
while True :
  x = m*m - n*n
  y = 2*m*n
  z = m*m + n*n

  if ((2 * y == x + 1) or
      (2 * y == x - 1)) :
    print (x,y,z), (m, n)
    total += z
    count += 1
    n = m
    m *= 4

  if count == 12 :
    print total
    break
  m += 1
