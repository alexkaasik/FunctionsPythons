import math
import datetime
from readline import write_history_file

#1
def calc(n1:float, n2:float, mode:str):
    if ((n1 == 0 or n2 == 0) and mode == "/"):
        answer = "error"
    elif mode == "+":
        answer = n1 + n2
    elif mode == "-":
        answer = n1 - n2
    elif mode == "*":
        answer = n1 * n2
    elif mode == "/":
        answer = n1 / n2
    else:
        answer = "uknown answer"

    return answer

#2
def is_year_leap(year):
    if year.isdigit() and year%4 == 0:
        print("TRUE")
    else:
        print("FALSE")

#3
def square(sq):
    if type(sq) == float or type(sq) == int:
        print(f"периметр {sq*2}")
        print(f"площадь {sq**2}")
        print(f"диагональ { round(math.sqrt(sq**2 + sq**2),2) }")
    else:
        print("error")

#4
def seasons(number: int):
    if 0 <= number < 3:
        print("kevad")
    elif 3 <= number < 6:
        print("suvi")
    elif 6 <= number < 9:
        print("sügis")
    elif 9 <= number < 12:
        print("talv")
    else:
        print("error")

#5
def Bank(years:int , money:float, p:float):
    for x in range(years):
        money += (money * p)
        print(f"{x+1} year = { round(money,2) }")
    return round(money,2)

#6
def is_prime(number: int):

    if number > 1:
        for i in range(2, int(number/2)+1):
            if (number % i) == 0:
                print(f"{number} = false")
                break
        else:
            print(f"{number} = true")
    else:
        print(f"{number} = false")

#7
def isCalendar(Day:int, Month:int, Year:int ):
    try:
        datetime.date(Year, Month, Day)
        CheckDate = True
    except:
        CheckDate = False

    if CheckDate == True:
        print("exits")
    else:
        print("fake date")

#8

print("----- 1 -----\n")

while(True):
    try:
        Number1 = float(input("N1: "))
        break
    except:
        pass

while(True):
    try:
        Number2 = float(input("N2: "))
        break
    except:
        pass

Mode = str(input("mode: "))

test = calc(Number1, Number2, Mode)

print(f"answer = {test}")

print("\n----- 2 -----\n")
WhatYear=input("year: ")
is_year_leap(WhatYear)

print("\n----- 3 -----\n")

WhatSquare=input("Square: ")
square(WhatSquare)

print("\n----- 4 -----\n")

WhatSeasons=int(input("1-12: "))-1
seasons(WhatSeasons)

print("\n----- 5 -----\n")

while(True):
    try:
        WhatYear=int(input("Year: "))
        break
    except:
        pass

while(True):
    try:
        HowMuch=float(input("money: "))
        break
    except:
        pass

per=float(10/100)

doneBank = Bank(WhatYear,HowMuch,per)
print(f"You will get {doneBank} after {WhatYear} years")

print("\n----- 6 -----\n")

for x in range(1001):
    is_prime(x)

print("\n----- 7 -----\n")

while(True):
    try:
        WhatDay=int(input("Day: "))
        break
    except:
        pass

while(True):
    try:
        WhatMonth=int(input("Month: "))
        break
    except:
        pass

while(True):
    try:
        WhatYear=int(input("Year: "))
        break
    except:
        pass

isCalendar(WhatDay,WhatMonth,WhatYear)

print("\n----- 8 -----\n")
