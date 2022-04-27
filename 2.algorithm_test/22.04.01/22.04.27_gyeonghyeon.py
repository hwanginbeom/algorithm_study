def check(p):
    sum_num = 0
    for i in p:
        if i == '(':
            sum_num += 1
        else:
            sum_num -= 1
            if sum_num < 0:
                return False
    return sum_num == 0


def separate(p):
    left, right = 0, 0
    for idx, value in enumerate(p):
        if value == '(':
            left += 1
        else:
            right += 1
        if left > 0 and left == right:
            return p[:idx + 1], p[idx + 1:]


def solution(p):
    if p == '':
        return p
    u, v = separate(p)
    if check(u):
        return u + solution(v)
    for i in u[1:-1]:
        if (i == ')' and '(') or ')':
            print(i)
    return f"({solution(v)}){''.join([i == ')' and '(' or ')' for i in u[1:-1]])}"


p = "()))((()"
print(solution(p))
