# Find the number of ways to make 200 pence out of the following coins:
# 200p, 100p, 50p, 20p, 10p, 5p, 2p, 1p

sum = 0
count = 0
for twohundred in range (1,-1,-1) :
	sum = twohundred * 200
	for onehundred in range(2 - sum/100,-1,-1) :
		sum = twohundred * 200 + onehundred * 100
		for fifty in range (4 - sum/50, -1, -1) :
			print fifty
			sum = twohundred * 200 + onehundred * 100 + fifty * 50
			for twenty in range (10 - sum/20, -1, -1) :
				sum = twohundred * 200 + onehundred * 100 + fifty * 50 + twenty * 20
				for ten in range (20 - sum/10, -1, -1) :
					sum = twohundred * 200 + onehundred * 100 + fifty * 50 + twenty * 20 + ten * 10
					for five in range (40 - sum/5, -1, -1) :
						sum = twohundred * 200 + onehundred * 100 + fifty * 50 + twenty * 20 + ten * 10 + five * 5
						for two in range(100 - sum/2, -1, -1) :
							sum = twohundred * 200 + onehundred * 100 + fifty * 50 + twenty * 20 + ten * 10 + five * 5 + two * 2
							for one in range(200 - sum, -1, -1) :
								if (twohundred * 200 + onehundred * 100 + fifty * 50 + twenty * 20 + ten * 10 + five * 5 + + two * 2 + one == 200) :
									count += 1
print count