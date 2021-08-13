import sys

input = sys.stdin.readline

_list = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9, 12]
for i in range(11,100):
    _list.append(_list[i-3] + _list[i-2])

for _ in range(int(input())):
    print(_list[int(input())-1])
