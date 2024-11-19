testSize = int(input())
check = ["c", "o", "d", "e", "f", "o", "r", "c", "e", "s"]
word = []
counter = 0
for i in range(testSize):
    word.append(input())
for i in range(testSize):
    if word[i] in check:
        print("YES")
    else:
        print("NO")
