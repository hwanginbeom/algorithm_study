from bisect import bisect
import sys

input = sys.stdin.readline

n = int(input())
_port = list(map(int, input().split()))
_list = [_port[0]]
for i in range(1, n):
    if _port[i] > _list[-1]:
        _list.append(_port[i])
    else:
        _list[bisect(_list, _port[i])] = _port[i]
print(len(_list))
