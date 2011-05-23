# Find the maximum 16-digit string for a magic 5-gon ring
	# Solution adapted from Euler66.py

from useful import digits, digitsToNum

class Binder :

	def __init__ (self,val=0):
		self.maxNum = val
	
	def numify(self,lis) :
		ret = []
		for l in lis :
			ret.extend(digits(l))
		return digitsToNum(ret)
	
	def completeRing(self,middleDig, numsLeft, lastDig, trail, rowSum) :
		if numsLeft :
			targSum = rowSum - middleDig
			for num in numsLeft :
				if num == lastDig :
					continue
				thirdDig = targSum - num
				if thirdDig in numsLeft :
					self.completeRing(thirdDig,
									numsLeft-set([num,thirdDig]),
									lastDig,
									trail+[num,middleDig,thirdDig],
									rowSum)
		else :
			if middleDig == lastDig and trail.count(10) == 1 :
				minVal = 11
				minPos = 0
				for i in range(0,len(trail),3) :
					if trail[i] < minVal :
						minVal = trail[i]
						minPos = i
				trail = trail[minPos:] + trail[:minPos]
				val = self.numify(trail)
				if val > self.maxNum :
					self.maxNum = val

for i in range(14,17) :
	print i
	for num in range(1,11) :
		b = Binder(0)
		b.completeRing(num, set(range(1,11)), num, [],i)
		if b.maxNum :
			print b.maxNum