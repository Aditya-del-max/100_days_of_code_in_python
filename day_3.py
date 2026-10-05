height = int(input("Enter your height in cm: "))
age = int(input("Enter your current age: "))
if height >= 120:
    if age < 12:
        print("Your ticket price is $5.")
    elif age <= 18:
        print("Your ticket price is $7.")
    else:
        print("You are eligible to ride the rollercoaster and can ride alone.")
else:
    print("The number is odd.")