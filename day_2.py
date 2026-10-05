#BMI calculator
height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kilograms: "))
bmi = weight / (height ** 2)
#print(f"Your BMI is: ({bmi:.2f})")
bmi_as_integer=int(bmi)
#print(f"Your BMI as an integer is: {bmi_as_integer}")
print("Your BMI is: " + str(bmi_as_integer))