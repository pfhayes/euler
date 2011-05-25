# Find how many hands player 1 won.

class Card :
	def __init__ (self, num, suit) :
		if num == "T" :
			self.num = 10
		elif num == "J" :
			self.num = 11
		elif num == "Q" :
			self.num = 12
		elif num == "K" :
			self.num = 13
		elif num == "A" :
			self.num = 14
		else :
			self.num = int(num)
		self.suit = suit
			
class Hand :

	def __init__ (self, c1, c2, c3, c4, c5) :
		cards = (Card(c1[0],c1[1]),
		Card(c2[0],c2[1]),
		Card(c3[0],c3[1]),
		Card(c4[0],c4[1]),
		Card(c5[0],c5[1]))
		__init__(self, cards)

	def __init__ (self, cards) :
		for i in range(len(cards),0,-1) :
			for j in range(i-1) :
				if cards[j].num < cards[j+1].num :
					temp = cards[j]
					cards[j] = cards[j+1]
					cards[j+1] = temp
		self.cards = cards
		kindScore = 0
		breaker1 = 0
		breaker2 = 0
		numOf = [0 for i in range(15)]
		numOfSuits = {}
		for c in cards :
			numOf[c.num] += 1
			numOfSuits[c.suit] = numOfSuits.setdefault(c.suit,0) + 1
		if 5 in numOfSuits.values() and cards[0].num - 1 == cards[1].num and cards[1].num - 1 == cards[2].num and cards[2].num - 1 == cards[3].num and cards[3].num - 1 == cards[4].num :
			kindScore = 8
		elif 4 in numOf :
			kindScore = 7
			breaker1 = numOf.index(4)
		elif 3 in numOf and 2 in numOf :
			kindScore = 6
			breaker1 = numOf.index(3)
			breaker2 = numOf.index(2)
		elif 5 in numOfSuits.values() :
			kindScore = 5
		elif cards[0].num - 1 == cards[1].num and cards[1].num - 1 == cards[2].num and cards[2].num - 1 == cards[3].num and cards[3].num - 1 == cards[4].num :
			kindScore = 4
		elif 3 in numOf :
			kindScore = 3
			breaker1 = numOf.index(3)
		elif 2 in numOf and 2 in numOf[numOf.index(2)+1:] :
			kindScore = 2
			breaker1 = numOf[numOf.index(2)+1:].index(2)
			breaker2 = numOf.index(2)
		elif 2 in numOf :
			kindScore = 1
			breaker1 = numOf.index(2)
		self.score = kindScore * 10**14 + breaker1 * 10**12 + breaker2 * 10**10 + cards[0].num * 10**8 + cards[1].num * 10**6 + cards[2].num * 10**4 + cards[3].num * 10**2 + cards[4].num

def make (c1, c2, c3, c4, c5) :
		cards = [Card(c1[0],c1[1]),
		Card(c2[0],c2[1]),
		Card(c3[0],c3[1]),
		Card(c4[0],c4[1]),
		Card(c5[0],c5[1])]
		return Hand(cards)
	
print make("3H","4H","5H",'6H','7H').score
	
count = 0
for line in open("Euler54.txt") :
	cards = []
	for i in range (0,15,3) :
		cards.append(Card(line[i], line[i+1]))
	hand1 = Hand(cards)
	cards = []
	for i in range (15,30,3) :
		cards.append(Card(line[i], line[i+1]))
	hand2 = Hand(cards)
	
	if hand1.score > hand2.score :
		count += 1
		
print count