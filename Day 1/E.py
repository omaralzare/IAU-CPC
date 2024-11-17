inputs = input().split()
space = int(inputs[0]) * int(inputs[1])
if space % 2 == 0:
    print(int(space / 2))
else:
    print(int((space - 1) / 2))
