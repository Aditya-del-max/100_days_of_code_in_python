print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n").lower()
name2 = input("What is their name? \n").lower()
combined_names = name1 + name2
t=combined_names.count("t")
r=combined_names.count("r")
u=combined_names.count("u")
e=combined_names.count("e")
true = t + r + u + e
l=combined_names.count("l")
o=combined_names.count("o")
v=combined_names.count("v")
e=combined_names.count("e")
love = l + o + v + e
score = int(str(true) + str(love))
print(f"Your score is {score}.")
if (score < 10) or (score > 90):
    print(f"Your score is {score}, you go together like coke and mentos.")
elif (score >= 40) and (score <= 50):
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")