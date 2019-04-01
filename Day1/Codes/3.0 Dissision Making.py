marks=eval(input("Enter Your marks: "))
grade=''
if(marks<35):
    grade='F'
    

elif(marks<45):
    grade='S'

elif(marks<60):
    grade='C'

elif(marks<75):
    grade='B'

else:
    grade='A'
    
print("Your Grade",grade)
