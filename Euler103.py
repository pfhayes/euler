# Find the minimal 7 item special sum set

from useful import powerset

best = []
minsum = 100000
for a1 in range(20,47) :
	for a2 in range(a1+1,47) :
		for a3 in range(a2+1, 47) :
			for a4 in range (a3+1, 47) :
				for a5 in range(a4+1, 47) :
					for a6 in range(a5+1, 47) :
						for a7 in range(a6+1, 47) :
							bad = False
							s = [a1,a2,a3,a4,a5,a6,a7]
							i = 1
							while (2*i + 1 <= len(s)) :
								if sum(s[:i+1]) < sum(s[-i:]) :
									bad = True
									break
								i += 1
							if bad :
								continue
							sums = set([])
							for k in powerset(s)[1:-1] :
								p = sum(k)
								if p in sums :
									bad=True
									break
								else :
									sums.add(p)
							else :
								l = sum(s)
								print s
								if l < minsum :
									minsum = l
									best = s
print best
