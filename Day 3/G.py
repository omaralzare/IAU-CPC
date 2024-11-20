size = int(input())
index = input().split()
arr = []
check = list(range(2000))
counter = 0
if len(index) != size:
    exit()
for i in range(size):
    arr.append(int(index[i]))
for i in range(size):
    if arr[i] in check:
        check.remove(arr[i])
print(min(check))
