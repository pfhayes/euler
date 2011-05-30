# Useful functions for Projet Euler

# Returns a list of all primes less than n

from math import sqrt, log10

def flatten(lis) :
	l = []
	for it in lis :
		if isinstance(it, (list, tuple)) :
			l.extend(flatten(it))
		else :
			l.append(it)
	return l

#----------------------MODULUS-----------------------

def multMod (base,exp,mod) :
	squares = [base % mod]
	temp = 2
	ret = 1
	while temp <= exp :
		squares.append(squares[-1]**2 % mod)
		temp*=2
	for i in reversed(xrange(len(squares))) :
		if exp % 2 :
			ret *= squares[i]
		exp /= 2
	return ret % mod

#-----------------------SETS-------------------------

def powerset(seq):
	if len(seq) :
		head = powerset(seq[:-1])
		return head + [item + [seq[-1]] for item in head]
	else:
		return [[]]

def genAllLists(length, currNum, maxNum, repeats=False) :
	if length == 0 :
		return [[]]
	else :
		tabs = []
		if repeats :
			for firstDig in xrange(currNum,maxNum+1) :
				for lis in genAllLists(length-1, firstDig, maxNum,repeats) :
					l = [firstDig]
					l.extend(lis)
					tabs.append(l)
		else :
			for firstDig in xrange(currNum,maxNum+1) :
				for lis in genAllLists(length-1, firstDig+1, maxNum,repeats) :
					l = [firstDig]
					l.extend(lis)
					tabs.append(l)
		return tabs

def allArrangements(lis) :
	if not lis :
		return [[]]
	ret = []
	for i in xrange(len(lis)) :
		ret.extend([[lis[i]]+p for p in allArrangements(lis[:i]+lis[i+1:])])
	return ret

def allSums(numItems, s, mi, ma) :
	if numItems == 0 :
		if s == 0 :
			return [[]]
		return []
	ret = []
	for it in xrange(mi, ma+1) :
		ret.extend([[it] + lis for lis in allSums(numItems-1, s - it, it, ma)])
	return ret
		

#---------------------MATRICES-----------------------

class Matrix :
	def __init__ (self,body) :
		self.body = body
		
#---------------------GRAPHING-----------------------

def genLineFunc(p1,p2) :
	if p1 == p2 :
		raise IllegalArgumentException
	elif (p1[0] == p2[0]) :
		def f(x) :
			return p1[0]
	else :
		def f(x):
			m = (p2[1] - p1[1])/float((p2[0]-p1[0]))
			b = (p1[1] - (m*p1[0]))
			return m*x + b
	return f
		

#---------------------MEMOIZATION--------------------

def memoize(func) :
	def memoized_func(*args) :
		d = {}
		if args in d :
			return d[args]
		else :
			ret = func(*args)
			d[args] = ret
			return ret
	return memoized_func
		

#----------------------COMBINATORIAL---------------------

def fact(n) :
  ret = 1
  while n >= 2 :
    ret *= n
    n -= 1
  return ret

def gcd(a,b) :
	if b == 0 :
		return a
	return gcd(b, a%b)

def perm(n,k) :
	if k== 0:
		return 1
	return reduce ((lambda x, y: x*y), xrange(n,n-k,-1))

def choose(n,k) :
	return perm(n,k) / fact(k)

def multinom(n, *args) :
	ret = fact(n)
	for arg in args :
		ret /= fact(arg)
	return ret

#------------------------BASES-----------------------

def base(n, b) :
	st = ""
	while n > 0 :
		st = str(n%b) + st
		n /= 2
	return st

def bin(n) :
	return base(n,2)
	

#------------------------DIGITS----------------------

def digitsToNum(l, base=10) :
	num = 0
	for dig in l :
		num *= base
		num += dig
	return num

def digits (n, numDigits=-1, base=10) :
	if n == 0 : 
		if numDigits < 1 :
			return [0]
		else :
			return [0]*numDigits
	digs = []
	while n > 0 :
		digs, n = [int(n%base)]+digs, n/base
	if len(digs) < numDigits :
		digs = [0 for x in xrange(numDigits-len(digs))] + digs
	return digs

def evenPalify(n) :
	num = 0
	digs = digits(n)
	for d in digs :
		num += d
		num *= 10
	digs.reverse()
	for d in digs :
		num += d
		num *= 10
	return num/10
	
