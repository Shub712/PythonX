def DisplayEvenFactor(Value):

    if (Value < 0):
        Value = - Value
    
    for i in range(1,Value):
        if(Value % i ==0) and (i % 2 == 0):
            print(i,end = ' ')

def main():

    No = 0

    print("Enter The Number ; ")
    No = int (input())

    DisplayEvenFactor(No)
    
if __name__ == "__main__":
    main()