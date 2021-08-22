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
                except:
                    food[''.join(i2)] = 1
        food = dict(filter(lambda x:x[1] == max(food.values()), food.items()))
        for idx in food.keys():
            answer[idx] = max(food.values())
    answer = dict(filter(lambda x:x[1] >= 2, answer.items()))
    answer = [ i[0] for i in sorted(answer.items(), key=lambda x : (x[0],x[1]),reverse=False)]
    return answer