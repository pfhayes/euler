from numpy import *

rolls = [float(i)/16 for i in [1,2,3,4,3,2,1]]
#rolls = [float(i)/36 for i in [1,2,3,4,5,6,5,4,3,2,1]]
CCs = [2,17,33]
CHs = [7,22,36]

#Dice rolls
arr = zeros((41,40))
for i in range(40) :
	for j in range(len(rolls)) :
		arr[i][(i-2-j)%40] = rolls[j]

#Probabilities sum to 1
for i in range(40) :
	arr[40][i] = 1

#Go to jail
for i in range(40) :
	arr[10][i] += arr[30][i]
	arr[30][i] = 0

#Community Chest
for space in CCs :
	for i in range(40): 
		arr[0][i] += float(1)/16 * arr[space][i]
		arr[10][i] += float(1)/16 * arr[space][i]
		arr[space][i] *= (float(14)/16)
#Chance
for space in CHs :
	for i in range(40) :
		plus = float(1)/16 * arr[space][i]
		for spot in [0,10,11,24,39,5] :
			arr[spot][i] += plus
		arr[space-3][i] += plus
		if space == 7 :
			arr[15][i] += 2*plus
			arr[12][i] += plus
		if space == 22 :
			arr[25][i] += 2*plus
			arr[28][i] += plus
		if space == 36 :
			arr[5][i] += 2*plus
			arr[12][i] += plus
		arr[space][i] *= (float(6)/16)
		
for i in range(40) :
	arr[i][i] -= 1
	
solveto = zeros((41,1))
solveto[40][0] = 1

lis = linalg.lstsq(arr, solveto)
vals = sorted([(lis[0][i][0],i) for i in range(len(lis[0]))])
print vals[39][1],vals[38][1],vals[37][1]