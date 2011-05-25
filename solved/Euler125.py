# Find the sum of all palindromic numbers below 10^8
# that can be written as the sum of squares

from useful import oddPalify, evenPalify

palindromes = []

for i in range (1,10000) :
	palindromes.append(oddPalify(i))
	palindromes.append(evenPalify(i))

total = 0
i = 0
for palin in palindromes :
  i += 1
  lower = 1
  upper = 2
  sum = 5
  while lower < upper :
    while sum < palin :
      upper += 1
      sum += upper*upper
    if sum == palin :
      break
    sum -= lower*lower
    lower += 1
  if lower < upper :
    total += sum

print total
