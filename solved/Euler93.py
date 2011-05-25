# Find the set of 4 digits such that the longest chain
# from 1 to n can be formed by arithmetic operations on those digits.

def powerset(seq):
	if len(seq) :
		head = powerset(seq[:-1])
		return head + [item + [seq[-1]] for item in head]
	else:
		return [[]]

def genAllTreeVals(l) :
	if len(l) == 1 :
		return set(l)
	valset = set()
	for i in l :
		root = i
		pows = powerset(l)
		pows = pows[1:-1]
		while pows :
			x = pows[0]
			pair = ()
			for p in pows :
				if len(x+p) == len(l) and len(set(x+p))==len(l) :
					pair = (x,p)
					break
			s1 = genAllTreeVals(pair[0])
			s2 = genAllTreeVals(pair[1])
			for i in s1 :
				for j in s2 :
					valset.add(i+j)
					valset.add(i-j)
					valset.add(j-i)
					valset.add(i*j)
					try :
						valset.add(i/j)
					except :
						pass
					try :
						valset.add(j/i)
					except :
						pass
			pows.remove(pair[0])
			pows.remove(pair[1])
	return valset

def genAllList(length, firstdig=0) :
	if length == 1 :
		return [[float(k)] for k in range(firstdig,10)]
	j = []
	for i in range(firstdig,10) :
		j.extend([[float(i)] + l for l in genAllList(length-1,i+1)])
	return j

trees = genAllList(4)

maxReached = 0
maxTree = []
for t in trees:
	l = [k for k in genAllTreeVals(t) if k>0 and int(k)==k]
	l.sort()
	count = 0
	while (count < len(l) and l[count] == count+1) :
		count+=1
	if count > maxReached :
		maxReached = count
		maxTree = t

print maxTree
					