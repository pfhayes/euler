# Find the number of ways to split n councs into any number of piles

# Define M(n, k) to be the number of ways to split n coins into 
# piles of no more than k coins.

d = {}
d[(1,1)] = 1

def M(n, k) :
  if not (n,k) in d :
    if n <= 1 :
      return 1
    if k == 1 :
      return 1
    total = 0
    for i in xrange(1, k+1) :
      if i > n :
        break
      total += M(n-i, i)
    d[(n,k)] = total
  return d[(n,k)]

print M(1,1)
print M(3,3)
print M(5,5)
print M(7,7)
print M(9,9)

i = 1
while True :
  if M(i,i) % 1000000 == 0 :
    print M(i,i)
    exit(0)
