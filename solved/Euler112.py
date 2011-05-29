# A number is bouncy if the digits of the nmber are nonincreasing and
# nondecreasing
# Find the number for which the proportion of bouncy numbers below it is 99%

def isIncreasing(num, below=9) :
  if num <= below :
    return True
  if num % 10 <= below :
    return isIncreasing(num / 10, num%10)
  return False

def isDecreasing(num, above=0) :
  if above <= num < 10 :
    return True
  if num % 10 >= above :
    return isDecreasing(num / 10, num%10)
  return False

bouncies = 0
n = 1
while True :
  if isIncreasing(n) or isDecreasing(n) :
    pass
  else :
    bouncies += 1
  if 100 * bouncies == 99 * n :
    break
  n += 1

print n
