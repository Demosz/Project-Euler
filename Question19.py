#19. Counting Sundays
"""
You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""
"""
January=31
February=28
March=31
April=30
May=31
June=30
July=31
August=31
September=30
October = 31
November=30
December=31
"""
#  print 4*30+7*31+28 (Formula for days in a typical year)
# print 4*30+7*31+29 (Formula for days in a leap year)
# print (Number of days since 1900)%7 (Formula for what day the year started)

#This function determines if a year is indeed a leap year
def isLeapYear(year):
    if year % 400 ==0:
        return True
    elif year % 4 == 0 and year % 100 != 0:
        return True
    return False

#This function returns an array of years since 1900, starting with 1900
def yearsSince(year):
    years = []
    for i in range(1900, year+1):
        years.append(i)
    return years

#This function determines on what day the Year starts, and returns a modifier
def yearDayStart(year):
    total = 0
    yearCount = yearsSince(year)
    for i in yearCount:
        if isLeapYear(i):
            total += 366
        else:
            total += 365
    return total % 7

#This function returns an array with the number of days between months.
def dayArray(year):
    if isLeapYear(year):
        return [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30]
    else:
        return [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30 ]

#This function counts how many firsts fall on a Sunday in a year.
def howManyFirsts(year):
    sunCount = 0
    dayCount = 0
    dayList = dayArray(year)
    dayMod = yearDayStart(year)
    if dayMod ==6:
        sunCount += 1
    dayCount += dayMod
    for i in dayList:
        dayCount += i
        if dayCount % 7 == 0:
            sunCount +=1
    return sunCount

#This final function applies the previous function to every year since 1900 to the entered year.
def yearCount(finalYear):
    firsts = 0
    for i in range(1901, finalYear):
        firsts += howManyFirsts(i)
    return firsts

print yearCount(2001)