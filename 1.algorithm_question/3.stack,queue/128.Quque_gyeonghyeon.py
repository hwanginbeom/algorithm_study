from collections import deque
import sys

input=sys.stdin.readline
n = int(input())

stack = deque()

def solution(x):
    if x[0] == 'push':
        stack.append(x[1])
    elif x[0] == 'pop':
        if len(stack) > 0:
            print(stack[0])
            stack.popleft()
        else:
            print(-1)
    elif x[0] == 'size':
        print(len(stack))
    elif x[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif x[0] == 'front':
        if len(stack) > 0:
            print(stack[0])
        else:
            print(-1)
    else:
        if len(stack) > 0:
            print(stack[-1])
        else:
            print(-1)


for i in range(n):
    text = input().split()
    solution(text)