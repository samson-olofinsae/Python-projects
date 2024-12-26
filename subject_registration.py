courses=['math', 'physics', 'chemistry', 'biology']

print('You may register two courses for the semster')

first_sub = input('enter fisrt course: ')
while first_sub not in courses:
    print('course not valid')
    first_sub = input('re-enter fisrt course: ')
else:
    print('course valid')
    print(f'{first_sub} registerd successfully')


second_sub= input('enter second course: ')
while second_sub == first_sub:
    print('course already registered')
    second_sub = input('re-enter second course: ')
else:
    while second_sub not in courses:
        print('course not valid')
        second_sub = input('re-enter second course: ')
    else:
        print('course valid')
        print(f'{second_sub} registerd successfully')




print(f'courses registered for the semester: {first_sub} , {second_sub}')
