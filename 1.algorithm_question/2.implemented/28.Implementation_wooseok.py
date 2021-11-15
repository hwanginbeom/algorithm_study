# 연산자 끼워넣기
# https://www.acmicpc.net/problem/14888
from itertools import permutations


def calculate(op, a, b) :
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        if a < 0 :
            a *= -1
            return a // b * -1
        else :
            return a // b


def solution() :
    n = int(input())
    num_list = list(map(int, input().split()))
    op_count_list = list(map(int, input().split()))
    op_list = []
    operator = ['+', '-', '*', '/']
    count = 0

    for i in op_count_list :
        for j in range(i) :
            op_list.append(operator[count])
        count += 1

    op_combi = list(permutations(op_list, len(op_list)))

    max_value = -1000000000
    min_value = 1000000000
    for op_tuple in op_combi :
        total = num_list[0]
        for i in range(len(op_tuple)) :
            total = calculate(op_tuple[i], total, num_list[i + 1])

        max_value = max(max_value, total)
        min_value = min(min_value, total)

    print(max_value)
    print(min_value)


solution()
