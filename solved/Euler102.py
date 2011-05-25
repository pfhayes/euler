# Find the number of triangles in the text file that contain the origin

from useful import genLineFunc

count = 0
temp = 0
for line in open("Euler102.txt") :
	toks = map(int,line.split(","))
	A = tuple(toks[0:2])
	B = tuple(toks[2:4])
	C = tuple(toks[4:6])
	all = [A,B,C]
	if (0,0) in all :
		continue
	lessThan0 = [x for x in all if x[0] < 0]
	moreThan0 = [x for x in all if x[0] > 0]
	if len(moreThan0) == 0 or len(lessThan0) == 0:
		continue
	if len(moreThan0) > len(lessThan0) :
		biggerList = moreThan0
		singlePoint = lessThan0[0]
	else :
		biggerList = lessThan0
		singlePoint = moreThan0[0]
	l1 = genLineFunc(biggerList[0],singlePoint)
	l2 = genLineFunc(biggerList[1],singlePoint)
	if (l1(0) > 0 and l2(0) < 0) or (l1(0) < 0 and l2(0) > 0) :
		count += 1

print count