def oddPalify(n) :
	num = 0
	digs = digits(n)
	for d in digs :
		num += d
		num *= 10
	digs.reverse()
	for d in digs[1:] :
		num += d
		num *= 10
	return num/10

def isPali(st) :
	st = str(st)
	for i in xrange(len(st)/2+1) :
		if st[i] != st[-i-1] :
			return False
	return True

#------------------------PRIMES----------------------

def primeList(n):
	# returns a list of prime numbers from 2 to < n
	if n < 2:
		return []
  	if n == 2:
  		return [2]
  	# do only odd numbers starting at 3
  	s = range(3, n, 2)
  	# n**0.5 may be slightly faster than math.sqrt(n)
  	mroot = n ** 0.5
  	half = len(s)
  	i = 0
  	m = 3
  	while m <= mroot:
		if s[i]:
	  		j = (m * m - 3)//2
	  		while j < half:
				s[j] = 0
				j += m
		i = i + 1
		m = 2 * i + 3
  	# make exception for 2
	return [2]+[x for x in s if x]

def isPrime(n) :
	if n == 1 or n == 0 :
		return False
	if n == 2 :
		return True
	if n % 2 == 0 :
		return False
	for p in xrange(3,int(sqrt(n))+1, 2) :
		if n % p == 0:
			return False
	return True

# Returns a set of all prime factors of n
def primeFactorize (n, primes=[]) :
  ret = []
  if not primes :
    primes = PrimeList(int(sqrt(n)+1))
  for p in primes :
    while n % p == 0 :
      ret.append(p)
      n /= p
    if n == 1 :
      return ret
  return ret + [n]

def doubleFactorize(n) :
	ret = []
	for f in xrange(1,int(sqrt(n))+1) :
		if n % f == 0:
			ret.append((f,n/f))
	return ret

def numdivisors(n, primes=[]) :
  if primes == [] :
    primes = PrimeList(int(sqrt(n) + 1))
  ret = 1
  curr = 2
  top = n
  for p in primes :
    count = 1
    while top % p == 0 :
      count += 1
      top /= p
    ret *= count
    if p > top :
      break
  return ret

def divisors(n) :
	ret = []
	for f in xrange(1,int(sqrt(n))+1) :
		if n % f == 0:
			ret.extend([f,n/f])
	return set(ret)

def propDivisors(n) :
	ret = []
	for f in xrange(1,int(sqrt(n))+1) :
		if n % f == 0:
			if n == f*f :
				ret.append(f)
			else:
				ret.extend([f,n/f])
	return ret

def phi(n, primes=[]) :
	facts = primeFactorize(n, primes)
	if len(facts) == 1:
		return n - 1
	return n * reduce(lambda x,y:x*y, [float(fact - 1)/fact for fact in set(facts)])

#------------------------CLASSES----------------------

class SortedList (list) :
	def __contains__ (self, y) :
		if len(self) == 0 :
			return False
		if len(self) == 1:
			if self[0] == y :
				return True
			else :
				return False
		it = self[len(self)/2]
		if it == y :
			return True
		else :
			if it > y :
				return y in self[:len(self)/2]
			else :
				return y in self[len(self)/2:]

class PrimeSet(set) :
	def __init__ (self, n) :
		if n % 2 == 0 :
			self.cap = n
		else :
			self.cap = n + 1
		if n < 2:
			list.__init__(self,[])
			return
	  	if n == 2:
	  		list.__init__(self,[2])
	  		return
	  	# do only odd numbers starting at 3
	  	s = range(3, n, 2)
	  	# n**0.5 may be slightly faster than math.sqrt(n)
	  	mroot = n ** 0.5
	  	half = len(s)
	  	i = 0
	  	m = 3
	  	while m <= mroot:
			if s[i]:
		  		j = (m * m - 3)//2
		  		while j < half:
					s[j] = 0
					j += m
			i = i + 1
			m = 2 * i + 3
	  	# make exception for 2
		set.__init__(self, [2]+[x for x in s if x])
	
	def extend(self, n) :
		if n <= self.cap :
			return
		s = range(self.cap+1, n, 2)
	  	# n**0.5 may be slightly faster than math.sqrt(n)
	  	for p in self[1:] :
	  		if (p - (self.cap+1) % p) % 2 == 0 :
	  			curr = (p - (self.cap+1) % p) /2
	  		else :
	  			curr = (2*p - (self.cap+1) % p)/2
	  		while curr < len(s) :
	  			s[curr] = 0
	  			curr += p
	  	mroot = n ** 0.5
	  	i = 0
	  	m = self.cap+1
	  	half = (n-(self.cap+1))/2
	  	while m <= mroot:
			if s[i]:
		  		j = (m * m - (self.cap+1))//2
		  		while j < half:
					s[j] = 0
					j += m
			i = i + 1
			m = 2 * i + self.cap+1
		set.update(self, [x for x in s if x])
	
