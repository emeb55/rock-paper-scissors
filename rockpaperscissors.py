#ask user to make a choice 
#if choice is not valid 
#print and erorr
#let computer make a choice 
#print choices (emojis)
#determine the winner
#ask the user if they want to continue
#if not 
#terminate

       # if guess == r:
        #    print("🪨")
        #elif guess == p:
        #    print("📃")
        #elif guess == s:
        #    print("✂️")

import random 

emojis = {'r':'🪨','p':'📃','s':'✂️'}
choices = ('r', 'p', 's')
while True:
    guess = input("lets play Rock Paper Scissors! (r/p/s)").lower().strip()
    if guess not in choices:
        print("Please enter a valid response ;)")
        continue
                    
    computer_choice = random.choice(choices)

    print(f' you chose {emojis[guess]}')
    print(f' computer chose {emojis[guess]}')

    if guess == computer_choice:
        print("tie")
    elif (
    (guess == 'r' and computer_choice == 's' ) or 
    (guess == 's' and computer_choice == 'p' ) or 
    (guess == 'p' and computer_choice == 'r' )):
        print("!!!!you win!!!!!")
    else:
        print( "you lose ://///")

    should_continue = input ("continue? (y/n): ").lower()
    if should_continue == "n":
        break 



    
 



    
