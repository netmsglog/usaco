"""
ID: yscript1
LANG: PYTHON3
TASK: friday
"""
import sys
def print_err(*args):
    sys.stderr.write(' '.join(map(str,args)) + '\n')

def is_leapyear(year):
    if year % 100 == 0:  # century year
        if year % 400 == 0:
            return True
        else:
            return False
    if year % 4 == 0:
        return True
    return False

def days_of_month(year, month):
    m30 = [9, 4, 6, 11]
    m31 = [1, 3, 5, 7, 8, 10, 12]
    if month in m30:
        return 30
    if month in m31:
        return 31
    isleap = is_leapyear(year)
    if isleap:
        return 29
    return 28

# #test is_leapyear
# tests=[1900, 1700, 1800, 2100, 2000, 1992, 1990]
# for y in tests:
#     print(y, is_leapyear(y))

# #test days_of_month
# print( days_of_month(1900, 2))
# print( days_of_month(2000, 2))
# print( days_of_month(2000, 12))
# print( days_of_month(2000, 7))

fin = open ('friday.in', 'r')
fout = open ('friday.out', 'w')

years = int(fin.readline().strip())
# calculate every day from 1990.1.1 to 1990+years-1.12.31

# 1-Monday  2-Tuesday 3-Wednesday 4-Thursday 5-Friday 6-Saturday 7-Sunday
weekday = 1  # start from Monday (1900-1-1)
nums_of_13 = [ -1, 0, 0, 0, 0, 0, 0, 0]   # used to store sum of 13th weekdays
names_of_weekday = ['null', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

for y in range(years):
    year = 1900 + y
    for m in range(12):
        month = m + 1
        days = days_of_month( year, month)
        for d in range(days):
            date = d + 1
            if date==13:
                #print(year,'-',month,'-',date, names_of_weekday[weekday])
                nums_of_13[weekday] = nums_of_13[weekday] + 1
            # move forward next weekday
            weekday = weekday + 1
            if weekday > 7:
                weekday = 1

seq = [6, 7, 1, 2, 3, 4, 5]
ostr = ''
for s in seq:
    ostr = ostr + str(nums_of_13[s]) + ' '
ostr = ostr.strip()+'\n'
fout.write(ostr)
fout.close()