def leapyear(year):
    return (year%4==0 and year%100!=0) or (year%400==0)
year=int(input('enter a year: '))    
print('leap year' if leapyear(year) else 'not')