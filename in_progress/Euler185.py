# Solve the following game of mastermind, where only the number of digits
# in the correct position is given

# Works, but is too slow

import copy
from useful import digits

d = {}
d[5616185650518293] = 2
d[3847439647293047] = 1
d[5855462940810587] = 3
d[9742855507068353] = 3
d[4296849643607543] = 3
d[3174248439465858] = 1
d[4513559094146117] = 2
d[7890971548908067] = 3
d[8157356344118483] = 1
d[2615250744386899] = 2
d[8690095851526254] = 3
d[6375711915077050] = 1
d[6913859173121360] = 1
d[6442889055042768] = 2
d[2321386104303845] = 0
d[2326509471271448] = 2
d[5251583379644322] = 2
d[1748270476758276] = 3
d[4895722652190306] = 1
d[3041631117224635] = 3
d[1841236454324589] = 3
d[2659862637316867] = 2

"""
d[90342] = 2
d[70794] = 0
d[39458] = 2
d[34109] = 1
d[51545] = 2
d[12531] = 1
"""

digits_map = {}
for key in d :
  digits_map[key] = digits(key)

seq = [set([0,1,2,3,4,5,6,7,8,9]) for x in xrange(16)]
keys = []

# Build the list of keys, with keys with fewer correct entries
# coming first
for key in d :
  if d[key] == 0 :
    digs = digits_map[key]
    for i in xrange(len(digs)) :
      seq[i].discard(digs[i])
  elif d[key] == 1 :
    keys.append(key)
for key in d :
  if d[key] == 2 :
    keys.append(key)
for key in d :
  if d[key] == 3 :
    keys.append(key)

def dfs(keys, index, seq) :
  if index == len(keys) :
    for s in seq :
      if len(s) != 1 :
        return
    # OMG! We found i!
    print  "Whoo!", seq
    exit(0)
  key = keys[index]
  num_digs = d[key]
  digs = digits_map[key]
  indexes = range(num_digs)
  while True :
    new_seq = copy.deepcopy(seq)
    j = 0
    bad = False
    for i in xrange(len(seq)) :
      if j < len(indexes) and i == indexes[j] :
        if digs[i] in new_seq[i] :
          new_seq[i] = set([digs[i]])
        else :
          bad = True
          break
        j += 1
      else :
        new_seq[i].discard(digs[i])
        if len(new_seq[i]) == 0 :
          bad = True
          break
    if not bad :
      # Do the DFS
      dfs(keys, index + 1, new_seq)
    # Move to the next indexes
    for i in xrange(len(indexes)) :
      if indexes[len(indexes) - 1 - i] != len(digs) - 1 - i :
        indexes[len(indexes) - 1 - i] += 1
        while i != 0 :
          indexes[len(indexes) - i] = indexes[len(indexes) - 1 - i] + 1
          i -= 1
        break
    else :
      # We couldn't change indexes, we reached the end
      break
    if index == 0 :
      print key, indexes

dfs(keys, 0, seq)
