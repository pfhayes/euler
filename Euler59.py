# Brute force decrypt the XOR cipher

numList = map(int,open("Euler59.txt").read().split(","))

"""for i in range(103,104):
	for j in range(97,123) :
		for k in range(100,101) :
			temp = ""
			for h in range(len(numList)) :
				if h % 3 == 0 :
					if numList[h]^i < 32 :
						break
					temp= temp +(chr(numList[h] ^ i))
				if h % 3 == 1 :
					if numList[h]^i < 32 :
						break
					temp= temp +(chr(numList[h] ^ j))
				if h % 3 == 2 :
					if numList[h]^i < 32 :
						break
					temp= temp +(chr(numList[h] ^ k))
			else:
				temp = temp.lower()
				if "and" in temp or "the" in temp :
					print i,j,k,temp"""
					
# It is 103 111 100 (god)

i,j,k = 103,111,100
temp = 0
for h in range(len(numList)) :
	if h % 3 == 0 :
		temp= temp +((numList[h] ^ i))
	if h % 3 == 1 :
		temp= temp +((numList[h] ^ j))
	if h % 3 == 2 :
		temp= temp +((numList[h] ^ k))

print temp