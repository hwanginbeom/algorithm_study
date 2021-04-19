# 괄호 변환
# https://programmers.co.kr/learn/courses/30/lessons/60058

# 균형잡힌 문자열인지 확인
def is_balance(string):
    if string.count('(') == string.count(')'):
        return True
    else: return False

# 올바른 문자열인지 확인
def is_correct(string):
    stack = []
    for s in string:
        if s == '(':
            stack.append(s)
        elif stack:
            stack.pop()
    # 비어있으면 True, 원소가 있으면 False
    return not stack

# 문자열을 뒤집기
def reverse(string):
    result = ''
    for s in string:
        if s == '(': result += ')'
        else: result += '('
    return result

def solution(p):
    u, v, answer = '', '', ''
    # 올바른 문자열이면 결과로 반환
    if is_correct(p): return p
    # 2단계. 첫 문자부터 확인해가며 최소한의 균형잡힌 문자열을 u, 나머지를 v로 반환
    for i in range(2, len(p) + 1):
        if is_balance(p[:i]):
            u, v = p[:i], p[i:]
            break
    # 3단계. u가 올바른 문자열이면 완료 처리하고 v를 재귀적으로 수행
    if is_correct(u):
        answer = u + solution(v)
    # 4단계. 올바른 문자열이 아닌 경우
    else:
        answer += '(' + solution(v) + ')' + reverse(u[1:-1])
    return answer