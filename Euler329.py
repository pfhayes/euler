# The prime frog

from useful import PrimeList, gcd

def fracreduce((p1, q1)) :
  d = gcd(p1,q1)
  return (p1/d, q1/d)

def add((p1,q1), (p2,q2)) :
  return fracreduce((p1*q2 + q1*p2, q1*q2))

def mult((p1,q1), (p2,q2)) :
  return fracreduce((p1*p2,q1*q2))

numspots = 500
seqlen = 15

spots = [(1,numspots)] * numspots

primes = set(PrimeList(numspots+10))

pprobs = []
nprobs = []

for x in xrange(seqlen) :
  pprob = (0,1)
  nprob = (0,1)
  for i in xrange(len(spots)) :
    if i + 1 in primes :
      pprob = add(pprob, mult((2,3),spots[i]))
      nprob = add(nprob, mult((1,3),spots[i]))
    else :
      pprob = add(pprob, mult((1,3),spots[i]))
      nprob = add(nprob, mult((2,3),spots[i]))
  pprobs.append(pprob)
  nprobs.append(nprob)
  
  newspots = [(0,1)] * numspots
  newspots[0] = mult((1,2), spots[1])
  newspots[1] = add(spots[0], mult((1,2),spots[2]))
  newspots[numspots - 1] = mult((1,2), spots[numspots-2])
  newspots[numspots - 2] = add(spots[numspots - 1], mult((1,2),spots[numspots - 3]))

  for i in xrange(2, len(spots)-2) :
    newspots[i] = add(mult((1,2), spots[i-1]), mult((1,2),spots[i+1]))
  spots = newspots

ret = (1,1)
s = "PPPPNNPPPNPPNPN"[0:seqlen]
print s
for i in xrange(len(s)) :
  char = s[i]
  if char == "P" :
    ret = mult(ret, pprobs[i])
  else :
    ret = mult(ret, nprobs[i])

print pprobs
print nprobs
print float(ret[0]) / ret[1]
print fracreduce(ret)

