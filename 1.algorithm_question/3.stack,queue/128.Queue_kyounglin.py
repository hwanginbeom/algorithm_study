# 2021-07-24

# 출처 : https://www.acmicpc.net/problem/18258

# 큐2
import sys
input = sys.stdin.readline
from collections import deque

n=int(input())
queue=deque()

for _ in range(n):
    x=input().split()
    if x[0]=='push':
        queue.append(int(x[1]))
    elif x[0]=='front':
        if len(queue)==0:
            print(-1)
        else:
            print(queue[0])
    elif x[0]=='size':
        print(len(queue))
    elif x[0]=='empty':
        if len(queue)==0:
            print(1)
        else:
            print(0)
    elif x[0]=='pop':
        if len(queue)==0:
            print(-1)
        else:
            print(queue.popleft())
    elif x[0]=='back':
        if len(queue)==0:
            print(-1)
        else:
            print(queue[-1])
