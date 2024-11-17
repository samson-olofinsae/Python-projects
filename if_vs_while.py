# different behaviour of IF and WHILE statements
# WHILE behaves like an if statement, with the exception that it performs an indefinate loop if the condition is true

number = 8

if number < 9:
    #print('number is less than 9')
    pass


while number < 9:
    print('number is less than 9') # this will indefinately generate a flood of values (as long as the statement naumber < 9 is true)
    break # add a break to break out of the indefinate WHILE loop
