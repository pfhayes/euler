# Find the minimal way to connect the network

class Node :
	def __init__(self,num) :
		self.root = num
		self.connects = {}
	
	def __str__ (self) :
		return str(self.root)
		
	def __repr__ (self) :
		return str(self.root)

nodes = [Node(x) for x in range(40)]

total = 0
smallest = 1000
smallestPair = ()

col = 0
for line in open("Euler107.txt") :
	lis = line.strip().split(",")
	for i in range(len(lis)) :
		if lis[i] == "-" :
			continue
		else :
			val = int(lis[i])
			total += val
			if val < smallest :
				smallest = val
				smallestPair = (i,col)
			nodes[i].connects[col] = val
	col += 1

total = total/2
	
networkSize = col

network = set([nodes[smallestPair[0]], nodes[smallestPair[1]]])

connections = {smallestPair:smallest}

while (len(network) < networkSize) :
	minVal = 1000
	minNode = None
	pair = ()
	for node in network :
		ks = node.connects.keys()
		for key in ks :
			if nodes[key] in network :
				continue
			if node.connects[key] < minVal :
				minVal = node.connects[key]
				pair = (node.root, key)
				minNode = nodes[key]
	if minNode == None :
		quit("HAAAAAAHHAAA")
	network.add(minNode)
	connections[pair] = minVal
	newTotal += minVal

newTotal = sum(connections.values())
print total, newTotal, total - newTotal