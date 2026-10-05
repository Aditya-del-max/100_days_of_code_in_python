import random
print("Welcome to the Rock, Paper, Scissors Game!")
user_choice = int(input("Press 0 for Rock, 1 for Paper, and 2 for Scissors: "))
rock=("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
paper=("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
scissors=("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

if user_choice == 0:
    print(f"You chose Rock:\n{rock}")
elif user_choice == 1:
    print(f"You chose Paper:\n{paper}")
elif user_choice == 2:
    print(f"You chose Scissors:\n{scissors}")
else:
    print("Invalid input. Please choose 0, 1, or 2.")

print("Computer chooses:")

computer_choice = random.randint(0, 2)
if computer_choice == 0:
    print(f"Computer chose Rock:\n{rock}")
elif computer_choice == 1:
    print(f"Computer chose Paper:\n{paper}")
elif computer_choice == 2:
    print(f"Computer chose Scissors:\n{scissors}")
else:
    print("Invalid input. Please choose 0, 1, or 2.")
if user_choice == computer_choice:
    print("It's a draw!")
elif (user_choice == 0 and computer_choice == 2) or (user_choice == 1 and computer_choice == 0) or (user_choice == 2 and computer_choice == 1):
    print("You win!")
else:
    print("You lose!")