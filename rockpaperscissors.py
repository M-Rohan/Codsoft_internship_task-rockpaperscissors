# < Rock Paper Scissors Game >

rock = '''
     _______
----'    ____)
        (______)
        (______)
        (_____)
----.___(____)
'''

paper = '''
      _______
----'    _____)_____
            _________)
            __________)
           __________)
----._____________)
'''

scissors ='''
      _______
----'   ______)______
          ____________)
          _____________)
          ______)
----.__________)
'''

import random 

game_on = True
user_score = 0
computer_score = 0
print("\n< ROCK PAPER SCISSORS GAME >")
while (game_on == True):
    print("\n Enter: 0 for Rock | 1 for paper | 2 for scissors")
    user_choice = int(input("Enter your choice:"))

    if user_choice == 0 :
        print(rock)
    elif user_choice == 1 :
        print(paper)
    elif user_choice == 2 :
        print(scissors)
    else :
        print("Invalid input !!")
        user_choice = int(input("Enter your choice:"))
        

    computer_choice = random.randint(0,2)
    print(f"\n Computer chose {computer_choice}")

    if computer_choice == 0 :
        print(rock)
    elif computer_choice == 1 :
        print(paper)
    elif computer_choice == 2 :
        print(scissors)
    else :
        print("Invalid input !!")
    
    if (computer_choice == 0) and (user_choice == 2) :
        computer_score += 1
        print(f"You lose !! \n Score :\n Your score ={user_score} \t Computer score ={computer_score}")
    elif (user_choice == 0) and (computer_choice == 2) :
        user_score += 1
        print(f"You win !! \n Score :\n Your score ={user_score} \t Computer score ={computer_score}")
    elif (user_choice > computer_choice) :
        user_score += 1
        print(f"You win !! \n Score :\n Your score ={user_score} \t Computer score ={computer_score}")
    elif (computer_choice > user_choice) :
        computer_score += 1
        print(f"You lose !! \n Score :\n Your score ={user_score} \t Computer score ={computer_score}")
    else :
        print(f"It's a Draw  \n Score :\n Your score ={user_score} \t Computer score ={computer_score}")

    print("PLAY AGAIN ?")
    play_again = int(input("Enter  1 for yes || Enter  0 for no"))
    if play_again == 1 :
        game_on = True
    elif play_again == 0 :
        game_on = False
    else :
        print("Invalid response !")
        break
    
