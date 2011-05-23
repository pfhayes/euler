#Find the first Fibonacci number whose first and last nine digits are pandigital

from useful import digits

last1 = 1
last2 = 1
first1 = 1
first2 = 1
term = 3
lotsOfDigs = 10**15
while(True):
	lastCurr = (last1 + last2) % 10**9
	firstCurr = (first1 + first2)
	if firstCurr >= lotsOfDigs :
		firstCurr /= 10
		first2 /= 10
	last9 = digits(lastCurr)
	first9 = digits(firstCurr)[:9]
	print term, firstCurr
	if 0 not in first9 and len(first9) == 9 and len(set(first9)) == 9 and 0 not in last9 and len(last9) == 9 and len(set(last9)) == 9:
		print term
		break
	last1 = last2
	last2 = lastCurr
	first1 = first2
	first2 = firstCurr
	term += 1