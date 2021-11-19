# 큐
# https://www.acmicpc.net/problem/10845
from collections import deque


def solution() :
    n = int(input())
    queue = deque([])
    answer = []

    for _ in range(n) :
        command = input().split()

        if command[0] == 'push' :
            queue.append(command[1])
        elif command[0] == 'pop' :
            result = queue.popleft() if queue else -1
            answer.append(result)
        elif command[0] == 'size' :
            answer.append(len(queue))
        elif command[0] == 'empty' :
            result = 0 if queue else 1
            answer.append(result)
        elif command[0] == 'front' :
            result = queue[0] if queue else -1
            answer.append(result)
        else :
            result = queue[-1] if queue else -1
            answer.append(result)

    for i in answer :
        print(i)


solution()
