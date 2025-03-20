# different behaviour of IF and WHILE statements
# WHILE behaves like an if statement, with the exception that it performs an indefinate loop if the condition is true

# IF example
number = 8

if number < 9:
    #print('number is less than 9')
    pass
# WHILE example 1

while number < 9:
    print('number is less than 9') # this will indefinately generate a flood of values 
                                   # (as long as the statement naumber < 9 is true)
    break # add a break to break out of the indefinate WHILE loop
    pass 
# WHILE example 2

sky_colour='blue'  # asignment operation

while sky_colour == 'blue': # comparative operation    
    print ('sky colour is blue') # this will generate an indefinate WHILE loop since 
                                 # sky_colour comparation (== 'blue') is still the 
                                 # same as the assignment (= 'blue')in memory
