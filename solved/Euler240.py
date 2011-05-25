# Find the number of ways that twenty 12-sided die can be rolled so the top ten dice sum to 70

from useful import allSums, choose, multinom, fact

topNum = 10
totalNum = 20
diceLeft = totalNum-topNum
diceVal = 12
sumTo = 70

allWays = 0
for sum in allSums(topNum,sumTo,1,diceVal) :
	counts = [0] * diceVal
	for dig in sum :
		counts[dig-1] += 1
	upperBound = sum[0]
	thisManyWays = 0
	for reps in xrange(diceLeft+1) :
		counts[upperBound-1] += reps
		thisManyWays += multinom(totalNum, *(counts)) * (upperBound-1)**(diceLeft-reps) / fact(diceLeft-reps)
		counts[upperBound-1] -= reps
	allWays += thisManyWays

print allWays