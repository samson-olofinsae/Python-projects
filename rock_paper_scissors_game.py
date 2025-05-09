import random

the_rule = '''
Rock wins against scissors.
Scissors win against paper.
Paper wins against rock.
'''
values = ['Rock', 'Papers', 'Scissors']
user_choice = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n'))

if user_choice == 0:
    user_choice=values[0]
    print(f'You chose: {values[0]}')
    computer_choice=random.choice(values)
    print(f'computer chose: {computer_choice}')
    if user_choice == values[0] and computer_choice == values[2]:
     print('You won')
    else:
        print('sorry, computer wins')

elif user_choice == 1:
    user_choice=values[1]
    print(f'You chose: {values[1]}')
    computer_choice=random.choice(values)
    print(f'computer chose: {computer_choice}')
    if user_choice == values[1] and computer_choice == values[0]:
     print('You won')
    else:
        
        print('sorry, computer wins')
elif user_choice == 2:
    user_choice=values[2]
    print(f'You chose: {values[2]}')
    computer_choice=random.choice(values)
    print(f'computer chose: {computer_choice}')
    if user_choice == values[2] and computer_choice == values[1]:
     print('You won')
    else:
        
        print('sorry, computer wins')
