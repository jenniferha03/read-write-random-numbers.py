"""
average_steps_taken.py
Name: Khue (Jennifer) Ha
"""


import sys


def average_steps(file_object, num_days):
    """
    Accepts two arguments: the file object containing the steps and
    the number of days to read from the file.
    Returns the average of the number of steps read.
    """
    month = 0
    monthly_steps = 0
    average = 0
    for _ in range(num_days):
        try:
            steps = int(file_object.readline())
            month += 1
            monthly_steps += steps
            average = monthly_steps / num_days
        except ValueError as err:
            print("The program has aborted because the steps file contains invalid data.")
            print(err)
            sys.exit()
    return average


def open_input_file():
    """
    Prompts the user for the name of the file and opens it.
    If the file name entered is not found, the user should be prompted until
    they enter a file name of a file that exists.
    """
    file_object = None
    file_name = None
    while file_object is None:
        try:
            file_name = input("Enter the name of the input file: ")
            file_object = open(file_name, 'r', encoding="utf8")
        except FileNotFoundError:
            print(f'The file "{file_name}" was not found. Check the file name and try again.')
    return file_object


def main():
    """
    Calls the open_input_file function.
    Calls average_steps for each month to get the average steps and
    then prints the average steps for the month on each iteration.
    """
    steps_file = open_input_file()
    january = average_steps(steps_file, 31)
    print(f"The average steps taken in   January was {january: 4,.0f}")
    february = average_steps(steps_file, 28)
    print(f"The average steps taken in  February was {february: 4,.0f}")
    march = average_steps(steps_file, 31)
    print(f"The average steps taken in     March was {march: 4,.0f}")
    april = average_steps(steps_file, 30)
    print(f"The average steps taken in     April was {april: 4,.0f}")
    may = average_steps(steps_file, 31)
    print(f"The average steps taken in       May was {may: 4,.0f}")
    june = average_steps(steps_file, 30)
    print(f"The average steps taken in      June was {june: 4,.0f}")
    july = average_steps(steps_file, 31)
    print(f"The average steps taken in      July was {july: 4,.0f}")
    august = average_steps(steps_file, 31)
    print(f"The average steps taken in    August was {august: 4,.0f}")
    september = average_steps(steps_file, 30)
    print(f"The average steps taken in September was {september: 4,.0f}")
    october = average_steps(steps_file, 31)
    print(f"The average steps taken in   October was {october: 4,.0f}")
    november = average_steps(steps_file, 30)
    print(f"The average steps taken in  November was {november: 4,.0f}")
    december = average_steps(steps_file, 31)
    print(f"The average steps taken in  December was {december: 4,.0f}")
    steps_file.close()


if __name__ == '__main__':
    main()
