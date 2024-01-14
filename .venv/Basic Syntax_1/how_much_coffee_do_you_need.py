words = input()
coffe = 0

while words != 'END':
    if words.lower() == 'dog' or words.lower() == 'cat' or words.lower() == 'coding' or words.lower() == 'movie':
        if words.isupper():
            coffe += 2
        else:
            coffe += 1
    else:
        pass
    words = input()
if coffe > 5:
    print('You need extra sleep')
else:
    print(coffe)