# Find the maximum sum of a path down a triangle
# While this can be done brute force, Euler67 is a similar probem that
# cannot be, so we try a better solution.

tri = []
maxSums = {}

for line in open("Euler18.txt") :
	tri.append(map(int,line.split()))
	
def maxSumToGetTo(i,j) :
	try :
		return maxSums[(i,j)]
	except :
		if i == 0 :
			toReturn = tri[i][j]
		elif j == len(tri[i]) - 1 :
			toReturn = maxSumToGetTo(i-1,j-1) + tri[i][j]
		elif j == 0 :
			toReturn = maxSumToGetTo(i-1,j) + tri[i][j]
		else :
			toReturn = max([maxSumToGetTo(i-1, j-1),maxSumToGetTo(i-1,j)]) + tri[i][j]
		maxSums[(i,j)] = toReturn
		return toReturn

for i in range(15) :
	print maxSumToGetTo(14,i)