money = int(input())
denominations = [100, 20, 10, 5, 1]
number = 0

for denomination in denominations:
    count = money // denomination
    number += count
    money -= count * denomination

print(number)
