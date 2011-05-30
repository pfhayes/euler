# Find the value of D which gives the largest minimal solution
# in x for x^2 - Dy^2 = 1, given that x and y are integers

# Use http://en.wikipedia.org/wiki/Pell%27s_equation

# Use our algorithm in Euler64.py to compute continued fractions for
# sqrt(D) and test to see if they satisfy the equation

from math import sqrt
from useful import gcd

max_x = 0
max_N = 0

for N in xrange(1, 1001) :
  root = sqrt(N)
  floor_root = int(root)
  if floor_root * floor_root == N :
    # Perfect square
    continue
  left_of_frac, frac_top, frac_bottom = floor_root, 1, floor_root
  lis = []

  print N
  while True :
    lis.append(left_of_frac)
    new_frac_bottom_before_reduce = N - frac_bottom*frac_bottom
    divisor = gcd(frac_top, new_frac_bottom_before_reduce)
    new_frac_top_int_part = new_frac_bottom_before_reduce / divisor
    assert(frac_top == divisor)
    new_frac_top_before_reduce = (sqrt(N) + frac_bottom)
    new_left_of_frac = int(new_frac_top_before_reduce / new_frac_top_int_part)
    new_frac_top = (new_frac_top_before_reduce -
      new_left_of_frac * (new_frac_top_int_part))
    new_frac_bottom = int(sqrt(N) - new_frac_top + 0.0001)
    left_of_frac, frac_top, frac_bottom = (new_left_of_frac,
      new_frac_top_int_part, new_frac_bottom)

    # Update the convergent fraction
    x, y = 1, 0
    for left_term in reversed(lis) :
      y, x = x, y
      x, y = left_term * y + 1 * x, y
    # Reduce fraction
    x /= gcd(x, y)
    y /= gcd(x, y)

    if x*x - N*y*y == 1 :
      if x >= max_x :
        max_x = x
        max_N = N
      break

print max_N, max_x
