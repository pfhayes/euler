# Find the sum of both diagonals in a 1001 by 1001 spiral formed as follows:
#	21	22	23	24	25	...
#	20	7	8	9	10
#	19	6	1	2	11
#	18	5	4	3	12
#	17	16	15	14	13

sum = 1
for i in range (2,1002) :
	# Bottom left to top-right diagonal
	if i % 2 == 0 :
		sum += (i)**2 + 1 + (i)**2 - i + 1
	else :
		sum += (i)**2 + (i)**2 - i + 1
		
print sum