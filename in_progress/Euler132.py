from useful import divisors,primeFactorize,PrimeList

# We observe that 1111...1111 of 2n digits
# = 1111...1111 * 100000...0001, where the lengths are n, n+1

# Call 1000000...0001 of n+1 digits D(n)
# So, R(2n) = R(n) * D(n)

def R(n) :
  ret = 1
  while n > 1 :
    ret = ret * 10 + 1
    n -= 1
  return ret

def D(n) :
  return 10**(n) + 1

num = 10**9
while num % 2 == 0 :
  num = num / 2
# num = 1953125

# So, R(10**9) = R(1953125) * D(1953125) * D(2*1953125) * ... * D(1/2 * 10**9)
# And, there are 9 of these D terms

# More generally, if 1111...1111 = R(pq), then R(pq) = R(p) * 10...010...01
# where there are q 1's and each block of 0's has length p - 1

# So, since 1953125 = 5**9, we can get it to
# R(5) * D2(5) * D2(25) * D2(125) * ... * D2(390625)
# where D2(n) = 1000010000100001....100001, with 5n+1 digits

# Observe that the D's are never divisible by 3, or 5.
# And, after trying many possibilities, the only D's that are divisible
# by 7 are D(3), D(9), D(15), D(21), ...
# So, none of the D's we have here.
# Similarly, no R(2n+1) is divisible by 7, so our R isn't.

# When is D(n) divisible by 11? Since 1001 = 91 * 11, 100001 = 9091 * 11,
# 10000001 = 909091 * 11, ...
# Now, observe that D(1), D(3), D(5), ... are divisible by 11

# So, only D(1953125) is divisible by 11, and the rest are divisible only
# by primes larger than 11

# Now, grab primes and use a classic long division algorithm to check
# divisibility

def checkDivisibilityR(length, p) :
  digs_left = length - 1
  cmp = 1
  rem = cmp % p
  while digs_left > 0 :
    digs_left -= 1
    cmp = 10*rem + 1
    rem = cmp % p
  if (rem == 0) :
    return 1 + checkDivisibilityR(length, p*p)
  return 0

def checkDivisibilityD(length, p) :
  digs_left = length - 1 # There are length+1 digits, and we take off 2
  cmp = 10
  rem = cmp % p
  while digs_left > 1 :
    digs_left -= 1
    cmp = 10*rem
    rem = cmp % p
  cmp = 10*rem + 1
  rem = cmp % p
  if (rem == 0) :
    return 1 + checkDivisibilityD(length, p*p)
  return 0

primes = PrimeList(100000)
primes = primes[5:] # Skip 2,3,5,7
divisors = [11]
top = 10**9

for prime in primes :
  print "Starting", prime
  """
  divisors.extend([prime] * checkDivisibilityR(1953125, prime))
  if (len(divisors) >= 40) :
    break
    """
  print divisors
  divisors.extend([prime] * checkDivisibilityD(top/512, prime))
  if (len(divisors) >= 40) :
    break
  """
  print divisors
  divisors.extend([prime] * checkDivisibilityD(top/256, prime))
  if (len(divisors) >= 40) :
    break
  print divisors
  divisors.extend([prime] * checkDivisibilityD(top/128, prime))
  if (len(divisors) >= 40) :
    break
  print divisors
  divisors.extend([prime] * checkDivisibilityD(top/64, prime))
  if (len(divisors) >= 40) :
    break
  print divisors
  divisors.extend([prime] * checkDivisibilityD(top/32, prime))
  if (len(divisors) >= 40) :
    break
  print divisors
  divisors.extend([prime] * checkDivisibilityD(top/16, prime))
  if (len(divisors) >= 40) :
    break
  print divisors
  divisors.extend([prime] * checkDivisibilityD(top/8, prime))
  if (len(divisors) >= 40) :
    break
  print divisors
  divisors.extend([prime] * checkDivisibilityD(top/4, prime))
  if (len(divisors) >= 40) :
    break
  print divisors
  divisors.extend([prime] * checkDivisibilityD(top/2, prime))
  if (len(divisors) >= 40) :
    break
  print divisors
  """
  print "After", prime, ",", divisors
print "Done!"
print divisors
print sum(divisors[:40])
