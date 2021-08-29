# 괄호 변환
# https://programmers.co.kr/learn/courses/30/lessons/60058
# 21.04.18 재풀이


def divide_str(string):
    if not string:
        return string

    count_left = 0
    count_right = 0

    for i in range(len(string)):
        if string[i] == '(':
            count_left += 1
        else:
            count_right += 1

        if count_left == count_right:
            u = string[:(i + 1)]
            v = string[(i + 1):]

            return u, v


def is_correct(string):
    stack = []

    for s in string:
        if stack:
            temp = stack.pop()

            if temp == '(' and s == ')':
                continue
            else:
                stack.append(temp)
                stack.append(s)
        else:
            stack.append(s)

    if not stack:
        return True
    else:
        return False


def solution(p):
    if not p :
        return p

    u, v = divide_str(p)

    if is_correct(u):
        if is_correct(v):
            return u + v
        else:
            return u + solution(v)
    else:
        temp_str = '('
        temp_str += solution(v)
        temp_str += ')'

        u = u[1:-1]
        temp = ''
        for i in u :
            if i == '(' :
                temp += ')'
            else :
                temp += '('

        temp_str += temp

        return temp_str


# p = "(()())()"
# p = ")("
p = "()))((()"
print(solution(p))
# 반성공
