total = 4

all = {}
two = {}
one = {}
none = {}

all[3] = 4
two[3] = 194
one[3] = 1445
none[3] = 2197

for i in range(4,17) :
  all[i] = 16 * all[i-1] + two[i-1]
  print "all",i,all[i]
  total += all[i]
  two[i] = 15 * two[i-1] + 2 * one[i-1]
  one[i] = 14 * one[i-1] + 3 * none[i-1]
  none[i] = 13 * none[i-1]

print "total", hex(total)
