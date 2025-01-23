def add(n1, n2):
    return n1 + n2


def sub(n1, n2):
    return n1 - n2


def mul(n1, n2):
    return n1 * n2


def div(n1, n2):
    return n1 / n2


def pwr(n1, n2):
    return n1 ** n2


operations_dict = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div,
    "**": pwr,
}


def calculator():
    print('''
     _____________________
    |  _________________  |
    | | Jahanzaib Calc. | |  .----------------.  .----------------.  .----------------.  .----------------. 
    | |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
    |  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
    | | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
    | |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
    | | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
    | |___|___|___| |___| | | |  \ '.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ '.___.'\  | |
    | | 1 | 2 | 3 | | x | | | |   '._____.'  | || ||____|  |____|| || |  |________|  | || |   '._____.'  | |
    | |___|___|___| |___| | | |              | || |              | || |              | || |              | |
    | | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
    | |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
    |_____________________|
    ''')
    restart = True
    num1 = float(input("What is your first number?: "))
    while restart:

        for key in operations_dict:
            print(key)
        chosen_operation = input("Pick an operation: ")
        operation = operations_dict[f"{chosen_operation}"]
        num2 = float(input("What is your next number?: "))
        result = operation(num1, num2)
        print(f"{num1} {chosen_operation} {num2} = {result}")
        should_continue = input(
            f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ").lower()
        if should_continue == "y":
            num1 = result
        elif should_continue == "n":
            restart = False
            print("\n" * 25)
            calculator()


calculator()
