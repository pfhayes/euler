def fig(i,n) :
	if i == 3:
		return n*(n+1)/2
	if i == 4:
		return n*n
	if i == 5 :
		return n*(3*n-1)/2
	if i == 6:
		return n*(2*n-1)
	if i == 7:
		return n*(5*n-3)/2
	if i == 8:
		return n*(3*n-2)
	raise Exception
	
def first(n) :
	return n/100

def last(n) :
	return n%100

d = {}

for i in range(3,9) :
	d[i] = set([])
	count = 1
	num = 1
	while num < 10000 :
		if num >= 1000 and num / 10 % 10 != 0:
			d[i].add(num)
		count += 1
		num = fig(i, count)

def findInRest(targetFirstDigs, lis, initialFirstDigs, trail) :
	if lis :
		for key in d.keys() :
			if key not in lis :
				continue
			else :
				se = d[key]
				for cand in se :
					if first(cand) == targetFirstDigs :
						findInRest(last(cand), [x for x in lis if x!=key], initialFirstDigs,trail+[cand])
	else :
		if targetFirstDigs == initialFirstDigs :
			print trail
			print sum(trail)
			quit()

for num in d[3] :
	findInRest(last(num),[4,5,6,7,8],first(num),[num])