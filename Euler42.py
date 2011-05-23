# Find the number of words in the text file that make a triangle number when their letter-values are summed.

vals = {}
maxSum = 0
words = open("Euler42.txt").read().split(",")
for word in words :
	sum = 0
	for c in word[1:-1] :
		sum += ord(c) - 64	
	vals[sum] = vals.setdefault(sum, 0) + 1
	maxSum = max((maxSum, sum))

tris = []
count = 1
while count * (count+1) / 2 < maxSum :
	tris.append(count*(count+1)/2)
	count += 1

total = 0
for t in tris :
	total += vals.setdefault(t,0)

print total