print('welcome to Python Pizza Deliveries!')
size = input('What size pizza do you want? S, M or L: ')



if size == 'S':
    s_bill = 15
    print(f'Your current bill is: ${s_bill}')
    pepperoni = input('Do you want pepperoni on your pizza? Y or N: ')
    if pepperoni == 'Y':
        s_bill += 3
        print(f'Your current bill is: ${s_bill}')
        extra_cheese = input('Do you want extra cheese? Y or N: ')
        if extra_cheese == 'Y':
            s_bill += 1
            print(f'Your total bill is: ${s_bill}')
        elif extra_cheese == 'N':
            print(f'Your total bill is ${s_bill}')

    
if size == 'M':
    m_bill = 20
    print(f'Your current bill is ${m_bill}')
    pepperoni = input('Do you want pepperoni on your pizza? Y or N: ')
    if pepperoni == 'Y':
        m_bill += 3
        print(f'Your current bill is: ${m_bill}')
        extra_cheese = input('Do you want extra cheese? Y or N: ')
        if extra_cheese == 'Y':
            m_bill += 1
            print(f'Your total bill is: ${m_bill}')
        elif extra_cheese == 'N':
            print(f'Your total bill is ${m_bill}')

if size == 'L':
    l_bill = 25
    print(f'Your current bill is ${l_bill}')
    pepperoni = input('Do you want pepperoni on your pizza? Y or N: ')
    if pepperoni == 'Y':
        l_bill += 3
        print(f'Your current bill is: ${l_bill}')
        extra_cheese = input('Do you want extra cheese? Y or N: ')
        if extra_cheese == 'Y':
            l_bill += 1
            print(f'Your total bill is: ${l_bill}')
        elif extra_cheese == 'N':
            print(f'Your total bill is ${l_bill}')
