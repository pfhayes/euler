# Find the shortest string such that all strings in Euler79.txt are ordered subsets of it

class Node :
	def __init__ (self, val) :
		self.val = val
		self.nextNodes = set([])

nodes = []
for i in range(10) :
	nodes.append(Node(i))

for line in open("Euler79.txt") :
	nodes[int(line[0])].nextNodes = nodes[int(line[0])].nextNodes.union(set([int(line[1])]))
	nodes[int(line[1])].nextNodes = nodes[int(line[1])].nextNodes.union(set([int(line[2])]))
	
for i in nodes :
	print i.val, i.nextNodes