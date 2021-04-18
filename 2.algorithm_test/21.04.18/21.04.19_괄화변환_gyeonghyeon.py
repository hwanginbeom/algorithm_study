def check(p):
    sum = 0
    for i in p:
        if i == '(':
            sum += 1
        else:
            sum -= 1
            if sum < 0:
                return False
    return sum == 0


def seperate(p):
    sum = r = 0
    for i in range(len(p)):
        if p[i] == '(':
            sum += 1
        else:
            r += 1
        if sum > 0 and sum == r:
            return p[:i+1], p[i+1:]


def solution(p):
    if p == '':
        return p
    u, v = seperate(p)
    if check(u):
        return u + solution(v)
    return f"({solution(v)}){''.join([i == ')' and '(' or ')' for i in u[1:-1]])}"

