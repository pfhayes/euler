prod = 0

f = open ("Euler11.txt")
arr = []
for line in f :
	l = line.split(" ")
	l = map(int, l)
	arr.append(l)
	
def get (i,j) :
	try :
		num = arr[i][j]
	except :
		num = 0
	return num

for i in range(20) :
	for j in range(20) :
		prod = max([prod,
					get(i, j)*get(i+1, j)*get(i+2, j)*get(i+3, j),
					get(i, j)*get(i, j+1)*get(i, j+2)*get(i, j+3),
					get(i, j)*get(i+1, j+1)*get(i+2, j+2)*get(i+3, j+3),
					get(i+3,j)*get(i+2,j+1)*get(i+1,j+2)*get(i, j+3)])
					
print prod