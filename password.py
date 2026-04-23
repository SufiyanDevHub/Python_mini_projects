password = "python123"

# attempt = 0
for i in range(3,0,-1):
    user_password = input("Enter your password: ")
    if password == user_password:
        print("Access Granted")
        break
    else:   
        if i-1>0:
            print(f"Try again! Your attempt left {i-1}")
        else:
            print("No more attempts")    
        
if password!=user_password:        
    print("You can try again after 1 hour")