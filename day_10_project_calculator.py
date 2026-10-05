#calculator
def add(x, y):
    return float(x + y)
def subtract(x, y):
    return float(x - y)
def multiply(x, y):
    return float(x * y)
def divide(x, y):
    return float(x / y)

symbols = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
def calculator():
    print(''' _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
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
|_____________________|''')
    n1=float(input("Enter first number: "))
    proceed = True
    while proceed:
        operation=input("Enter operation (+, -, *, /): ")
        n2=float(input("enter second number: "))
        result = symbols[operation](n1, n2)
        print(f"{n1} {operation} {n2} = {result}")
        choice = input("Do you want to continue calculating with the answer? (y/n) or (q) to quit: ")
        if choice.lower() == 'y':
            n1=result
        elif choice.lower() == 'n':
            print("\n" * 20)
            n1=float(input("Enter first number: "))
        elif choice.lower() == 'q':
            proceed = False
            print("Thank you for using the calculator!")

calculator()