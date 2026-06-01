def Display(Value):

    if Value < 0:
        No =  -No 

    for i in range(-Value,Value+1):
        print(i, end  = ' ')

def main():

    No = 0
    print("Enter The Number : ")

    No = int(input())
    Display(No)

if __name__ == "__main__":
    main()