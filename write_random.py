"""
write_random.py

"""

import random


def get_number():
    """
    Prompts user to input the number and validates the input entered.
    Returns the number that user entered.
    """
    user_input = None
    while user_input is None:
        user_input = input("How many random numbers do you want to write to the output file? ")
        try:
            user_input = int(user_input)
        except ValueError:
            user_input = None
            print("Enter a positive integer value.")
            print('')
        else:
            if user_input <= 0:
                user_input = None
                print("Enter a positive integer value.")
                print('')
    return user_input


def write_numbers(file_name, count):
    """
    Takes two arguments are the file name and the count as the number entered by user.
    Generates random numbers to write to the file.
    """
    with open(file_name, 'w', encoding="utf8") as file_object:
        for _ in range(1, count + 1):
            steps = random.randint(100, 15000)
            file_object.write(f"{steps}\n")
    file_object.close()


def read_numbers(file_name):
    """
    Takes the file name as the argument and prints the count, total, and average of numbers.
    """
    total = 0
    days = 0
    average = 0
    with open(file_name, 'r', encoding="utf8") as file_object:
        for line in file_object:
            steps = int(line)
            days += 1
            total += steps
            average = total / days
    file_object.close()
    print(f"  Count: {days}")
    print(f"  Total: {total}")
    print(f"Average: {average:.2f}")


def main():
    """
    Call get_number function and prompts user to input the file name
    Runs the program by calling write_numbers and read_numbers functions.
    """
    count = get_number()
    file_name = input("Enter the name of the output file: ")
    write_numbers(file_name, count)
    read_numbers(file_name)


if __name__ == '__main__':
    main()

    
    
    
    
    
