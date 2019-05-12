while(input("Enter Student Index:")):
    marks=eval(input("Enter your Marks:"))
    if(marks>=0 and marks<100):
        if(marks>0 and marks<30):
            print("Student Is FAIL, Student Grade D-")
        if(marks>30 and marks<35):
            print("Student Is FAIL, Student Grade D")
        if(marks>=35 and marks<40):
            print("Student Is FAIL, Student Grade D+")
        if(marks>=40 and marks<45):
            print("Student Is FAIL, Student Grade C-")
        if(marks>=45 and marks<50):
            print("Student Is PASS, Student Grade C")
        if(marks>=55 and marks<60):
            print("Student Is PASS, Student Grade C+")
        if(marks>=60 and marks<65):
            print("Student Is PASS, Student Grade B-")
        if(marks>=65 and marks<70):
            print("Student Is PASS, Student Grade B")
        if(marks>=70 and marks<75):
            print("Student Is PASS, Student Grade B+")
        if(marks>=75 and marks<80):
            print("Student Is PASS, Student Grade A-")
        if(marks>=80 and marks<90):
            print("Student Is PASS, Student Grade A")
        if(marks>=90 and marks<=100):
            print("Student Is PASS, Student Grade A+")
    else:
        print("ERROR! Please enter a numerical value between 0 to 100")
