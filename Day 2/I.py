matches = int(input())
arrMatche = []
for i in range(matches):
    newArr = []
    index = input().split()
    for j in range(2):
        newArr.append(int(index[j]))
    arrMatche.append(newArr)
