import os
import time
import threading
from math import floor
from typing import Tuple, Callable, Optional, List
from queue import Queue
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

# Constants for range limits and file names
FIXED_RANGE_START: int = 2
FIXED_RANGE_END: int = 1000
FIXED_STEPS: int = 1
LOG_FILE: str = "collatz_log.txt"
MAX_WORKERS: int = 8  # Increased to scale further

# Clear screen function (cross-platform)
clear: Callable[[], None] = lambda: os.system('cls' if os.name == 'nt' else 'clear')

# Logger function to centralize output and save logs to a file
def logger(message: str, to_file: bool = True) -> None:
    """
    Logs messages to both the console and a log file.
    Efficient logging with timestamp and color for better visibility.
    
    :param message: The message to log.
    :param to_file: Whether to also write the log to a file.
    """
    print(f"\033[1;32m{message}\033[0m")  # Green text for visibility
    if to_file:
        with open(LOG_FILE, "a") as log_file:
            log_file.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - {message}\n")

# Helper function to validate positive integers
def validate_positive_integer(value: str) -> Optional[int]:
    """
    Validates if the input is a positive integer greater than 1.
    
    :param value: The input string to validate.
    :return: The validated positive integer or None if invalid.
    """
    try:
        num: int = abs(floor(int(value)))
        if num <= 1:
            raise ValueError("Input must be greater than 1.")
        return num
    except ValueError as e:
        logger(f"Error: {str(e)}")
        return None

# Function to handle the Collatz sequence calculation with cycle detection
def collatz_sequence(start: int) -> Tuple[int, bool]:
    """
    Calculate the Collatz sequence for a given starting number.
    Checks for cycles during the calculation to prevent infinite loops.
    
    :param start: The starting integer for the Collatz sequence.
    :return: A tuple of the final number and a boolean indicating if a cycle was detected.
    """
    visited = set()  # Set to track numbers and detect cycles
    steps = 0  # Track the number of steps taken to reach 1
    
    while start != 1:
        if start in visited:  # Cycle detected
            logger(f"Cycle detected with starting value {start}. Exiting.")
            return start, True
        visited.add(start)
        start = start // 2 if start % 2 == 0 else 3 * start + 1
        steps += 1
        logger(f"Step {steps}: {start}")

    return start, False  # Reached 1, no cycle detected

# Function for handling ranges and steps with multi-threading or multiprocessing
def calculate_collatz_in_range(start: int, end: int, step: int = 1, use_multiprocessing: bool = False) -> None:
    """
    Process the Collatz sequence for each number in the specified range using multi-threading or multiprocessing.
    
    :param start: The starting number for the range.
    :param end: The ending number for the range.
    :param step: The step size between numbers in the range (default is 1).
    :param use_multiprocessing: Flag to switch between multi-threading and multi-processing (default is False).
    """
    # Use multiprocessing for better performance with large ranges
    if use_multiprocessing:
        with ProcessPoolExecutor(max_workers=MAX_WORKERS) as executor:
            results = executor.map(collatz_sequence, range(start, end + 1, step))
            for result in results:
                pass  # Just processing results, no need for logging here
    else:
        queue = Queue()  # Queue to manage the numbers for processing
        with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
            for num in range(start, end + 1, step):
                queue.put(num)  # Add number to queue
                executor.submit(process_number, queue)  # Process number in a separate thread
            executor.shutdown(wait=True)  # Wait for all threads to finish

# Function to process an individual number and log the result
def process_number(queue: Queue) -> None:
    """
    Processes an individual number, computes its Collatz sequence, and logs the result.
    
    :param queue: The queue holding the numbers to be processed.
    """
    num = queue.get()  # Get the number to process from the queue
    logger(f"Processing number: {num}")
    _, error_detected = collatz_sequence(num)  # Calculate the Collatz sequence
    if error_detected:  # If a cycle is detected, log the result
        logger(f"Cycle detected for number {num}!")
    queue.task_done()  # Mark the task as done

# Function to handle the selection of range inputs from the user
def get_user_range_input() -> Tuple[int, int]:
    """
    Prompts the user for a valid range end input.
    
    :return: A tuple containing the start and end of the range.
    """
    while True:
        range_end_input = input("Enter a positive integer greater than 1 for the range end: ").strip()
        end_value = validate_positive_integer(range_end_input)  # Validate input
        if end_value:  # If the input is valid, return the range
            return FIXED_RANGE_START, end_value

# Function to handle Collatz sequence calculation for a singular number input
def get_user_number_input() -> int:
    """
    Prompts the user for a valid number input to test.
    
    :return: The validated number to test.
    """
    while True:
        number_input = input("Enter the number you want to test: ").strip()
        number = validate_positive_integer(number_input)  # Validate input
        if number:  # If the input is valid, return the number
            return number

# Display available options to the user
def display_main_menu() -> str:
    """
    Displays the main menu and prompts the user for their selection.
    
    :return: The user's selected option.
    """
    clear()  # Clear the console for a clean display
    print("""
    Collatz Sequence Tester
    =======================
    1. Fixed Range (2 to 1000)
    2. Custom Range
    3. Single Number Test
    4. Custom Range with Multiprocessing
    q. Quit
    """)
    return input("Please choose an option (1/2/3/4/q): ").strip().lower()

# Main function to handle user flow and logic
def main() -> None:
    """
    Main entry point for the user interaction. Handles the logic flow based on the user's choice.
    """
    logger("Collatz Sequence Tester started.", to_file=False)
    while True:
        user_choice = display_main_menu()  # Display the main menu and get the user's choice

        # Exit the program
        if user_choice == 'q':
            logger("Exiting the program. Goodbye!")
            break
        
        # Process for fixed range
        elif user_choice == '1':
            logger(f"Processing Collatz sequence for range {FIXED_RANGE_START} to {FIXED_RANGE_END}.")
            calculate_collatz_in_range(FIXED_RANGE_START, FIXED_RANGE_END, FIXED_STEPS)
        
        # Process for custom range
        elif user_choice == '2':
            start, end = get_user_range_input()  # Get custom range from user
            logger(f"Processing Collatz sequence for range {start} to {end}.")
            calculate_collatz_in_range(start, end)
        
        # Process for a single number
        elif user_choice == '3':
            number = get_user_number_input()  # Get a single number from user
            logger(f"Processing Collatz sequence for number {number}.")
            _, error_detected = collatz_sequence(number)  # Calculate the sequence
            if error_detected:
                logger("Cycle detected!")
        
        # Process for custom range with multiprocessing
        elif user_choice == '4':
            start, end = get_user_range_input()  # Get custom range from user
            logger(f"Processing Collatz sequence for range {start} to {end} using multiprocessing.")
            calculate_collatz_in_range(start, end, use_multiprocessing=True)
        
        # Handle invalid input
        else:
            logger("Invalid input! Please select 1, 2, 3, 4, or 'q' to quit.")

# Run the program if this is the main module
if __name__ == "__main__":
    main()  # Call the main function to start the program

