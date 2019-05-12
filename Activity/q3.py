unit=eval(input("Enter Number of Units: "))
if(unit>0 and unit<30):
    print("Charge = ",unit*5)
if(unit>=30 and unit<60):
    print("Charge = ",30*5+(unit-30)*20)
if(unit>=60 and unit<120):
    print("Charge = ",30*5+(unit-30)*20+(unit-60)*150)
if(unit>=120 and unit<200):
    print("Charge = ",30*5+(unit-30)*20+(unit-60)*150+(unit-120)*500)
else:
    print("Charge = ",30*5+(unit-30)*20+(unit-60)*150+(unit-120)*500+(unit-200)*1000)
    
