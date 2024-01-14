num = int(input())
number = int(input())


while num != 0:



    if number == 88:
        print('Hello')

    elif number == 86:
        print('How are you?')


    elif (number != 88 or number != 86)  and number < 88:
        print('GREAT!')


    elif number > 88:
        print('Bye.')
    number = int(input())
    num -= 1

