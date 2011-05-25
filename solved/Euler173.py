# Find the number of large squares with square holes in the center
# using up to a million small square tiles

total_tiles = 1000000
count = 0

# Given an upper bound for the dimension of the outer square,
# and a lower bound for the dimension of the inner square,
# find the number of possibile configurations
# Assuming upper > lower, and upper and lower are either
# both even or both odd
def getPossibilities(lower, upper) :
  howMany = (lower - upper)/2
  return howMany * (howMany - 1) / 2

count = 0

# Odds
lower = 1
upper = 3
squares_used = 8
lastUpper = -1

while upper >= lower + 2 :
  while squares_used <= total_tiles :
    squares_used += 4*upper + 4
    upper += 2
  count += getPossibilities(upper, lower)
  if lastUpper != -1 :
    count -= getPossibilities(lastUpper, lower)
  lastUpper = upper 
  while squares_used > total_tiles :
    squares_used -= 4*lower + 4
    lower += 2

# Now do the same for evens
lower = 2
upper = 4
squares_used = 12
lastUpper = -1

while upper >= lower + 2 :
  while squares_used <= total_tiles :
    squares_used += 4*upper + 4
    upper += 2
  count += getPossibilities(upper, lower)
  if lastUpper != -1 :
    count -= getPossibilities(lastUpper, lower)
  lastUpper = upper
  while squares_used > total_tiles :
    squares_used -= 4*lower + 4
    lower += 2

print count
