def is_year_leap(year):
   if year %400 ==0 or year %100==0 and year %4 ==0:
     print(True,":","is a leap year")
   else:
    print(False,":",year,"not a leap year")
year = int(input("please enter a year"))
is_year_leap(year)