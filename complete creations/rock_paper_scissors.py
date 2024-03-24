import random

user_action = input("Enter a choice (rock, paper, scissors): ")
possible_actions = ["rock", "paper", "scissors"]
computer_action = random.choice(possible_actions)
print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

if user_action == computer_action:
     print ('its a tie!')
elif user_action == 'rock':
    if computer_action == 'paper':
        print ('paper covers rock you lose!')
    if computer_action =='scissors':
          print ('Rock breaks scissors you WIN!')
elif user_action == 'paper':
    if computer_action == 'rock':
          print ('paper covers rock you WIN!')
    if computer_action == ("scissors"):
         print ("scissors cuts paper you lose!")
elif user_action == 'scissors':
    if computer_action == 'rock':
          print('Rock breaks scissors you lose!')
    if computer_action =='paper':
          print ('scissors cuts paper you win!')