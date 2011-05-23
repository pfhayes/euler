# Find the number of strings made of {L,O,A} of length 30 such that
# there are no blocks of 3 consecutive A's, or more than one L

# Use the generating function for
# {e, A, AA} ({0}{e, A, AA})* ({e} U {L}{e,A,AA}({0}{e,A,AA])*)

less6 = 3
less5 = 8
less4 = 19
less3 = 43
less2 = 94
less1 = 200

i = 7
curr = 0
while i <= 30 :
  curr = 2*less1 + less2 - 3*less4 - 2 *less5 - less6
  print i, curr
  i += 1
  less6 = less5
  less5 = less4
  less4 = less3
  less3 = less2
  less2 = less1
  less1 = curr

print curr
