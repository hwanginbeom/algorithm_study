# 균형잡힌 괄호 : (와 )의 갯수가 같은지, u와 v로 나눌 index
def balance(data):
    cnt = 0
    for key, value in enumerate(data):
        if value == '(':
            cnt += 1
        elif value == ')':
            cnt -= 1
        if cnt == 0:
            return key


# 올바른 괄호 : (와 )의 짝이 맞는지
def correct(data):
    cnt = 0
    for i in range(len(data)):
        if data[i] == '(':
            cnt += 1
        else:
            cnt -= 1
        if cnt < 0:
            return False
    return True


def solution(p):
    # 1. 입력이 빈 문자열인 경우, 빈 문자열을 반환
    if p == '':
        return p

    # 2. 균형잡힌 괄호 문자열로, u와 v로 분리한다
    u, v = p[:balance(p)+1], p[balance(p)+1:]

    # 3. u가 올바른 괄호 문자열이라면, v는 1단계부터 다시 수행
    if correct(u):
        string = solution(v)
        return u + string

    # 4. u가 올바른 괄호 문자열이 아니라면,아래 과정을 수행
    else:
        t = '('
        t += solution(v)
        t += ')'

        u = u[1:-1]
        table = str.maketrans('()', ')(')
        u = u.translate(table)

        t += ''.join(u)
        return t

p = "()))((()"
print(solution(p))
