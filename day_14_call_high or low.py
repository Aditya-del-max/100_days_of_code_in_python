import random
from day_14_project_high_or_low import data,logo,vs
print(logo)
random_index1 = random.choice(data)
print(f"Compare A: {random_index1['name']}, a {random_index1['description']}, from {random_index1['country']}.")
print(vs)
random_index2 = random.choice(data)
while random_index1 == random_index2:
    random_index2 = random.choice(data)
print(f"Compare B: {random_index2['name']}, a {random_index2['description']}, from {random_index2['country']}.")
correct_answer = ''
player_score = 0
game_over = False
while not game_over:
    if random_index1['follower_count'] > random_index2['follower_count']:
        correct_answer = 'a'
    elif random_index1['follower_count'] < random_index2['follower_count']:
        correct_answer = 'b'
    ask=input("who has more followers 'A' or 'B' : ").lower()
    if ask == correct_answer:
        player_score += 1
        print(f"You are right! Your current score is: {player_score}")
        random_index1 = random_index2
        random_index2 = random.choice(data)
        while random_index1 == random_index2:
            random_index2 = random.choice(data)
        print(logo)
        print(f"Compare A: {random_index1['name']}, a {random_index1['description']}, from {random_index1['country']}.")
        print(vs)
        print(f"Compare B: {random_index2['name']}, a {random_index2['description']}, from {random_index2['country']}.")
    elif ask != correct_answer:
        print(f"You are wrong! Your final score is: {player_score}")
        game_over = True
