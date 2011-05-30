# How many primes below 1000000 have the property that there exists some n
# such that n^3 + n^2*p is a perfect cube?

# After trying a few values, it appears that the value of n must always be a
# perfect cube.

# Observe that n^3 + n^2*p = n^2 (n - p), which means that n^2 must
# be a cube as well as n - p.

# n^2 a cube => n a cube, as previously suspected.

# Furthermore, since a^3 - b^3 = (a - b) * (a^2 + ab + b^2), this can only
# be prime if one of the factors is 1, which must be a - b. So only consecutive
# cubes can have a difference that is prime.

# Thus, since n - p is a cube and n is a cube, n - (n - p) = p is a difference
# of cubes, which is prime, so n and n - p must be consecutive.

# Thus, p is the difference between consecutive primes.

# So, we will check all consecutive cubes to see if their difference is prime

from useful import PrimeList

primes = set(PrimeList(1000000))

lastcube = 0
cube = 1
n = 1
count = 0
while cube - lastcube < 1000000 :
  if cube - lastcube in primes :
    count += 1
  lastcube = cube
  n += 1
  cube = n*n*n
print count

