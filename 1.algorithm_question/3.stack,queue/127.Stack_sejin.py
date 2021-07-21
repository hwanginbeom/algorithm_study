import sys
input = sys.stdin.readline

n = int(input()) # n:명령수
stack = []

for _ in range(n):
    data = input().split()

    # push : 스택 넣기
    if data[0] == 'push':
        stack.append(data[1])

    # pop : 스택 가장 위 정수 빼고 그 수 출력, 없으면 -1 출력
    elif data[0] == 'pop':
        if len(stack) != 0:
            print(stack.pop())
        else:
            print(-1)

    # size : 스택에 들어있는 정수 개수 출력
    elif data[0] == 'size':
        print(len(stack))

    # empty : 스택 비어있으면 1, 아니면 0 출력
    elif data[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)

    # top : 스택 가장 위 정수 출력, 없으면 -1 출력
    elif data[0] == 'top':
        if len(stack) != 0:
            print(stack[-1])
        else:
            print(-1)

