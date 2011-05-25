# Find ther area of the rectangle that contains the number of smaller rectangles closest
# to 2 000 000.

def numInRect(width,height) :
	numWaysToChoose1 = (width+1) * (height+1)
	numWaysToChoose2 = (width) * (height)
	return numWaysToChoose1 * numWaysToChoose2 / 4

coords = (0,0)
m = 1000000
for i in range(100):
	for j in range(100):
		k = abs(numInRect(i,j) - 2000000)
		if k < m :
			m = k
			coords = (i,j)

print coords
print numInRect(coords[0],coords[1])
print coords[0]*coords[1]
			