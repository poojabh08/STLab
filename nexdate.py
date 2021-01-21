def isleap(year):
    if (year % 4) == 0:  
        if (year % 100) == 0:  
            if (year % 400) == 0:  
                return True
            else:  
                return False
        else:
            return True  
    else:  
        return False

l=[]
d=int(input("Enter date: "))
l.append(d)
m=int(input("Enter month: "))
l.append(m)
y= int(input("Enter year: "))
l.append(y)
year=l[2]  
if l[2]<1812 or l[2]>2014 or l[1]>12 or l[1]<1 or l[0]>31 or l[0]<1:
    print("Boundary limit reached")
else:
    y=isleap(year)
    month = l[1]
    if month in (1, 3, 5, 7, 8, 10, 12):
        month_length = 31
    elif month == 2:
        if y:
            month_length = 29
        else:
            month_length = 28
    else:
        month_length = 30
    day = l[0]
    if day < month_length:
        day += 1
    else:
        day = 1
        if month == 12:
            month = 1
            year += 1
        else:
            month += 1
    print("Next date is {}-{}-{}".format(day,month,year))