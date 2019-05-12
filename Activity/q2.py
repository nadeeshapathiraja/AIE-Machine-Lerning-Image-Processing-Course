Tyear=eval(input("Enter Today Year: "))
Tmonth=eval(input("Enter Today Month: "))
Tdate=eval(input("Enter Today date: "))

dobyear=eval(input("Enter DOB Year: "))
dobmonth=eval(input("Enter DOB Month: "))
dobdate=eval(input("Enter DOB date: "))

year=o
month=0
date=0

if (Tmonth<dobmonth):
    year=Tyear-1
    month=month+12-dobmonth
    

print("Your Age: Yaer-",(Tyear-dobyear)," Months-",(Tmont-dobmonth)," Dates-",(Tdate-dobdatedobdate))
