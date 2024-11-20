size = int(input())
index = input().split()
arr = []
newArr = []
for i in range(size):
    arr.append(index[i])
newArr.append(arr[size - 1])
for i in range(size - 1):
    newArr.append(arr[i])
for i in range(size):
    print(newArr[i], end=" ")
