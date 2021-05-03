# Kakao Intern Coding Test
# 수식 최대화
# https://programmers.co.kr/learn/courses/30/lessons/67257

# 구분자 단위로 쪼개어 우선순위에 따라 계산하는 함수
def calc(priority, n, expression):
    # priority 연산자 우선순위 모음 / n 우선순위 --> 낮은 것부터 0, 1, 2 / expression 더 낮은 우선순위에서 쪼개진 식 문자열
    # 가장 높은 우선순위에 도달하면 계산
    if n == 2:
        return str(eval(expression))    # eval : str 입력값을 그 자체로 계산
    # 먼저 쪼갠 부분부터 계산
    if priority[n] == '*':
        # 결과를 재귀적으로 호출하여 모든 부호를 구분자로 쪼개어 순서대로 계산하고 res 에 저장
        res = eval('*'.join([calc(priority, n + 1, e) for e in expression.split('*')]))
    if priority[n] == '+':
        res = eval('+'.join([calc(priority, n + 1, e) for e in expression.split('+')]))
    if priority[n] == '-':
        res = eval('-'.join([calc(priority, n + 1, e) for e in expression.split('-')]))
    return str(res)

def solution(expression):
    # 초기값 설정
    answer = 0
    # 가능한 모든 연산 우선순위
    priorities = [
        ('*', '-', '+'),
        ('*', '+', '-'),
        ('+', '*', '-'),
        ('+', '-', '*'),
        ('-', '*', '+'),
        ('-', '+', '*')
    ]
    # 모든 연산 우선순위 경우를 적용시켜 최댓값 도출
    for priority in priorities:
        res = int(calc(priority, 0, expression))
        answer = max(answer, abs(res))

    return answer