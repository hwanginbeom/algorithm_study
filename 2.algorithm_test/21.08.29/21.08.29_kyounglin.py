# 2021-08-31

# 출처 : https://programmers.co.kr/learn/courses/30/lessons/60058

# 괄호 변환

w = '()))((()'


# u,v를 분리하는 함수
def sep(w):
    left = 0
    right = 0
    for i in range(len(w)):
        if w[i] == '(':
            left += 1
        else:
            right += 1

        if left == right:
            return w[:i + 1], w[i + 1:]


# u가 올바른 괄호 문자열인지 확인하는 함수

def balance(u):
    stack = []

    for j in u:
        if j == '(':
            stack.append(j)
        else:
            if not stack:  # stack이 비어있음
                return False
            stack.pop()

    return True


# 문제 풀이

def solution(w):
    answer = ''

    # 순서1
    if w == '':
        return ''

    # 순서2
    u, v = sep(w)

    # 순서3
    if balance(u):
        # 순서3-1
        return u + solution(v)
    # 순서4
    else:
        # 순서4-1
        answer += '('
        # 순서4-2
        answer += solution(v)
        # 순서4-3
        answer += ')'
        # 순서4-4
        for k in u[1:len(u) - 1]:
            if k == '(':
                answer += ')'
            else:
                answer += '('
    # 순서4-5
    return answer


print(solution(w))