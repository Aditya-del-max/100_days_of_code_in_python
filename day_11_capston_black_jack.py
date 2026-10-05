import random

print("Welcome to the Blackjack Game!")

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)
my_cards = []
computer_cards = []

for _ in range(2):
    my_cards.append(deal_card())
    computer_cards.append(deal_card())
print(f"Your cards: {my_cards}, current score: {sum(my_cards)}")
print(f"Computer's first card: {computer_cards[0]}")
user_choice = input("Type 'y' to get another card, type 'n' to pass: ")
choice=True
while choice:
    if sum(computer_cards) < 17:
                computer_cards.append(deal_card())
    if user_choice == 'y':
        my_cards.append(deal_card())
        computer_cards.append(deal_card())
        print(f"Your cards: {my_cards}, current score: {sum(my_cards)}")
        print(f"Computer's first card: {computer_cards[0]}")
    elif user_choice == 'n':
        if sum(my_cards) > sum(computer_cards):
            print(f"Your final hand: {my_cards}, final score: {sum(my_cards)}")
            print(f"Computer's final hand: {computer_cards}, final score: {sum(computer_cards)}")
            print("You win!")
        elif sum(my_cards) < sum(computer_cards):
            print(f"Your final hand: {my_cards}, final score: {sum(my_cards)}")
            print(f"Computer's final hand: {computer_cards}, final score: {sum(computer_cards)}")
            print("You lose!")
        elif sum(my_cards) == sum(computer_cards):
             
            choice = False
    else:
        print("Invalid input. Please type 'y' or 'n'.")
