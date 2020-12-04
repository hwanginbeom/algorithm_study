# 14888번 - 연산자 끼워넣기
import sys
from itertools import permutations

a = int(input())
data = list(map(int, sys.stdin.readline().split()))
plus, sub, mul, div = map(int,input().split())
array = []
for i in range(plus):
    array.append('+')
for i in range(sub):
    array.append('-')
for i in range(mul):
    array.append('*')
for i in range(div):
    array.append('/')
print(array)

result = list(permutations(array, len(array)))
print(result)
print(a)
print(data)
print(plus, sub, mul, div)

for i in data:
    i
for i in result:
    for j in i:
        data
        

# 15651번 - N과 M(4)
n, m = map(int, input().split())

check = [False] * (n + 1)
a = [0] * m


def go(index, n, m):
    if index == m:
        for i in range(m):
            print(a[i], end=' ')
        print()
        return
    for i in range(1, n + 1):
        a[index] = i
        go(index + 1, n, m)



go(0, n, m)