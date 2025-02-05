import random
# hard level
# The order of letters, symbols and number is randomised

print('Welcome to the PyPassword Generator!')
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P',
           'Q', 'R', 'S', 'T', 'U', 'V', 'W' ,'X', 'Y', 'Z']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

nr_letters = int(input('How many letters would you like in your password?\n'))
nr_symbols = int(input('How many symbols would you like?\n'))
nr_numbers = int(input('How many numbers would you like?\n'))

letters_pass_word=''
symbols_pass_word=''
numbers_pass_word=''

for ch in range(1,(nr_letters+1)):
    letter_string=random.choice(letters)
    #letters_pass_word=letters_pass_word+letter_string
    letters_pass_word += letter_string

for ch in range(1,(nr_symbols+1)):
    symbols_string=random.choice(symbols)
    #symbols_pass_word=symbols_pass_word+symbols_string
    symbols_pass_word += symbols_string

for ch in range(1,(nr_numbers+1)):
    numbers_string=random.choice(numbers)
    #numbers_pass_word=numbers_pass_word+numbers_string
    numbers_pass_word += numbers_string

#print(f'Your easy password is {letters_pass_word}{symbols_pass_word}{numbers_pass_word}')
initial_password=f'{letters_pass_word}{symbols_pass_word}{numbers_pass_word}'
#print(initial_password)

###### Performing SHUFFLING (You can only shuffle items of a list)

# convert your randomly-generated password string to list
password_list= list(initial_password)

# shuffle the password 
random.shuffle(password_list)

# Reconvert to String
password_string = ''.join(password_list)
print(f'Your hard password is {password_string}')
