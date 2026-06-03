import random
import time
from tqdm import tqdm

import tkinter as tk

root = tk.Tk()
root.title("Number Guessing Game")
root.geometry(400*300)

def Checkguess():
    
    print("="*46)
    print("------ Welcome To Number Guessing Game  ------")
    print("--------- It's an single player game ---------")
    print("="*46)
        
    print("="*46)
    print("Please difficulty level: ")
    print("Press 1 for : Easy")
    print("Press 2 for : Medium")
    print("Press 3 for : Hard")
    print("="*46)
    
    difficulty = int(input("Enter Difficulty:"))
    
    
    value1 = 1
    value2 = None
    
    if difficulty == 1:
        value2 = 100
        
    elif difficulty == 2:
        value2 = 500
        
    elif difficulty == 3:
        value2 = 1000
    else:
        print("Please select correct difficulty")

        
    start = (input("\nPress R to start the game ->"))
    
    start = start.lower()
    
    if start == "r":
         
        for i in tqdm(range(100),desc="Loading",unit="it"):
            time.sleep(0.05)
            
        number = random.randint(value1,value2)
        attempts = 0
        
        while True:
            try:
                guess = int(input("\nEnter Guess : "))
                attempts = attempts + 1
                distance = abs(guess - number)

                if guess < number :
                    print("Number is Higher...")
                    print(f"Attempt {attempts}")
            
                elif guess > number:
                    print("Number is Lower...")
                    print(f"Attempt {attempts}")
            
                elif(guess == number):
                    print("🏆 You Have Guessed it successfully!!!")
                    print(f"Total attempts: {attempts}")
                    break
                
                #=========== HINT SECTION ===============
                
                if distance <=10:
                    print("🔥 Very Very Close!")
                    
                elif distance <=50:
                    print("🙂 Close!")
                    
                elif distance <=100:
                    print("😐 Far!")
                    
                else:
                    print("🥶 Too Far Away!")
                
            except ValueError as e :
                print("Please enter numbers only")
                print(e)
            
if __name__ == "__main__":
    Checkguess()