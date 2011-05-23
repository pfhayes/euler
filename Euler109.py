# Find the number of ways to check out in darts

all = []
all.extend(["S"+str(x) for x in range(1,21)])
all.extend(["D"+str(x) for x in range(1,21)])
all.extend(["T"+str(x) for x in range(1,21)])
all.extend(["S25","D25"])

def val(c) :
	points = int(c[1:])
	if c[0] == "S" :
		return points
	if c[0] == "D" :
		return 2*points
	if c[0] == "T" :
		return 3*points

target = 100

count = 0.0

for shot1 in all :
	if shot1[0] != "D" :
		continue
	if val(shot1) < target :
		count += 1
		for shot2 in all :
			if val(shot1) + val(shot2) < target :
				count += 1
				for shot3 in all :
					if val(shot1) + val(shot2) + val(shot3) < target :
						if shot2 == shot3 :
							count += 1
						else :
							count += 0.5

print count