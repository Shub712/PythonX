CheckEven = lambda No : (No % 2 == 0)

Increment = lambda No : No + 1

Add = lambda A,B : A + B

def filterX(Task, Elements):
    Result = list()

    for no in Elements:
        Ret = Task(no)

        if(Ret == True):
            Result.append(no)
    return Result

def mapX(Task, Elements):
    Result = list()

    for no in Elements:
        Ret = Task(no)
        Result.append(no)
    return Result

def reduceX(Task,Elements):
    Sum = 0
    
    for no in Elements:
        Sum  = Task(Sum,no)
    return Sum


def main():

    Data = [10,21,24,38,45,21]
    print("Actual Data is : ", Data)

    FData = list(filterX(CheckEven,Data))
    print("Data after filter : ", FData)

    MData = list (map(Increment,FData))
    print("Data after map : ", MData)

    RData = reduceX(Add,MData)
    print("Data after reduce : ", RData)

if __name__ == "__main__":
    main()