import random
cards=[11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card(x):
    dealt_cards = []
    for _ in range(x):
        dealt_cards.append(random.choice(cards))
    return dealt_cards
def calculate_score(my_cards, computer_cards):
    if sum(my_cards) > 21:
        print("You went over. You lose!")
        continue_game = False
    elif sum(computer_cards) > 21:
        print("Computer went over. You win!")
        continue_game = False
    elif sum(my_cards) > sum(computer_cards):
        print("You win!")
        continue_game = False
    elif sum(my_cards) < sum(computer_cards):
        print("You lose!")
        continue_game = False
    else:
        print("It's a draw!")
print("Welcome to the Blackjack Game!")
question = input("Do you want to play a game of Blackjack? Type 'y' or 'n': \n")
if question == 'y':
    my_cards = deal_card(2)
    computer_cards = deal_card(2)
    print(f"Your cards: {my_cards}, current score: {sum(my_cards)}")
    print(f"Computer's first card: {computer_cards[0]}")
continue_game = True
while continue_game:
    user_choice = input("Type 'y' to get another card, type 'n' to pass: \n")
    if user_choice=='y':
        my_cards.append(deal_card(1)[0])
        print(f"Your cards: {my_cards}, current score: {sum(my_cards)}")
        print(f"Computer's first card: {computer_cards[0]}")
        calculate_score(my_cards, computer_cards)
        
    elif user_choice=='n':
        print("\n" * 20)
        print(f"Your final hand: {my_cards}, final score: {sum(my_cards)}")
        print(f"Computer's final hand: {computer_cards}, final score: {sum(computer_cards)}")
        calculate_score(my_cards, computer_cards)
        continue_game = False
