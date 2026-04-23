import random

rand_num = random.randint(1,100)

guess = int(input("Enter your number: "))
i = 1
while rand_num!=guess:
    if guess<rand_num:
        print("Guess Higher!")
    else:
        print("Guess lower!")
    guess = int(input("Enter your number again: "))
    i+=1    

print("Correct Answer")
print("Total Count",i)