year = int(input("enter the year: "))
if year % 4 == 0:
    if year % 100 != 0:
        print("it is leap year")
    else:
         print("it is not leap year")
else:
     print("it is not leap year")
      
