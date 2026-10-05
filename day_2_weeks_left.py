#Weeks left until 90 years old calculator
age=input("Enter your current age: ")
age_as_integer=int(age)
years_remaining=90-age_as_integer
weeks_remaining=years_remaining*52
days_remaining=years_remaining*365
print(f"You have {days_remaining} days,\n {weeks_remaining} weeks,\n and {years_remaining} years left until you are 90.")