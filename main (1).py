# leap year

input_year = int(input("enter the year to check:"))
if(input_year%400 == 0):
      print("%d is a leap year"%input_year)
elif(input_year%100 == 0):
      print("%d is not a leap year"% input_year)
elif(input_year%4 == 0):
      print("%d is a leap year"% input_year)
else:
      print("%d is not a leap year"% input_year)