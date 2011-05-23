# Define a||1 = a
# a||(k+1) = a^(a||k), where || is Knuths' Up-arrow notation

# Find the last 8 digits of 1777||1855

i = 1
last = 1777
top = 1885

while i < top :
  last = pow(1777,last,100000000)
  i += 1

print last
