divisor = int(input())
boundary = int(input())



while (boundary / divisor) %1 != 0:
    boundary -= 1



print(boundary)