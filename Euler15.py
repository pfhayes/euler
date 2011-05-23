# Find the number of paths through a 20 * 20 grid
# If we lay the grid out like Pascal's triangle, each possible node
# has the number of possible paths leading to it equal to the sum
# of the nodes above it.

def get (l, n) :
	try :
		return l[n]
	except :
		return 0

l = [1]

for i in range(20) :
	l2 = [1]
	for i in range(len(l)) :
		l2.append(get(l,i)+get(l,i+1))
	l = l2
	
while len(l) > 1 :
	l2 = []
	for i in range(len(l) - 1):
		l2.append(l[i]+l[i+1])
	l = l2

print l[0]