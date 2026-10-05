'''import random
print("welcome to name randomiser")
names_string=input("Give me everybody's names, separated by a comma and a space. ")
names=names_string.split(", ")
person_number=random.randint(0, len(names) - 1)
print(f"{names[person_number]} is going to buy the meal today!")
'''
print("Welcome to Treasure Island.")
line1=[" "," "," "," ",]
line2=[" "," "," "," ",]
line3=[" "," "," "," ",]
map=[line1,line2,line3]
print(f"A={map[0]}\nb={map[1]}\nc={map[2]}")
change=input("where should the x be placed? ")
change_lower=change.lower()
first=change_lower[0]
second=change_lower[1]
if first=="a":
    map[0][int(second)-1]="x"
elif first=="b":
    map[1][int(second)-1]="x"
elif first=="c":
    map[2][int(second)-1]="x"
else:
    print("invalid input")
print(f"A={map[0]}\nb={map[1]}\nc={map[2]}")