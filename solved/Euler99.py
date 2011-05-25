# Find the line number which has the greatest value in the file

maxbase = 0
maxexp = 0
l = 0
count = 0

for line in open("Euler99.txt") :
	base, exp = map(int,(line.strip().split(",")))
	if maxbase**(maxexp/float(exp)) < base :
		maxbase = base
		maxexp = exp
		l = count
	count += 1

print maxbase, maxexp, l