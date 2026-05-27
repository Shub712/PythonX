while True:
    
    print("Who are you?")
    
    name = input()
    
    if name != "Shubham":
        continue
    
    print("Hello Shubham, What is the password ? (It is a fish)")
    
    password = input()
    
    if password == "Ravas":
        break
    
    else:
        print("Incorrect password")
    
print("Access granted")