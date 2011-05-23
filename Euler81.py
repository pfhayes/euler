# Find the minimal sum from the top left to the bottom right

d = {}
mat = []

for line in open("Euler81.txt") :
	mat.append(map(int,line.strip().split(",")))

def minToGetTo(x,y) :
	if (x,y) in d :
		return d[(x,y)]
	elif x == 0 and y == 0 :
		d[(x,y)] = mat[0][0]
		return mat[0][0]
	elif x >= 80 or x < 0 or y >= 80 or y < 0 :
		return 2**32
	else :
		ret = min([minToGetTo(x-1,y),minToGetTo(x,y-1)]) + mat[x][y]
		d[(x,y)] = ret
		return ret

print minToGetTo(79,79)