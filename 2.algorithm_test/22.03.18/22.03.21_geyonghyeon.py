from itertools import combinations
import sys

input = sys.stdin.readline


def solution(orders, course):
    answer = {}
    for n in course:
        food = {}
        for i in orders:
            combi = list(combinations(sorted(i), n))
            for i2 in combi:
                try:
                    food[''.join(i2)] += 1
                except KeyError:
                    food[''.join(i2)] = 1
        food = {idx: value for idx, value in food.items() if value == max(food.values())}
        answer = {**answer, **food}
    answer = {idx: value for idx, value in answer.items() if value >= 2}
    answer = [i[0] for i in sorted(answer.items(), key=lambda x: (x[0], x[1]), reverse=False)]
    return answer


orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course = [2, 3, 4]

solution(orders, course)
