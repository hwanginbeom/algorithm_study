# 수식 최대화
# https://programmers.co.kr/learn/courses/30/lessons/67257
import itertools


def operation(num1, num2, op):
    if op == '+':
        return str(int(num1) + int(num2))
    if op == '-':
        return str(int(num1) - int(num2))
    if op == '*':
        return str(int(num1) * int(num2))


def calculate(expression, op):
    cal_tmp = []
    number = ''

    # 수식에서 숫자와 연산자를 분리
    for i in expression:
        if i not in op:
            number += i
        else :
            cal_tmp.append(number)
            number = ''

            cal_tmp.append(i)

    # 마지막에 남는 숫자 넣기
    cal_tmp.append(number)

    result = []
    stack = []

    for o in op:
        while True:
            if len(cal_tmp) == 0:
                break

            tmp = cal_tmp.pop(0)

            # 숫자와 연산자를 차례대로 뽑아내어
            # 우선순위가 높은 연산자에 해당하면 해당 연산을 수행한 후 저장
            if tmp == o:
                stack.append(operation(stack.pop(-1), cal_tmp.pop(0), o))
            # 아니라면 그냥 저장
            else:
                stack.append(tmp)

        result.append(stack)
        cal_tmp = stack
        stack = []

    # 가장 마지막으로 수행되어 저장되는 결과값 반환
    return result[-1][0]


def solution(expression):
    answer = 0

    op = ['+', '-', '*']
    op = list(itertools.permutations(op, 3))

    for i in op:
        answer = max(answer, abs(int(calculate(expression, i))))

    return answer


expression = "100-200*300-500+20"
print(solution(expression))
