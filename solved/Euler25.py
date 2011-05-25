# Find the first Fibonacci number with over 1000 digits
from math import sqrt, log10

fibos = {1:1, 2:1}
phi = (1 + sqrt(5))/2.0

def fib(n) :
	try :
		return fibos[n]
	except :
		fibos[n] = fib(n-1) + fib(n-2)
		return fibos[n]

count = 1
while True:
	count += 1
	if log10(fib(count)) >= 999:
		print count
		break