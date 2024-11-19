arrSize = int(input())
index = input().split()
answers = []
isHard = False
for i in range(arrSize):
    answers.append(index[i])
    if answers[i] == "1":
        isHard = True
if isHard:
    print("HARD")
else:
    print("EASY")
