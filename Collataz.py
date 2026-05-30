
def collatz(number):
    value = 0
    
    if number % 2 == 0:
        value = number // 2
        return value
    
    else:
        value = 3 * number + 1
        return value
    
def main():
    ret = collatz(3)
    print(ret)
    
if __name__ == "__main__":
    main()