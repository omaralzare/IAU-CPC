arrSize = int(input())
arr = []
counter = 0
newCounter = 0
for row in range(arrSize):
    arr2 = []
    index = input().split()
    for col in range(3):
        arr2.append(index[col])
    arr.append(arr2)
for row in range(arrSize):
    counter = 0
    for col in range(3):
        if arr[row][col] == "1":
            counter += 1
    if counter >= 2:
        newCounter += 1
print(newCounter)
