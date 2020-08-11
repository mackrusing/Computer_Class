# Terminal Calculator
# (Orignially Terminal-Arithmetic-Machine)

# Created Jan 20, 2020

# v1.0
# Python 3

def start():
    print("")
    print("Welcome to the Terminal Arithmetic Machine!")
    print("For a list of all operators type help.")
    print("Otherwise, press ENTER to begin.")
    print("")
    start_input = input(">> ")
    if start_input == "HELP":
        print("")
        print("----- Help Menu -----")
        print("addition = +")
        print("subtraction = -")
        print("multiplication - *")
        print("division - /")
        print(" ")
        print("Press ENTER to begin.")
        print("")
        start_input = input(">> ")
        if start_input == "":
            input_operator()
        else:
            input_operator()
    else:
        input_operator()


def input_operator():
    print(" ")
    operator = input("Enter operation: ")
    if operator == "+":
        input_num1("+")
    elif operator == "-":
        input_num1("-")
    elif operator == "*":
        input_num1("*")
    elif operator == "/":
        input_num1("/")
    else:
        print("")
        print(f"\"{operator}\" is an invalid operator.")
        print("For a list of all operators type help.")
        print("Otherwise, press ENTER to continue.")
        print("")
        invalid_operator = input(">> ")
        if invalid_operator == "help":
            print("")
            print("----- Help Menu -----")
            print("addition = +")
            print("subtraction = -")
            print("multiplication - *")
            print("division - /")
            print("")
            print("Press ENTER to continue.")
            print("")
            start_input = input(">> ")
            if start_input == "":
                input_operator()
            else:
                input_operator()
        else:
            input_operator()


def input_num1(operator):
    if operator == "+":
        print("")
        num1 = input("Enter first term: ")
        try:
            num1 = int(num1)
            input_num2(operator, num1)
        except ValueError:
            try:
                num1 = float(num1)
                input_num2(operator, num1)
            except ValueError:
                print("")
                print(f"\"{num1}\" is an invalid input.")
                print("Press ENTER to continue.")
                print("")
                invalid_operator = input(">> ")
                if invalid_operator == "":
                    input_num1(operator)
                else:
                    input_num1(operator)
    elif operator == "-":
        print("")
        num1 = input("Enter the minued: ")
        try:
            num1 = int(num1)
            input_num2(operator, num1)
        except ValueError:
            try:
                num1 = float(num1)
                input_num2(operator, num1)
            except ValueError:
                print("")
                print(f"\"{num1}\" is an invalid input.")
                print("Press ENTER to continue.")
                print("")
                invalid_operator = input(">> ")
                if invalid_operator == "":
                    input_num1(operator)
                else:
                    input_num1(operator)
    elif operator == "*":
        print("")
        num1 = input("Enter first factor: ")
        try:
            num1 = int(num1)
            input_num2(operator, num1)
        except ValueError:
            try:
                num1 = float(num1)
                input_num2(operator, num1)
            except ValueError:
                print("")
                print(f"\"{num1}\" is an invalid input.")
                print("Press ENTER to continue.")
                print("")
                invalid_operator = input(">> ")
                if invalid_operator == "":
                    input_num1(operator)
                else:
                    input_num1(operator)
    elif operator == "/":
        print("")
        num1 = input("Enter the dividend: ")
        try:
            num1 = int(num1)
            input_num2(operator, num1)
        except ValueError:
            try:
                num1 = float(num1)
                input_num2(operator, num1)
            except ValueError:
                print("")
                print(f"\"{num1}\" is an invalid input.")
                print("Press ENTER to continue.")
                print("")
                invalid_operator = input(">> ")
                if invalid_operator == "":
                    input_num1(operator)
                else:
                    input_num1(operator)


def input_num2(operator, num1):
    if operator == "+":
        print("")
        num2 = input("Enter second term: ")
        try:
            num2 = int(num2)
            calculate(operator, num1, num2)
        except ValueError:
            try:
                num2 = float(num2)
                calculate(operator, num1, num2)
            except ValueError:
                print("")
                print(f"\"{num2}\" is an invalid input.")
                print("Press ENTER to continue.")
                print("")
                invalid_operator = input(">> ")
                if invalid_operator == "":
                    input_num2(operator, num1)
                else:
                    input_num2(operator, num1)
    elif operator == "-":
        print("")
        num2 = input("Enter the subtrahend: ")
        try:
            num2 = int(num2)
            calculate(operator, num1, num2)
        except ValueError:
            try:
                num2 = float(num2)
                calculate(operator, num1, num2)
            except ValueError:
                print("")
                print(f"\"{num2}\" is an invalid input.")
                print("Press ENTER to continue.")
                print("")
                invalid_operator = input(">> ")
                if invalid_operator == "":
                    input_num2(operator, num1)
                else:
                    input_num2(operator, num1)
    elif operator == "*":
        print("")
        num2 = input("Enter second factor: ")
        try:
            num2 = int(num2)
            calculate(operator, num1, num2)
        except ValueError:
            try:
                num2 = float(num2)
                calculate(operator, num1, num2)
            except ValueError:
                print("")
                print(f"\"{num2}\" is an invalid input.")
                print("Press ENTER to continue.")
                print("")
                invalid_operator = input(">> ")
                if invalid_operator == "":
                    input_num2(operator, num1)
                else:
                    input_num2(operator, num1)
    elif operator == "/":
        print("")
        num2 = input("Enter the divisor: ")
        try:
            num2 = int(num2)
            calculate(operator, num1, num2)
        except ValueError:
            try:
                num2 = float(num2)
                calculate(operator, num1, num2)
            except ValueError:
                print("")
                print(f"\"{num2}\" is an invalid input.")
                print("Press ENTER to continue.")
                print("")
                invalid_operator = input(">> ")
                if invalid_operator == "":
                    input_num2(operator, num1)
                else:
                    input_num2(operator, num1)


def calculate(operator, num1, num2):
    if operator == "+":
        print("")
        print(f"{num1} + {num2} = {num1 + num2}")
        restart()
    elif operator == "-":
        print("")
        print(f"{num1} - {num2} = {num1 - num2}")
        restart()
    elif operator == "*":
        print("")
        print(f"{num1} * {num2} = {num1 * num2}")
        restart()
    elif operator == "/":
        print("")
        print(f"{num1} / {num2} = {num1 / num2}")
        restart()


def restart():
    print("")
    print("Would you like to evaluate another expression?")
    print("y/n")
    print("")
    restart_var = input(">> ")
    if restart_var == "y":
        input_operator()
    if restart_var == "n":
        return "exited function"
    else:
        print("")
        print(f"\"{restart_var}\" is not a valid input.")
        restart()


start()
