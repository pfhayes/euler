# Nim!

n = 1
count = 0
while n <= 2**30 :
  if (n ^ (2*n) ^ (3*n)) == 0 :
    count += 1
  n += 1
print count
