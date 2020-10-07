def isValid(month: int, day: int, year: int)->bool:
	valid = False
	if isValidMonth(month) == True:
		if isValidDay(month, day, year) == True:
			valid = True
	return valid

def isLeapYear(year: int)->bool:
	valid = False
	if year%4 == 0:
		valid = True
		if year%100 == 0:
			valid = False
			if year%400 == 0:
				valid = True
	return valid

def isValidMonth(month: int)->bool:
	valid = False
	if month > 0 and month < 13:
		valid = True
	return valid

def isValidDay(month: int, day: int, year: int)->bool:
	valid = False
	if month > 0 and month < 13:
		if month == 2:
			if isLeapYear(year) == True:
				if day > 0 and day < 30:
					valid = True
			else:
				if day > 0 and day < 29:
					valid = True
		elif month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
			if day > 0 and day < 32:
				valid = True
		else:
			if day > 0 and day < 31:
				valid = True
	return valid

def getDayOfWeek(month: int, day: int, year: int):
	dayOfWeek = "Error, date is invalid."

	if isValid(month, day, year):
		numOfDays = getDaysFromYear(year)+getDaysFromMonth(month)+day+getNumOfLeapYears(year)+getLeapYearDate(month, day, year)

		if numOfDays%7 == 0:
			dayOfWeek = "Saturday"
		elif numOfDays%7 == 1:
			dayOfWeek = "Sunday"
		elif numOfDays%7 == 2:
			dayOfWeek = "Monday"
		elif numOfDays%7 == 3:
			dayOfWeek = "Tuesday"
		elif numOfDays%7 == 4:
			dayOfWeek = "Wednesday"
		elif numOfDays%7 == 5:
			dayOfWeek = "Thursday"
		elif numOfDays%7 == 6:
			dayOfWeek = "Friday"

	return dayOfWeek

def getDaysFromYear(year: int)->int:
	days = year*365
	return days

def getDaysFromMonth(month: int)->int:
	days = 0

	if month == 1:
		days = 0
	elif month == 2:
		days = 31
	elif month == 3:
		days = 31+28
	elif month == 4:
		days = 31+28+31
	elif month == 5:
		days = 31+28+31+30
	elif month == 6:
		days = 31+28+31+30+31
	elif month == 7:
		days = 31+28+31+30+31+30
	elif month == 8:
		days = 31+28+31+30+31+30+31
	elif month == 9:
		days = 31+28+31+30+31+30+31+31
	elif month == 10:
		days = 31+28+31+30+31+30+31+31+30
	elif month == 11:
		days = 31+28+31+30+31+30+31+31+30+31
	elif month == 12:
		days = 31+28+31+30+31+30+31+31+30+31+30

	return days

def getNumOfLeapYears(year: int)->int:
	num = int(year/4) - int(year/100) + int(year/400)
	return num

def getLeapYearDate(month: int, day: int, year: int)->int:
	num = 0
	if isLeapYear(year) == True:
		if month < 3:
			num = -1;

	return num

def getThanksgivingDate(year: int)->int:
	date = 0
	weekDay = getDayOfWeek(11, 1, year)

	if weekDay == "Sunday":
		date = 26
	elif weekDay == "Monday":
		date = 25
	elif weekDay == "Tuesday":
		date = 24
	elif weekDay == "Wednesday":
		date = 23
	elif weekDay == "Thursday":
		date = 22
	elif weekDay == "Friday":
		date = 28
	elif weekDay == "Saturday":
		date = 27

	return date

