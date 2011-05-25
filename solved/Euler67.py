# Find the maximum sum of a path down a triangle
# This is similar to Euler18, only this is much to large to be done by
# brute force. Here's hoping the recursive algorithm was good enough...

tri = []
maxSums = {}

for line in open("Euler67.txt") :
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

m = 0
for i in range(100) :
	m = max([maxSumToGetTo(99,i),m])
	
print m