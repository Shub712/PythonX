import sys

while True:
    
    print("type exit to exit")
    
    response = input()
    
    if response == 'exit':
        
        sys.exit()  # we can use sys.exit to stop the program early

    print(f"your response is {response}")