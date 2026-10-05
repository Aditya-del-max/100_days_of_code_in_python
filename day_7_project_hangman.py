import hangman
HANGMAN_stages=hangman.HANGMAN_stage
lives=6
import random
word_list=["aditya","monkey","cammel","aqdas_gandu"]
chosen_word=random.choice(word_list)
#print(chosen_word)
i=0
k=0
#creating empty list 
display =["_"]*len(chosen_word)
end_of_game= False

while not end_of_game or not lives<0:
   # for letter in range(len(chosen_word)):
    #    display+=["_"]
    print(display)
    #guess letter
    guess=input("guess a letter? \n").lower()
# allready guessed
    if guess in display:
         print("allready guessed")
         continue
    i=0
    for letter in range(len(chosen_word)):
        if guess == chosen_word[i]:
            display[i]=chosen_word[i]
        i+=1
#loose
    if guess not in chosen_word:
        lives-=1
        print(HANGMAN_stages[k])
        k+=1
        if lives==0:
                print("u loose")
                break
#win
    if "_" not in display:
        end_of_game=True
        print(display)
        print("you win")
