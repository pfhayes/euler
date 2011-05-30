# First we make the observation that the number of solutions to
# 1/x + 1/y = 1/n is the same as the number of divisors of (n^2)
# that are <= n. Since n^2 will always have an odd number of
# divisors, we can just take (numdivisors(n^2) + 1) / 2 to
# get the number of divisors less than or equal to n

# Now, we want to find the smallest number n such that
# numdivisors(n^2) >= 8000003. Our next observation is that if the
# prime factorization of n is p1^a1 * p2^a2 * ... * pn^an, then 
# the number of divisors of n is (a1 + 1) * (a2 + 1) * .. * (an + 1).
# and also the number of divisors of n^2 is (2*a1 +1)  * .. * (2*an+1).

# Next, observe that this is true regardless of the values of
# p1, ..., pn. So, in order to minimize the value of n, we
# will have that p1 = 2, p2 = 3, p3 = 5, ..., and also that
# a1 >= a2 >= a3 >= ...

# So, under these conditions, find the values of a1 that will minimize
# the value of n

from useful import numdivisors, primeFactorize, PrimeList

top_prime = 500000
primes = PrimeList(top_prime)
print "Got primes"

# Step 1: Search for values of a1,...,an such that
# (2*a1 + 1) * ... * (2*an + 1) >= 8000003, with a1 >= a2 >= ...

top = 8000003

def compute_prod(a_list) :
  ret = 1
  for a in a_list :
    ret *= 2*a + 1
  return ret

def compute_n(a_list) :
  ret = 1
  for i in xrange(len(a_list)) :
    ret *= primes[i]**a_list[i]
  return ret

best_n = [9999999999999999999999999999]

def dfs (a_list) :
  prod = compute_prod(a_list)
  if prod > top :
    # The factors have reached a point where they create a number whose
    # number of divisors is large enough. Adding new factors will not help,
    # so compute the value of n and check to see if it is best
    n = compute_n(a_list)
    if n < best_n[0] :
      best_n[0] = n
      print n, a_list
  else :
    # The number isn't large enough and needs more factors. Add factors in 
    # such a way that preserves a1 >= a2 >= ...
    old_val = a_list[0]
    prod /= 2*a_list[0] + 1
    new_val = top / prod
    new_val = (new_val - 1)/2 + 1
    a_list[0] = new_val
    dfs(a_list)
    for i in xrange(len(a_list) - 1) :
      if (a_list[i] > a_list[i+1]) :
        a_list[i+1] += 1
        dfs(a_list)
        a_list[i+1] -= 1
    dfs(a_list + [1])
    a_list[0] = old_val

dfs([1])
