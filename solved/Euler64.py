# http://projecteuler.net/index.php?section=problems&id=64
# Find the number of values of N <= 10000 for which sqrt(N) has an odd period.

# The algorithm is given on the problem page, this is just numeric manipulation

from math import sqrt
from useful import gcd

count = 0
for N in xrange(1, 10001) :
  root = sqrt(N)
  floor_root = int(root)
  if floor_root * floor_root == N :
    # Perfect square
    continue
  left_of_frac, frac_top, frac_bottom = floor_root, 1, floor_root

  se = set([])
  while True :
    new_frac_bottom_before_reduce = N - frac_bottom*frac_bottom
    divisor = gcd(frac_top, new_frac_bottom_before_reduce)
    new_frac_top_int_part = new_frac_bottom_before_reduce / divisor
    assert(frac_top == divisor)
    new_frac_top_before_reduce = (sqrt(N) + frac_bottom)
    new_left_of_frac = int(new_frac_top_before_reduce / new_frac_top_int_part)
    new_frac_top = new_frac_top_before_reduce - new_left_of_frac * (new_frac_top_int_part)
    new_frac_bottom = int(sqrt(N) - new_frac_top + 0.0001)
    result_tuple = (new_left_of_frac, new_frac_top_int_part, new_frac_bottom)
    if (result_tuple in se) :
      break
    se.add(result_tuple)
    left_of_frac, frac_top, frac_bottom = result_tuple
  if len(se) % 2 == 1 :
    count += 1

print count

