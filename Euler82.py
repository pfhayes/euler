# Find the minimal sum from the left column to the right column

d = {}
mat = []

for line in open("Euler81.txt") :
	mat.append(map(int,line.strip().split(",")))
		
for col in range(len(mat[0])) :
	if col == 0 :
		continue
	for row in range(len(mat)) :
		minPath = mat[row][col-1]
		if row > 0 :
			if mat[row-1][col] < minPath :
				minPath = mat[row-1][col]
		if row < len(mat)-1 :
			runningTotal = mat[row+1][col] + mat[row+1][col-1]
			if runningTotal < minPath :
				minPath = runningTotal
			runningRow = row + 2
			while runningRow < len(mat) and runningTotal - mat[runningRow-1][col-1]< minPath :
				runningTotal = runningTotal - mat[runningRow-1][col-1] + mat[runningRow][col] + mat[runningRow][col-1]
				if runningTotal < minPath :
					minPath = runningTotal
				runningRow += 1
		mat[row][col] += minPath

print min([r[len(mat)-1] for r in mat])