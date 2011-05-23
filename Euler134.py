from useful import PrimeList, gcd, digits

primes = PrimeList(1000000+1000)
primes = primes[2:] # No 2, 3

# for p1, p2 consecutive primes, find the smallest n such
# that the last digits of n are p1, and n is divisible by
# p2

# Solve the linear diophantine equation
# -10**(z) * x + p2 * y = p1
# where z is the number of digits in p1
# Apply extended euclidean algorithm

answer = 0

def get_sol(a,b,c) :
  (x, y) = extended_gcd(a,b)
  return (x*c, y*c)

def extended_gcd(a,b) :
  if b == 0 :
    return (1,0)
  q = a / b
  r = a % b
  (s, t) = extended_gcd(b, r)
  return (t, s - q*t)

for i in xrange(len(primes)) :
  p1 = primes[i]
  p2 = primes[i+1]
  if p1 > 1000000 :
    break
  digs = len(digits(p1))
  a = -(10**digs)
  b = p2
  c = p1
  (solx, soly) = get_sol(a,b,c)
  n = int(soly/a) + 1
  realy = soly - a * n
  solution = p2 * realy
  answer += solution

print answer
