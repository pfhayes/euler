# Sort a list of names alphabetically, and calculate the sum of their scores
# Each name's score is the sum of the alpha values of its chars (a=1,b=2,..)
# times the position in the list

f = open("Euler22.txt")

whole = f.read()
nameList = whole.split(",")
nameList = map(lambda x : x[1:-1],nameList)
nameList.sort()

sum=0
for i in range(len(nameList)) :
	sum+=reduce(lambda x,y : x+y, map(lambda x: ord(x)-64, nameList[i])) * (i+1)

print sum