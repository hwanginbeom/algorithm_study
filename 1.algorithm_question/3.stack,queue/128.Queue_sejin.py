# 큐 : 선입선출
import sys
input = sys.stdin.readline

n = int(input())
from collections import deque
queue = deque()

for _ in range(n):
    data = input().split()

    # push : x를 큐에 넣는 연산
    if data[0] == 'push':
        queue.append(data[1])

    # pop : 큐 가장 앞 정수 빼고 출력, 큐에 들어있는 정수가 없는 경우 -1 출력
    elif data[0] == 'pop':
        if len(queue) != 0:
            print(queue.popleft())
        else:
            print(-1)

    # size : 큐에 들어있는 정수 개수 출력
    elif data[0] == 'size':
        print(len(queue))

    # empty : 큐가 비어있으면 1, 아니면 0 출력
    elif data[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)

    # front : 큐 가장 앞 정수 출력, 큐에 들어있는 정수가 없는 경우 -1
    elif data[0] == 'front':
        if len(queue) != 0:
            print(queue[0])
        else:
            print(-1)

    # back : 큐 가장 뒤 정수 출력, 큐에 들어있는 정수가 없는 경우 -1
    elif data[0] == 'back':
        if len(queue) != 0:
            print(queue[-1])
        else:
            print(-1)