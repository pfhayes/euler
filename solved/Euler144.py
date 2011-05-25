# Calculating the number of times that a beam of light reflects off
# the interior of an ellipse

import math

def norm((x1, x2)) :
  return math.sqrt(x1*x1+x2*x2)

def normalize((x1, x2)) :
  n = norm((x1, x2))
  return (x1/n, x2/n)

def dot((x1, x2), (y1, y2)) :
  return x1 * y1 + x2 * y2

def scalar(c, (x1, x2)) :
  return (c*x1, c*x2)

def sub((x1, x2), (y1, y2)) :
  return (x1 - y1, x2 - y2)

# Since the first ray does not come from the surface of the
# ellipse, treat it differently

start = (0.0, 10.1)
destx = 1.4
desty = -9.6
dest = (destx, desty)

incident = (sub(start, dest))
tangent = ((desty, -4*destx))
normal = ((4*destx, desty))

reflection = (sub(scalar(dot(incident, tangent), tangent), scalar(dot(incident, normal), normal)))

print dest, reflection
start = dest

bounces = 1

while True :
  (dx, dy) = normalize(reflection)
  (x, y) = start
  a = 4 * dx * dx + dy * dy
  b = 8 * x * dx + 2 * y * dy
  k = -b/a
  destx = x + k*dx
  desty = y + k*dy
  dest = (destx, desty)
  if (destx < 0.01 and destx > -0.01 and desty > 0 and bounces != 353) :
    print dest
    break

  incident = normalize(reflection)
  tangent = ((desty, -4*destx))
  normal = ((4*destx, desty))
  reflection = (sub(scalar(dot(incident, tangent), tangent), scalar(dot(incident, normal), normal)))

  bounces += 1
  start = dest

print bounces
