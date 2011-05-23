# Let Sm be the m-tuple of positive real numbers with 
# x1 + x2 + ... + xm = m for which x1*x2^2*...*xm^m is maximized

# Use Lagrange multipliers

# Maximizing f(x1,...,xm) subject to g(x1,...,xm) = m

# h(x1, ..., xm, l) = f(x1, ..., xm) + l * (g(x1,...,xm) - m)
# Differentiate, set all partials to 0
#   x2^2*...*xm^m + l = 0                   (1)
#   2*x1*x2*x3^3*...*xm^m + l = 0           (2)
#     ...
#   m * x1 * x2^2 * ... * xm^(m-1) + l = 0  (m)
#   x1 + ... + xm = m   (Original constraint)

# From eq'n 1 and 2, we get
# l = -x2^2*...*xm^m/
# l = -2 * x1*x2*x3^3*...xm^m
# which tell us 2 * x1 = x2

# And, in general, x(i+1) = ((i+1)/i) * xi

# Subbing this into the constraint equation, we get
# x1 = m / (1 + ... + m)
# The rest is just calculation

import math

total = 0
for m in xrange(2,16) :
  x1 = float(m) / sum([x for x in xrange(1,m+1)])
  prod = x1
  last = x1
  for i in xrange(2,m+1) :
    next = ((float(i))/(i-1)) * last
    prod *= next**i
    last = next
  print prod, int(prod)
  total += int(prod)

print total
