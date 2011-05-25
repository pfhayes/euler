peteprobs = [0] * 37
colinprobs = [0] * 37

from useful import choose, multinom

for num1s in range(10) :
	for num2s in range(10-num1s) :
		for num3s in range(10-num1s-num2s) :
			num4s = 9 - num1s - num2s - num3s
			peteprobs[num1s + 2*num2s + 3*num3s + 4*num4s] += multinom(9,num1s,num2s,num3s,num4s) * 0.25**9
			
for num1s in range(7) :
	for num2s in range(7-num1s) :
		for num3s in range(7-num1s-num2s) :
			for num4s in range(7-num1s-num2s-num3s) :
				for num5s in range(7-num1s-num2s-num3s-num4s) :
					num6s = 6-num1s-num2s-num3s-num4s-num5s
					colinprobs[num1s + 2*num2s + 3*num3s + 4*num4s + 5*num5s + 6*num6s] += multinom(6,num1s,num2s,num3s,num4s,num5s,num6s) * (float(1)/6)**6

tot = 0

for p in range(len(peteprobs)) :
	for c in range(len(colinprobs)) :
		if p > c :
			tot += peteprobs[p] * colinprobs[c]

print tot