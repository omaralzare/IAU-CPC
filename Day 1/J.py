import math

inputs = input().split()
people = int(inputs[0])
wizards = int(inputs[1])
percent = float(int(inputs[2]) / 100)
result = math.ceil(people * percent) - wizards
if result >= 0:
    print(result)
else:
    print(0)
