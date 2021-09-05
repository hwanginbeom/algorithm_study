# 수식 최대화
# https://programmers.co.kr/learn/courses/30/lessons/67257
# 21.05.02 재풀이
import re
import itertools
import copy


def calc(op, num1, num2):
    if op == '*':
        return num1 * num2
    if op == '+':
        return num1 + num2
    if op == '-':
        return num1 - num2


def solution(expression):
    answer = 0

    num_list = list(map(int, re.split('[*+-]', expression)))
    op_list = re.findall('[*+-]', expression)
    expression_list = []

    for i in range(len(op_list)):
        expression_list.append(num_list[i])
        expression_list.append(op_list[i])

    expression_list.append(num_list[-1])

    # 연산자 우선순위 모든 경우의 수 구하기
    operation = list(set(op_list))
    all_priority_list = list(itertools.permutations(operation, len(operation)))

    # 연산자의 우선순위대로 계산한 값 중 최댓값 구하기
    for priority in all_priority_list:
        expression_list_copy = copy.deepcopy(expression_list)

        for op in priority:
            temp_list = []
            check = -1

            for i in range(len(expression_list_copy)):
                if expression_list_copy[i] == op:
                    result = calc(expression_list_copy[i], temp_list.pop(), expression_list_copy[i + 1])
                    temp_list.append(result)
                    check = i + 1
                else:
                    if i == check:
                        continue

                    temp_list.append(expression_list_copy[i])

            expression_list_copy = copy.deepcopy(temp_list)

        answer = max(answer, abs(expression_list_copy[0]))

    return answer


expression = "100-200*300-500+20"
print(solution(expression))
# 성공
