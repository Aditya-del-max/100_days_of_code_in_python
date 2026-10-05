'''def format_name(first_name, last_name):
    first_name = first_name.strip().capitalize()
    last_name = last_name.strip().capitalize()
    formatted_name = f"{first_name} {last_name}"
    return f"First Name: {first_name},\n Last Name: {last_name},\n Formatted Name: {formatted_name}"

first_names = input("Enter your first name: ").strip().capitalize()
last_names = input("Enter your last name: ").strip().capitalize()
x=format_name(first_name=first_names, last_name=last_names)
print(x)
'''
def format_name(first_name, last_name):
    if first_name == "" or last_name == "":
        return "You didn't provide valid inputs."
    first_name = first_name.strip().capitalize()
    last_name = last_name.strip().capitalize()
    formatted_name = f"{first_name} {last_name}"
    return f"First Name: {first_name},\n Last Name: {last_name},\n Formatted Name: {formatted_name}"

print(format_name(input("Enter your first name: "), input("Enter your last name: ")))
