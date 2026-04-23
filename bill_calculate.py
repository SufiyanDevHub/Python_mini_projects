unit = int(input("Enter your units: "))

if unit <=100:
    bill = 0
    print(f"No Charge Fee,Your bill is {bill}")
elif  unit<=200:
    bill = (unit-100)*5
    print(f"5 rupees per unit,Your bill is {bill}")
else:
    bill = 500 + (unit-200)*10
    print(f"10 rupees per unit,Your bill is {bill}")