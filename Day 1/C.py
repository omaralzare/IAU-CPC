brothers = input().split()
if (brothers[0] == "1" or brothers[0] == "2") and (
    brothers[1] == "1" or brothers[1] == "2"
):
    print("3")
elif (brothers[0] == "1" or brothers[0] == "3") and (
    brothers[1] == "1" or brothers[1] == "3"
):
    print("2")
else:
    print("1")
