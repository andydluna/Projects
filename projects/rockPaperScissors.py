choices = set()

ROCK = 'rock'
PAPER = 'paper'
SCISSORS = 'scissors'

choices.add(ROCK)
choices.add(PAPER)
choices.add(SCISSORS)

user1 = input('User 1, please enter your name: ')
user2 = input('User 2, please enter your name: ')

user1_choice = input(f'{user1}, do you want to choose rock, paper or scissors? ').lower()
user2_choice = input(f'{user2}, do you want to choose rock, paper or scissors? ').lower()

if user1_choice in choices and user2_choice in choices and user1_choice == user2_choice:
    print("It's a tie!")
elif (user1_choice == ROCK and user2_choice == PAPER) \
or (user1_choice == PAPER and user2_choice == ROCK):
     print('Paper wins!')
elif (user1_choice == ROCK and user2_choice == SCISSORS) \
or (user1_choice == SCISSORS and user2_choice == ROCK):
     print('Rock wins!')
elif (user1_choice == PAPER and user2_choice == SCISSORS) \
or (user1_choice == SCISSORS and user2_choice == PAPER):
     print('Scissors wins!')
else:
    print('Invalid input, try again. Please enter rock, paper or scissors.')