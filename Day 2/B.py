userName = input()
userName.split()
HeOrShe = list(set(userName))
if len(HeOrShe) % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
