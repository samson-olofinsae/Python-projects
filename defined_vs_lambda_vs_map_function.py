# FUNCTIONS: DEFINED, LAMBDA and MAP funtions
# Defined function vs Lambda function


# defined function
def add(x, y):
    result = x + y
    return result

print (add(4 ,10))

# lambda function

# syntax
# lambda argument : expression
mylamda= lambda x, y: x + y

print(mylamda(6, 9))

#print(mylambda(6, 7))

# defined function

def printer():
    print('hello world')


# lambda function

mylam = lambda : 'hello world'

print(mylam())


# defined function
def greetings(name):
    print(f'hello {name}. This is from a defined function')


greetings('Sam')


# lambda function
mylam = lambda name : f'hello {name}. This is from a lambda function'
print(mylam('Sam'))

# Lamba function to store details

details=lambda book: f'I need to read {book} by lunch break today'

print(details('Harry Potter'))

# MAP function
# This enables you to call a defined function on a series of iterable arguments in parallel 
# syntax: map(function, iterable)

def program(x):
    return f'{x} is very good'


mymap=map(program, ['python', 'javascript'])
#print(mymap)
print(list(mymap))
