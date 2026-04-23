i = 1
balance = 20000
code = 2580
while i <=3:
    pin_code = int(input("Enter your PIN code: "))

    if code == pin_code:

        amount = int(input("Enter your withdrawl amount"))

        if amount <=balance:
            balance = balance - amount
            print("Transaction Successful!,Remaining balance:",balance)
            break
        else:
            print("Insufficient Balance!")
           


    else:
        print("try Again!,Attempt left",3-i)
    i+=1
else:
    print("Your card has been blocked!")