# 큐2
# https://www.acmicpc.net/problem/18258
from collections import deque


def solution() :
    n = int(input())
    queue = deque([])
    answer = []

    for _ in range(n) :
        command = input().split()

        if command[0] == 'push' :
            queue.append(int(command[1]))
        elif command[0] == 'pop' :
            if queue :
                answer.append(queue.popleft())
            else :
                answer.append(-1)
        elif command[0] == 'size' :
            answer.append(len(queue))
        elif command[0] == 'empty' :
            if queue :
                answer.append(0)
            else :
                answer.append(1)
        elif command[0] == 'front' :
            if queue :
                answer.append(queue[0])
            else :
                answer.append(-1)
        elif command[0] == 'back' :
            if queue :
                answer.append(queue[-1])
            else :
                answer.append(-1)

    for i in answer :
        print(i)


solution()
