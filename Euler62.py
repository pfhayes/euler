# Find the smallest cube for which 5 permutations of its digits are cubes

perms = {}

from useful import digits

count = 1
while True :
	num = count**3
	cub = digits(num)
	cub.sort()
	cub = tuple(cub)
	l = perms.setdefault(cub,[0,num])
	l[0] += 1
	if l[0] >= 5 :
		print l
		break
	perms[cub] = l
	count += 1
	