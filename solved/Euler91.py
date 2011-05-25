# Find the number of points P(x1,y1) and Q(x2,y2) such that triangle OPQ is right-angled
# for 0 <= x1,x2,y1,y2 <= 50

def dot(v1,v2) :
	s = 0
	for i, j in zip(v1,v2) :
		s += i*j
	return s

d = {}

square = 51
count = 0
for x1 in range(square):
	print x1
	for x2 in range(square) :
		for y1 in range(square) :
			for y2 in range(square) :
				if (x1,y1) == (0,0) or (x2,y2) == (0,0) or (x1,y1) == (x2,y2) :
					break
				v1 = (x1, y1)
				v2 = (x2,y2)
				v3 = (x2-x1,y2-y1)
				if (dot(v1,v2) == 0 or dot(v1,v3) == 0 or dot(v2,v3)==0) :
					if ((x1,y1), (x2,y2)) not in d and ((x2,y2), (x1,y1)) not in d:
						d[((x1,y1), (x2,y2))] = True
						count += 1
print count
