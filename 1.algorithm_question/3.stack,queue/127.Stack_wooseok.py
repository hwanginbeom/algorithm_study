# 스택
# https://www.acmicpc.net/problem/10828


def solution() :
    n = int(input())
    stack = []
    answer = []

    for _ in range(n) :
        command = input().split()

        if command[0] == 'push' :
            stack.append(command[1])
        elif command[0] == 'pop' :
            if stack :
                answer.append(stack.pop())
            else :
                answer.append(-1)
        elif command[0] == 'size' :
            answer.append(len(stack))
        elif command[0] == 'empty' :
            if stack :
                answer.append(0)
            else :
                answer.append(1)
        elif command[0] == 'top' :
            if stack :
                answer.append(stack[-1])
            else :
                answer.append(-1)

    for i in answer :
        print(i)


solution()
