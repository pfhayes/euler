# Find the number of words who, when replacing the letters with digits,
# are such that they have anagrams that both words form square numbers.

from math import log10
from useful import digits, digitsToNum

words = open("Euler98.txt").read().split(",")
for i in range(len(words)) :
	words[i] = words[i].strip('"')
	
m = {}
squares = {}
lengths = {}

for word in words:
	w = list(word)
	w.sort()
	w = tuple(w)
	if w in m :
		m[w].append(word)
	else :
		m[w] = [word]

for i in range(10**5) :
	sq = i**2
	digs = digits(sq)
	if len(digs) == len(set(digs)) :
		digs = len(digs)
		if digs in squares :
			squares[digs].add(sq)
		else :
			squares[digs] = set([sq])

for key in m :
	if len(m[key]) > 1 :
		l = len(m[key][0])
		if l in lengths :
			lengths[l].append(m[key])
		else :
			lengths[l] = [m[key]]

for key in reversed(sorted(lengths.keys())) :
	maxNum = 0
	for wordset in lengths[key] :
		word1, word2 = wordset[:2]
		for square in squares[len(word1)] :
			squareDigs = digits(square)
			lis = [squareDigs[word2.index(char)] for char in word1]
			if lis[0] == 0 :
				continue
			num = digitsToNum(lis)
			if num in squares[len(word1)] :
				maxNum = max([maxNum,num,square])
	print maxNum