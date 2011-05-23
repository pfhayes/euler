#!/usr/bin/env python
# Find the maximum prize fund that can be allocated to the disc game

numturns = 15
winningprob = 0

for i in range(1 << numturns) :
	count = 0
	prob = 1.0
	for j in range(numturns) :
		if i / (1 << j) % 2 == 0 :
			count += 1
			prob /= j+2
		else :
			prob *= float(j+1)/(j+2)
	if count > numturns/2 :
		winningprob += prob

print float(1)/winningprob