lvl = int(input())
lvlCheck = []
plvl = input().split()
xlvl = []
qlvl = input().split()
ylvl = []
counter = 0
for i in range(lvl):
    lvlCheck.append(i + 1)
for i in range(int(plvl[0])):
    xlvl.append(int(plvl[i + 1]))
for i in range(int(qlvl[0])):
    ylvl.append(int(qlvl[i + 1]))
for i in range(int(plvl[0])):
    if xlvl[i] in lvlCheck:
        lvlCheck.remove(xlvl[i])
for i in range(int(qlvl[0])):
    if ylvl[i] in lvlCheck:
        lvlCheck.remove(ylvl[i])
if not lvlCheck:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")
