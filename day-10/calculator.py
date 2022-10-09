from art import logo


def add(first_number, second_number):
    return first_number + second_number


def subtract(first_number, second_number):
    return first_number - second_number


def multiply(first_number, second_number):
    return first_number * second_number


def divide(first_number, second_number):
    return first_number / second_number


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculator():
    first_number = float(input("What's the first number? "))
    keep_calculating = 'y'
    while (keep_calculating in ('y', 'n')):
        for symbol in operations:
            print(symbol)
        operation = input("What's the operation? ")
        second_number = float(input("What's the next number? "))
        result = operations[operation](first_number, second_number)
        print(f"{first_number} {operation} {second_number} = {result}")
        keep_calculating = input(
            f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation\n")
        if keep_calculating == 'y':
            first_number = result
        elif (keep_calculating == 'n'):
            calculator()
        else:
            return


print(logo)
calculator()
