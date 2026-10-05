height=int(input("Enter your height in cm: "))
age = int(input("Enter your current age: "))
want_photo = input("Do you want a photo taken? Y or N. ")
bill = 0
if height >= 120:
    if age < 12:
        bill = bill + 5
    elif age <= 18:
        bill = bill + 7
    elif age > 35 and age < 45:
        bill = 0
        print("You get a free ride on the rollercoaster.")
    elif age > 18:
        bill = bill + 12
    if want_photo == "y" or want_photo == "Y":
        bill = bill + 3
    
    print(f"Your final bill is ${bill}.")
else:
    print("You are not eligible to ride the rollercoaster and can ride alone.")
