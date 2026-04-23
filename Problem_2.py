total = 0 

while total<=5000:
    price = int(input("Enter your item price: "))
    total = total +price

    if total > 5000:
        break

if total <=5000:
    print("Within Budget")
else:
    print("Budget exceeded")