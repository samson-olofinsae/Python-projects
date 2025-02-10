
# The Fizzbuzz game exercise
#print the numbers between 1 and 100
# if number is divisible by 3, print Fizz
# if number is divisible by 5, print Fizz
# if number is divisible by 3 and 5, print FizzBuzz

for number in range(1,101):
    if number % 3 == 0 and number % 5 == 0:
        number = 'FizzBuzz'
    elif number % 3 == 0:
        number = 'Fizz'
    elif number % 5 == 0:
        number = 'Buzz'  
    print(number)
