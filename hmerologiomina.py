import calendar
y = int(input("Input the year : "))

m = 13

while m>12:
	m = int(input("Input the month : "))
	print "error"
print(calendar.month(y, m))