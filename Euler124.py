from useful import primeFactorize

dict = {}

for x in xrange(2,100001) :
  facts = primeFactorize(x)
  rad = frozenset(facts)
  if rad in dict :
    dict[rad].append(x)
  else :
    dict[rad] = [x]

tosort = []

for key in dict.keys() :
  prod = 1
  for fact in key :
    prod *= fact
  tosort.append((prod, key))

tosort.sort()

lower = 0
target = 10000

for (prod, rad) in tosort :
  if (lower + len(dict[rad]) < target) :
    lower += len(dict[rad])
    continue
  lis = dict[rad]
  lis.sort()
  goal = target - lower
  print rad
  print lis
  print lis[goal - 2:goal + 2]
# answer is off by 2 for whatever reason. answer is lis[goal - 2]
  break
