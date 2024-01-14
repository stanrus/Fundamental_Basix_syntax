str_one = input()

while str_one != 'End':
    if str_one == 'SoftUni':
        str_one = input()
    for index in str_one:
        print(2 * index, end='')
    print('\r')
    str_one = input()