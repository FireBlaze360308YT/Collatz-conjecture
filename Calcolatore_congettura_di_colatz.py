# Hello, I'm a novice python programmer, I'm learning python so don't expect nothing complex yet.
# I'm fascinated by math in general and i like the colatz conjecture, so i wanted to make a calculator.
# It's a simple program to test myself, it wont be used by scientist to test if the colatz conjecture is true or not.
# But if u want to know the colatz conjecture curve of a specified number u can use this!
# I hope u enjoy!

#Updates will come out, this version dates at 14/14/2024

#imports!
import os
from math import *

#Fixed range constant, change this to change the fixed range, this wont be changed in the code tho!
FIXED_RANGE_END :int = 1000
FIXED_RANGE_START :int = 2
FIXED_STEPS :int = 1

#Used to clean the cmd!
clear = lambda: os.system('cls')

#Used to keep track of numbers that don't fall back to 1!
error :list = [1]

#The colatz calculator used the colatz function (search online)!
def colatz_calculator(start :int, finish :int, steps :int = 1) -> str:
    for i in range(start, (finish+1), steps):
        print(f"The initial value of i is {str(i)}.")
        error.append(str(i))
        x = 1
        daje :set = {0}
        while i != 1 and x == 1:
            if (i % 2) == 0:
                i = int(i//2)
                print(f"The value of i is {str(i)}")
                if (i in daje) == False:
                    daje.add(i)
                else:
                    return "An error has occurred!"
                continue
            elif (i % 2) != 0:
                i = int((i * 3) + 1)
                print(f"The value of i is {str(i)}") 
                if (i in daje) == False:
                    daje.add(i)
                else: 
                    return "An error has occurred!"
                continue
            else:
                x -= 1
        print(f"Ending value of i is {str(i)}")
        daje.clear()

#This function start the program, it ask the parameters of the program!
def selection() -> None:
    while True:
        clear()
        first_choice = input("Enter 1 for fixed range or 2 for custom range or 3 for a singular number. (q to quit)\n")
        try:
            if first_choice == "q" or first_choice == "Q" or first_choice == "":
                break
            first_choice = int(first_choice)
            if first_choice == 1:
                attempt :str = colatz_calculator(FIXED_RANGE_START, FIXED_RANGE_END, FIXED_STEPS)
                if attempt == "An error has occurred!":
                    print(f"{attempt} with the number {error[1]}")
                break
            elif first_choice == 2:
                while True:
                    second_choice = input("Enter an integer positive value bigger than 1 to be the end of the range!\n")
                    try:
                        second_choice = floor(int(second_choice))
                        if second_choice == 0 or second_choice == 1:
                            print("\nThe range must be more than 1\n")
                            continue
                        elif second_choice < 0:
                            second_choice = second_choice * -1
                            if second_choice == 1:
                                print("\nThe range must be more than 1\n")
                                continue
                            attempt :str = colatz_calculator(FIXED_RANGE_START, second_choice, FIXED_STEPS)
                            if attempt == "An error has occurred!":
                                print(f"{attempt} with the number {error[1]}")
                            break
                        else:
                            attempt :str = colatz_calculator(FIXED_RANGE_START, second_choice, FIXED_STEPS)
                            if attempt == "An error has occurred!":
                                print(f"{attempt} with the number {error[1]}")
                            break
                    except ValueError:
                        print("Only integer positive values allowed!\n")
                        continue      
                break
            elif first_choice == 3:
                while True:
                    third_choice = input("Enter the number u want to test!\n")
                    try:
                        third_choice = floor(int(third_choice))
                        if third_choice == 0 or third_choice == 1:
                            print("\nThe number must be more than 1\n")
                            continue
                        elif third_choice < 0:
                            third_choice = third_choice * -1
                            if third_choice == 1:
                                print("\nThe number must be more than 1\n")
                                continue
                            attempt :str = colatz_calculator(third_choice, third_choice)
                            if attempt == "An error has occurred!":
                                print(f"{attempt} with the number {error[1]}")
                            break
                        else:
                            attempt :str = colatz_calculator(third_choice, third_choice)
                            if attempt == "An error has occurred!":
                                print(f"{attempt} with the number {error[1]}")
                            break
                    except ValueError:
                        print("The number must be a positive integer")
                        continue
            else:
                print("\nEnter either 1 or 2 or 3 to enter!\n")
                continue
        except ValueError:
            print("Enter either 1 or 2 to enter or q to quit, NOTHING ELSE!\n")
            continue
        break

#Main function where everything will be executed!
def main() -> None:
    selection()

#start of the program!
main()
