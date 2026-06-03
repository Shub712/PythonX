def main():
    
    name = ''
    
    name = input("Enter Your Name :") 
    
    while True:
        
        print(f"Agent : Hi {name}")
        Agent = input("How can i help you ? ")
        
        if Agent == "Bye":
            print("Thank you visit again")
            break


if __name__ == "__main__":
    main()