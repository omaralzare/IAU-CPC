inputs = input().split()
size = int(inputs[0])
th = int(inputs[1])
index = input().split()
advancers = 0
check = int(index[th - 1])
for j in range(size):
    if int(index[j]) >= check and int(index[j]) != 0:
        advancers += 1
print(advancers)
