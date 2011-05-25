from useful import primeFactorize, primeList

primes = primeList(1000)

def search(lis) :
	n = 1
	for i in range(len(lis)) :
		n *= primes[i]**lis[i]
	x = n+1
	count = 0
	while x <= 2*n :
		if ((x * n) % (x-n) == 0) :
			count += 1
		x += 1
	#print n, lis, count
	if count >= 1000 :
		print n, count
	else :
		search(lis + [1])
		for j in range(len(lis)-1, -1, -1) :
			temp = lis[:]
			temp[j] = temp[j]+1
			dosearch = True
			for k in range(len(temp)-1) :
				if (temp[k] < temp[k+1]) :
					dosearch = False
			if (dosearch) :
				search(temp)
		

	

search([1])