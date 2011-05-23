# Find the number of lines in Euler105.txt that obey the special sumset property

from useful import powerset

total = 0
for line in open("Euler105.txt") :
	s = map(int, line.split(","))
	print s,"",
	bad = False
	for subs in powerset(s)[1:-1] :
		g = set(subs)
		comp = list(set(s) - g)
		for altSet in powerset(comp)[1:] :
			diff = (sum(g) - sum(altSet))
			if diff == 0 or float(len(g) - len(altSet)) / diff < 0 :
				print g, altSet,
				print "No!"
				bad = True
				break
		if bad :
			break
	else :
		print "Yes!",
		k = sum(s)
		total += k
		print k
print total