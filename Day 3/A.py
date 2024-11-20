number = int(input())
numbers = input().split()
counter = 0
sum = 0
for i in range(len(numbers)):
    if int(numbers[i]) > 0 and int(numbers[i]) % 6 == 0:
        counter += 1
        sum += int(numbers[i])
print(counter, sum)
