age = int(input())


while n != 4:
    if age <= 14:
        print('drink toddy')

    elif 14 < age <= 18:
        print('drink coke')

    elif 18 < age <= 21:
        print('drink beer')

    else:
        print('Bye.')

    n += 1
    age = int(input())
