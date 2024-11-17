import math

sizez = input().split()
lsize = math.ceil(int(sizez[0]) / int(sizez[2]))
wsize = math.ceil(int(sizez[1]) / int(sizez[2]))
print(lsize * wsize)
