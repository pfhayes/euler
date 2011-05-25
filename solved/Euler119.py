from useful import digits
from math import log10

i = 2
lis = []
try :
	while (True) :
		prod = i
		while (log10(prod) < i) :
			if (sum(digits(prod)) == i) :
				lis.append(prod)
			prod *= i
		i += 1
except KeyboardInterrupt, e :
	print sorted(lis)