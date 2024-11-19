numbers = input()
counter = 0
for i in range(len(numbers)):
    if numbers[i] == "4" or numbers[i] == "7":
        counter += 1
if counter == 4 or counter == 7:
    print("YES")
else:
    print("NO")
