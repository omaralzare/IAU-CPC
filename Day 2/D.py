timeLeft = 240
inputs = input().split()
size = int(inputs[0])
time = timeLeft - int(inputs[1])
timeNeeded = 0
counter = 0
for i in range(1, size + 1):
    timeNeeded += 5
    if timeNeeded <= time:
        if (time - timeNeeded) >= 0:
            time -= timeNeeded
            counter += 1
print(counter)
