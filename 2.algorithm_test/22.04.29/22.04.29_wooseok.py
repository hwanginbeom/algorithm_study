import re, copy
from itertools import permutations
from collections import deque


def calc(num1, num2, op):
    if op == '+':
        return num1 + num2
    elif op == '-':
        return num1 - num2
    else:
        return num1 * num2


def solution(expression):
    answer = 0

    op_list = list(re.sub('[0-9]', '', expression))

    # 식에 있는 모든 연산자의 우선순위 경우의 수 구하기
    priority_op_list = list(permutations(list(set(op_list)), len(list(set(op_list)))))

    num_list = list(re.sub('[^0-9]', ' ', expression).split(' '))

    # 식에서 숫자와 연산자 나누기
    ex_list = deque([])
    for i in range(len(op_list)):
        ex_list.append(num_list[i])
        ex_list.append(op_list[i])

    ex_list.append(num_list[-1])
    ex_list_copy = copy.deepcopy(ex_list)

    result_list = []

    # 정해진 우선순위마다 결과를 구해서 최대값 구하기
    for op in priority_op_list:

        for j in range(len(op)):
            stack = []

            while ex_list:
                temp = ex_list.popleft()

                if temp == op[j]:
                    num1 = stack.pop()
                    num2 = ex_list.popleft()

                    stack.append(calc(int(num1), int(num2), op[j]))
                else:
                    stack.append(temp)

            ex_list = deque(copy.deepcopy(stack))

        result_list.append(abs(stack.pop()))
        ex_list = deque(copy.deepcopy(ex_list_copy))

    answer = max(result_list)
    return answer


expression = "100-200*300-500+20"
print(solution(expression))
