def collatz_calculator(start=2, finish=1000, steps=1) -> None:
    for i in range(start, finish + 1, steps):
        print(f"The initial value of i is {i}.")
        while i != 1:
            if not i % 2:
                i //= 2
                print(f"The value of i is {i}")
            else:
                i = i * 3 + 1
                print(f"The value of i is {i}")
        print(f"Ending value of i is {i}")
    exit()

def selection():
    while True:
        game_mode = input("Enter:\n1 for fixed mode\n2 for custom mode\n3 for singular number\nq to quit\n>>> ").lower().strip()

        if game_mode == "q" or not game_mode:
            break

        try:
            game_mode = abs(int(game_mode))
            if game_mode == 1:
                collatz_calculator()
            if game_mode == 2:
                while True:
                    second_choice = input("Enter range end\n>>> ")
                    try:
                        second_choice = abs(int(second_choice))
                        collatz_calculator(finish=second_choice)
                    except ValueError:
                        print("Only integer positive values allowed!")
            if game_mode == 3:
                while True:
                    third_choice = input("Enter the number you want to test: ")
                    try:
                        third_choice = abs(int(third_choice))
                        if third_choice <= 1:
                            print("The number must be greater than 1.")
                        else:
                            collatz_calculator(third_choice, third_choice)
                    except ValueError:
                        print("The number must be a positive integer.")
            else:
                print("Please enter 1, 2, or 3.")
        except ValueError:
            print("Invalid input. Please enter 1, 2, or 'q' to quit.")

# Main function to start the program
def main():
    selection()


# Start the program
if __name__ == '__main__':
    main()
