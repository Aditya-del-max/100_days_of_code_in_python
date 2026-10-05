import random
def live_checker(lives,guess,number,game_running):
    if guess!=number:
        print("wrong answer")
        lives-=1
        print(lives)
    if lives==0:
        print("game over u loose")
        game_running=False
    if guess==number:
            print("you won!! ")
            game_running=False
            lives=0
    return lives,game_running

def start_game():
    number=random.randint(1,100)
    print(number)
    game_running=True
    lives=0
    while game_running:
        choice=input("type 'easy' for easy mode and 'hard' for hard mode\n")
        if choice=="easy":
            lives=10
        elif choice=="hard":
            lives=5
        else:
            print("wrong answer")
        while lives!=0:
            guess=int(input("guess the number? "))
            lives,game_running=live_checker(lives,guess,number,game_running)
        
print("Welcome to number guessing game ")
play_game=input("press 'y' to play the game\n")
while play_game=="y" :
    start_game()
    play_again=input("do you want to play again(y/n)? \n ")
    if play_again=="y":
        game_running=True
    elif play_again=="n":
        print("thank you for playing")
        play_game="n"