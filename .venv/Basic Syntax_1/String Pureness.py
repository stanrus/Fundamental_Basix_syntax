n = int(input())
check = True

while n != 0:
    check = True
    strin = input()
    for k in strin:
        if k == ',' or k == '.' or k == '_':
            check = False
            break
        else:
            check = True

    if check == True:
        print(f"{strin} is pure.")
    else:
        print(f"{strin} is not pure!")
    n -= 1