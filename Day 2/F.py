string = str(input())
counterLow = 0
counterUp = 0
for i in range(len(string)):
    string.split()
    if string[i].islower():
        counterLow += 1
    else:
        counterUp += 1
if counterUp > counterLow:
    print(string.upper())
else:
    print(string.lower())
