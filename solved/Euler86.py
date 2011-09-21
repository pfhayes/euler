# Assume the room dimensions are x by y by z, with x <= y <= z
# Then, the shortest path is formed by building the right triangle
# with sides of length (x + y) and z.

# So, we want to find all triples (x, y, z) with x <= y <= z, such that
# x + y and z form a right triangle with all integer side lengths

# So, we will generate all primitive pythagorean triples, and check those

from math import sqrt

top = 1000000

count = 0
z = 2
while True :
  for x_plus_y in xrange(2, 2*z+1) :
    hyp_sq = x_plus_y * x_plus_y + z * z
    if (sqrt(hyp_sq).is_integer()) :
      # This works for all possible splits of x, y such that
      # 1 <= x <= y <= z
      # That means that, since the largest possible value for y is z,
      # then the smallest possible value for x is x_plus_y - z.
      lowest_x_val = max([1, x_plus_y - z])
      count += x_plus_y / 2 + 1 - lowest_x_val
    if count > top :
      print z
      exit(0)
  z += 1

