inputs = input().split()
price = int(inputs[0])
money = int(inputs[1])
numbers = int(inputs[2])
result = 0
toBorrow = 0
for x in range(numbers):
    result += price * (numbers - x)
if result > money:
    toBorrow = result - money
print(toBorrow)