class PrimeDict(dict) :
	def __init__ (self, n) :
		if n % 2 == 0 :
			self.cap = n
		else :
			self.cap = n + 1
		d = {2:True}
		if n < 2:
			dict.__init__(self,{})
			return
	  	if n == 2:
	  		dict.__init__(self,d)
	  		return
	  	# do only odd numbers starting at 3
	  	s = range(3, n, 2)
	  	# n**0.5 may be slightly faster than math.sqrt(n)
	  	mroot = n ** 0.5
	  	half = len(s)
	  	i = 0
	  	m = 3
	  	while m <= mroot:
			if s[i]:
		  		j = (m * m - 3)//2
		  		while j < half:
					s[j] = 0
					j += m
			i = i + 1
			m = 2 * i + 3
		for i in s :
			if i :
				d[i] = True
		dict.__init__(self, d)
	
	def extend(self, n) :
		if n <= self.cap :
			return
		s = range(self.cap+1, n, 2)
	  	# n**0.5 may be slightly faster than math.sqrt(n)
	  	for p in self.keys() :
	  		if p == 2:
	  			continue
	  		if (p - (self.cap+1) % p) % 2 == 0 :
	  			curr = (p - (self.cap+1) % p) /2
	  		else :
	  			curr = (2*p - (self.cap+1) % p)/2
	  		while curr < len(s) :
	  			s[curr] = 0
	  			curr += p
	  	mroot = n ** 0.5
	  	i = 0
	  	m = self.cap+1
	  	half = (n-(self.cap+1))/2
	  	while m <= mroot:
			if s[i]:
		  		j = (m * m - (self.cap+1))//2
		  		while j < half:
					s[j] = 0
					j += m
			i = i + 1
			m = 2 * i + self.cap+1
		for i in s :
			if i :
				self[i] = True

class PrimeList(SortedList) :
	def __init__ (self, n) :
		if n % 2 == 0 :
			self.cap = n
		else :
			self.cap = n + 1
		if n < 2:
			list.__init__(self,[])
			return
	  	if n == 2:
	  		list.__init__(self,[2])
	  		return
	  	# do only odd numbers starting at 3
	  	s = range(3, n, 2)
	  	# n**0.5 may be slightly faster than math.sqrt(n)
	  	mroot = n ** 0.5
	  	half = len(s)
	  	i = 0
	  	m = 3
	  	while m <= mroot:
			if s[i]:
		  		j = (m * m - 3)//2
		  		while j < half:
					s[j] = 0
					j += m
			i = i + 1
			m = 2 * i + 3
	  	# make exception for 2
		list.__init__(self, [2]+[x for x in s if x])
	
	def extend(self, n) :
		if n <= self.cap :
			return
		s = range(self.cap+1, n, 2)
	  	# n**0.5 may be slightly faster than math.sqrt(n)
	  	for p in self[1:] :
	  		if (p - (self.cap+1) % p) % 2 == 0 :
	  			curr = (p - (self.cap+1) % p) /2
	  		else :
	  			curr = (2*p - (self.cap+1) % p)/2
	  		while curr < len(s) :
	  			s[curr] = 0
	  			curr += p
	  	mroot = n ** 0.5
	  	i = 0
	  	m = self.cap+1
	  	half = (n-(self.cap+1))/2
	  	while m <= mroot:
			if s[i]:
		  		j = (m * m - (self.cap+1))//2
		  		while j < half:
					s[j] = 0
					j += m
			i = i + 1
			m = 2 * i + self.cap+1
		list.extend(self, [x for x in s if x])
