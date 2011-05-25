# M(C,R) is the minimum number of cards to get through R rooms holding C cards.
# Observe M(x,y) = y + 1 for x >= y
# And, M(x,y+1) = the number of cards required to get M(x,y) cards through one
# door
# And, it takes x cards to deposit x - 2 cards past the first door

M = [[0 for x in range(31)] for x in range(41)]

for x in xrange(3,41) :
  for y in xrange(1,31) :
    if x >= y + 1 :
      M[x][y] = y + 1
    else :
      num_to_get_in_box = M[x][y-1]
      if x == 3 :
        full_loads = num_to_get_in_box - 2
        extra = 3
      elif num_to_get_in_box % (x - 2) == 1 :
        full_loads = num_to_get_in_box / (x-2)
        extra = 0
      elif num_to_get_in_box % (x - 2) == 0 :
        full_loads = num_to_get_in_box / (x-2) - 1
        extra = M[x][y-1] - full_loads * (x - 2) + 1
      else :
        full_loads = num_to_get_in_box / (x-2)
        extra = M[x][y-1] - full_loads * (x - 2) + 1
      if x == 3 and y == 3 :
        print num_to_get_in_box, full_loads, extra
      M[x][y] = full_loads * x + extra

print "M(3,1) =", M[3][1]
print "M(3,2) =", M[3][2]
print "M(3,3) =", M[3][3]
print "M(3,4) =", M[3][4]
print "M(4,6) =", M[3][6]
print "M(3,6) =", M[3][6]
print "M(4,6) =", M[3][6]
print "sum M(x,10) =", sum([M[x][10] for x in range(3,11)])
print "sum M(x,30) =", sum([M[x][30] for x in range(3,41)])

