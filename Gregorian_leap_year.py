def is_leap(year):
    leap = False
    if year%400==0:
        leap = True
    elif year%100==0:
        leap = False
    elif year%4==0:
        leap = True
    
    return leap
def input_year():
    while True:
        year =int(input("Enter year :"))
        if 1900 <= year <=(10**10):
            return year
status=is_leap(input_year())
if status == True:
    print("Leap year")
else:
    print("Not Leap year")