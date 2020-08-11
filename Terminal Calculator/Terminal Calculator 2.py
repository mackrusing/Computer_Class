# Terminal Calculator 2
# (Orignially Terminal-Arithmetic-Machine-v2)

# Created Feb 18, 2020

# v1.0
# Python 3


import os
import webbrowser


# Terminal Size

columns, lines = os.get_terminal_size()

int(columns)
int(lines)


# Main Menu

def end_menu_line():
    print("#" * columns)


def blank_menu_line():
    spaces_num = (columns - 2)
    spaces = " " * int(spaces_num)
    print("#" + spaces + "#")


def text_menu_line(text):
    # if even
    if (len(text) + columns) % 2 == 0:
        spaces_num = (columns - (len(text) + 2)) / 2
        spaces = " " * int(spaces_num)
        print("#" + spaces + text + spaces + "#")
    # if odd
    else:
        spaces_num1 = (columns - (len(text) + 2)) / 2 + 1
        spaces_num2 = ((columns - (len(text) + 2)) / 2)
        spaces1 = " " * int(spaces_num1)
        spaces2 = " " * int(spaces_num2)
        print("#" + spaces1 + text + spaces2 + "#")


# Blank line (not menu)

def blank():
    print(" ")


# At Start

def start():

    os.system("clear")

    end_menu_line()
    blank_menu_line()
    text_menu_line("help")
    blank_menu_line()
    text_menu_line("github")
    blank_menu_line()
    text_menu_line("exit")
    blank_menu_line()
    end_menu_line()
    input_function()

    # not sure what this does, so I took it out
    # os.system("clear")


def input_function():
    user_input = input(">> ")

    # 2 Number Expression
    try:
        num1, operator, num2 = user_input.split()
        num1 = int(num1)
        num2 = int(num2)
        calculate(operator, num1, num2)

    # Other Commands
    except ValueError:

        # Help Menu
        if user_input.lower() == "help":
            blank()
            print("------ Help Menu ------")
            blank()
            print("Input equation like so:")
            print("a + b")
            blank()
            print("Addition = +")
            print("Subtraction = -")
            print("Multiplication = *")
            print("Division = /")
            blank()
            input_function()

        # GitHub Command
    elif user_input.lower() == "github":
            webbrowser.open("https://github.com/mackrusing/computer-class/tree/master/Terminal%20Calculator")
            input_function()

        # Exit Command
        elif user_input.lower() == "exit":
            os.system('clear')
            exit(0)

        # Test Command
        elif user_input == "test":
            webbrowser.open("http://www.mackrusing.com")

        # Invalid Input
        else:
            blank()
            print(f"\'{user_input}\' is an invalid input.")
            blank()
            input_function()


# Calculate Answer

def calculate(operator, num1, num2):
    if operator == "+":
        blank()
        print(f"{num1} + {num2} = {num1 + num2}")
        blank()
        input_function()
    elif operator == "-":
        blank()
        print(f"{num1} - {num2} = {num1 - num2}")
        blank()
        input_function()
    elif operator == "*":
        blank()
        print(f"{num1} * {num2} = {num1 * num2}")
        blank()
        input_function()
    elif operator == "/":
        blank()
        print(f"{num1} / {num2} = {num1 / num2}")
        blank()
        input_function()
    else:
        blank()
        print(f"\'{operator}\' is an invalid input.")
        blank()
        input_function()


start()
