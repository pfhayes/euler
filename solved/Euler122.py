# Find the most efficient exponentiation method

d = {1:0, 2:1}

max = 200

def genAllMins (n, se, numMults) :
	if n > max :
		return
	se = se | set([n])
	for it in reversed(sorted(list(se))) :
		if it + n in d :
			if numMults + 1 <= d[it+n] :
				d[it+n] = numMults + 1
				genAllMins(n+it,se,numMults+1)
		else :
			d[it+n] = numMults+1
			genAllMins(n+it,se,numMults+1)

genAllMins(2,set([1]),1)

print sum([d[k] for k in d.keys() if k <= max])