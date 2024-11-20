size = int(input())
arr = []
for i in range(size):
    for j in range(size):
        arr.append(1)
newArr = []
sum = 0
max = 0
for i in range(size - 1):
    for j in range(size):
        for k in range(j):
            sum += arr[k]
        newArr.append(arr[j] + sum)
        sum = 0
    for j in range(size):
        arr[j] = newArr[j]
    newArr = []
for i in range(size):
    if int(arr[i]) > max:
        max = int(arr[i])
print(max)
