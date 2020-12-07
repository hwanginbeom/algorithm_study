import sys

a = int(sys.stdin.readline())
array=[]
for i in range(a):
    b = int(sys.stdin.readline())
    if b == 0:
        array.pop(-1)
    else:
        array.append(b)
print(sum(array))