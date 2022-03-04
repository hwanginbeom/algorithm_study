# 문자열 폭발
# https://www.acmicpc.net/problem/9935
import re


def solution() :
    s = input()
    bomb = input()

    # 시간 초과
    # while True :
    #     new_string = re.sub(bomb, '', s)
    #     if new_string == s :
    #         break
    #
    #     s = new_string

    stack = []
    bomb_length = len(bomb)
    for i in range(len(s)) :
        stack.append(s[i])

        if len(stack) >= bomb_length :
            if ''.join(stack[len(stack) - bomb_length:]) == bomb :
                for _ in range(bomb_length) :
                    stack.pop()

    if stack :
        print(''.join(stack))
    else :
        print('FRULA')


solution()
