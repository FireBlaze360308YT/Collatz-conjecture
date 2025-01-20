import os
from math import floor

# Fixed range constants
FIXED_RANGE_END = 1000
FIXED_RANGE_START = 2
FIXED_STEPS = 1

# Used to clean the command line
clear = lambda: os.system('cls')

# List to track numbers that don't fall back to 1
error = [1]


# The Collatz calculator function
def colatz_calculator(start, finish, steps=1):
    for i in range(start, finish + 1, steps):
        print(f"The initial value of i is {i}.")
        error.append(i)
        x = 1
        seen = set()
        while i != 1 and x == 1:
            if i % 2 == 0:
                i //= 2
                print(f"The value of i is {i}")
                if i in seen:
                    return "An error has occurred!"
                seen.add(i)
            else:
                i = i * 3 + 1
                print(f"The value of i is {i}")
                if i in seen:
                    return "An error has occurred!"
                seen.add(i)
        print(f"Ending value of i is {i}")
        seen.clear()


# Function to handle user selection
def selection():
    while True:
        clear()
        first_choice = input(
            "Enter 1 for fixed range, 2 for custom range, or 3 for a singular number (q to quit): ").lower()

        if first_choice == "q" or first_choice == "":
            break

        try:
            first_choice = int(first_choice)
            if first_choice == 1:
                result = colatz_calculator(FIXED_RANGE_START, FIXED_RANGE_END, FIXED_STEPS)
                if result == "An error has occurred!":
                    print(f"{result} with the number {error[1]}")
                break
            elif first_choice == 2:
                while True:
                    second_choice = input("Enter an integer value greater than 1 to set the range end: ")
                    try:
                        second_choice = abs(floor(int(second_choice)))
                        if second_choice <= 1:
                            print("The range must be greater than 1.")
                        else:
                            result = colatz_calculator(FIXED_RANGE_START, second_choice, FIXED_STEPS)
                            if result == "An error has occurred!":
                                print(f"{result} with the number {error[1]}")
                            break
                    except ValueError:
                        print("Only integer positive values allowed!")
            elif first_choice == 3:
                while True:
                    third_choice = input("Enter the number you want to test: ")
                    try:
                        third_choice = abs(floor(int(third_choice)))
                        if third_choice <= 1:
                            print("The number must be greater than 1.")
                        else:
                            result = colatz_calculator(third_choice, third_choice)
                            if result == "An error has occurred!":
                                print(f"{result} with the number {error[1]}")
                            break
                    except ValueError:
                        print("The number must be a positive integer.")
            else:
                print("Please enter 1, 2, or 3.")
        except ValueError:
            print("Invalid input. Please enter 1, 2, 3, or 'q' to quit.")


# Main function to start the program
def main():
    selection()


# Start the program
main()
