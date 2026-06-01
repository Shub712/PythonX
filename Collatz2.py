def collatz(number):
    
    while number != 1:
        
        if number %2 == 0:
            number = number // 2
            
        else:
            number = 3 * number + 1
            
        print(number)
        
def main():
    
    value = int(input("Enter number: "))
    collatz(value)
    
if __name__ == "__main__":
    main()