# 안정적인 문자열
# https://www.acmicpc.net/problem/4889


def solution() :
    answer = []
    count = 1

    while True :
        string = input()
        if '-' in string :
            break

        cnt = 0
        stack = []

        for i in string :
            if i == '{' :
                stack.append(i)
            else :
                if stack :
                    stack.pop()
                else :
                    cnt += 1
                    stack.append('{')

        if stack :
            cnt += len(stack) // 2

        answer.append([count, cnt])
        count += 1

    for i in answer :
        print('{}. {}'.format(i[0], i[1]))


solution()
