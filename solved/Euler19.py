# Find the number of Sundays between Jan 1, 1901 and Dec 31, 2000

year = 1901 # Jan 1st, 1901 was a Monday
month = 1
day = 7		# So we start on Sunday, Jan 7th, 1901

def daysInCurrMonth() :
	if month in [4,6,9,11] :
		return 30
	elif month is 2 :
		if year % 4 is 0 :
			return 29
		else :
			return 28
	else :
		return 31

count = 0
while year < 2001 :
	if day is 1:
		count += 1
	day += 7
	dICM = daysInCurrMonth()
	if day > dICM :
		day -= dICM
		month += 1
		if month > 12 :
			month -= 12
			year += 1
		
print count