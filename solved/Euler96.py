# Find an algorithm for solving Su Doku puzzles

import copy

r = open("Euler96.txt")

total = 0

states = []
guesses = []

for i in range(50) :
	print r.readline().strip()
	square = []
	canBe = []
	for i in range(9) :
		row = map(int,list(r.readline()[:9]))
		square.append(row)
		temp = []
		for term in row :
			if term == 0 :
				temp.append(set([1,2,3,4,5,6,7,8,9]))
			else :
				temp.append(set([]))
		canBe.append(temp)
	
	lastCanBe = 1
	val = 0
	GET_OUT = False
	solved = False
	while not solved :
		solved = True
		for x in range(9) :
			for y in range(9) :
				if square[x][y] == 0 :
					solved = False		
		GET_OUT = False
		for x in range(len(square)) :
			for y in range(len(square)) :
				if canBe[x][y] == None :
					continue
				if len(canBe[x][y]) == 1 :
					square[x][y] = canBe[x][y].pop()
				if len(canBe[x][y]) == 0 :
					if square[x][y] != 0 :
						term = square[x][y]
						for c in range(9) :
							newterm1 = canBe[x][c]
							newterm2 = canBe[c][y]
							if newterm1 != None:
								newterm1.discard(term)
							if newterm2 != None:
								newterm2.discard(term)
						topleftx = 3 * (x/3)
						toplefty = 3 * (y/3)
						for c in range(3) :
							for d in range(3) :
								newterm = canBe[topleftx+c][toplefty+d]
								if newterm != None :
									newterm.discard(term)
						canBe[x][y] = None
					else :
						GET_OUT = True
						square,canBe = states.pop()
						guess = guesses.pop()
						guessx = guess[0]
						guessy = guess[1]
						guessval = guess[2]
						canBe[guessx][guessy].discard(guessval)
						break
			if GET_OUT :
				break
		if GET_OUT :
			continue
		for x in range(0,9,3) :
			for y in range(0,9,3) :
				dic = {1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[],9:[]}
				for c in range(3) :
					for d in range(3) :
						term = canBe[x+c][y+d]
						if term == None:
							continue
						for possibility in term:
							dic[possibility].append((x+c,y+d))
				for k in dic.keys() :
					if len(dic[k]) == 1 :
						coords = dic[k][0]
						square[coords[0]][coords[1]] = k
						canBe[coords[0]][coords[1]] = set([])
		for x in range(9) :
			dic = {}
			for y in range(9) :
				if canBe[x][y] == None:
					continue
				dic[tuple(canBe[x][y])] = dic.setdefault(tuple(canBe[x][y]),0) + 1
			for key in dic.keys() :
				if len(key) == dic[key] :
					for y in range(9) :
						if canBe[x][y] == None :
							continue
						if tuple(canBe[x][y]) == key :
							continue
						for elem in key :
							canBe[x][y].discard(elem)
		for y in range(9) :
			dic = {}
			for x in range(9) :
				if canBe[x][y] == None:
					continue
				dic[tuple(canBe[x][y])] = dic.setdefault(tuple(canBe[x][y]),0) + 1
			for key in dic.keys() :
				if len(key) == dic[key] :
					for x in range(9) :
						if canBe[x][y] == None :
							continue
						if tuple(canBe[x][y]) == key :
							continue
						for elem in key :
							canBe[x][y].discard(elem)
		if canBe == lastCanBe :
			states.append((copy.deepcopy(square),copy.deepcopy(canBe)))
			lowestPosses = 1
			count = 1
			while count != 0 and lowestPosses <= 9:
				lowestPosses += count
				count = 0
				for x in range(81) :
					if canBe[x/9][x%9] == None :
						continue
					if len(canBe[x/9][x%9]) == lowestPosses :
						item = canBe[x/9][x%9].pop()
						guesses.append((x/9,x%9,item))
						canBe[x/9][x%9] = set([item])
						break
				else :
					count = 1
		lastCanBe = [[it for it in x] for x in canBe]
								
	for line in square :
		print line
	total += square[0][0]*100 + square[0][1]*10 + square[0][2]

print total

r.close()