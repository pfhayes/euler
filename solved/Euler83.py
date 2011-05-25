# Find the minimal sum from the top left to the bottom right corner

# Hurf durf Dijkstra's algorithm

class Vertex :
  pass

mat = []
vertices = []

for line in open("matrix.txt") :
	mat.append(map(int,line.strip().split(",")))

size = 80
nullv = Vertex()
nullv.dist = 2**30+1
Q = set([])

for i in xrange(size) :
  vertices.append([])
  for j in xrange(size) :
    v = Vertex()
    v.val = mat[i][j]
    v.adjacents = []
    v.dist = 2**30
    v.prev = nullv
    vertices[i].append(v)
    Q.add(v)

for i in xrange(size) :
  for j in xrange(size) :
    v = vertices[i][j]
    if i >= 1 :
      v2 = vertices[i-1][j]
      v.adjacents.append((v2, v2.val))
    if i < size - 1:
      v2 = vertices[i+1][j]
      v.adjacents.append((v2, v2.val))
    if j >= 1 :
      v2 = vertices[i][j-1]
      v.adjacents.append((v2, v2.val))
    if j < size - 1 :
      v2 = vertices[i][j+1]
      v.adjacents.append((v2, v2.val))

vertices[0][0].dist = vertices[0][0].val

while len(Q) > 0 :
  minv = nullv
  for v in Q :
    if v.dist < minv.dist :
      minv = v
  Q.remove(minv)
  for adj in minv.adjacents :
    (nextv, dist_bet) = adj
    alt = minv.dist + dist_bet
    if (alt < nextv.dist) :
      nextv.dist = alt
      v.prev = minv


print vertices[size-1][size-1].dist
