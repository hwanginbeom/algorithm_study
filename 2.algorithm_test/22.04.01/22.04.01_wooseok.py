# 괄호 변환
# https://programmers.co.kr/learn/courses/30/lessons/60058
from collections import deque


def is_correct(string):
    stack = []

    for i in string:
        stack.append(i)

        if len(stack) > 1:
            if stack[-1] == ')' and stack[-2] == '(':
                stack.pop()
                stack.pop()

    if stack:
        return False
    else:
        return True


def solution(p):
    answer = ''

    if not p:
        return answer

    str_list = deque(list(p))
    u = []

    while True:
        u.append(str_list.popleft())

        left = u.count('(')
        right = u.count(')')

        if left == right:
            break

    u = ''.join(u)
    v = ''.join(str_list)

    if is_correct(u):
        v = solution(v)
        return u + v
    else:
        new_string = '('
        v = solution(v)
        new_string += v + ')'

        u = u[1:-1]
        for i in range(len(u)):
            if u[i] == '(':
                new_string += ')'
            else:
                new_string += '('

        return new_string


p = "(()())()"
print(solution(p))
