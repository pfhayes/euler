# Find the maximum sum that can be made from choosing one element from each
# row and column in the matrix

import random
mat = map(lambda x : map(int, x.split()), open('Euler345.txt').readlines())

# Run simulated annealing. Start with a bad solution and Make swaps until we get
# the optimal answer
# This method does not guarantee an optimal solution, but run it a few times and
# use the best solution seen
soln = [(i, i) for i in xrange(len(mat))]
best = sum(map(lambda x : mat[x[0]][x[1]], soln))

while True :
  i1 = random.randint(0, len(soln) - 1)
  x1, y1 = soln[i1]
  i2 = random.randint(0, len(soln) - 1)
  x2, y2 = soln[i2]

  if mat[x2][y1] + mat[x1][y2] > mat[x1][y1] + mat[x2][y2] :
    soln[i1] = (x1, y2)
    soln[i2] = (x2, y1)
    best = sum(map(lambda x : mat[x[0]][x[1]], soln))
    print best
