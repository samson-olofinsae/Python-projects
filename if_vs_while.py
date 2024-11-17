# different behaviour of IF and WHILE statements
# WHILE behaves like an if statement, with the exception that it performs in indefinate loop if the condition is true

number = 8

if number < 9:
    #print('number is less than 9')
    pass


while number < 9:
    print('number is less than 9') # this will generate a flood of values (as long as line 10 is true)
