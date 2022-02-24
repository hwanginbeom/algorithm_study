import sys

input = sys.stdin.readline

import sys

input = sys.stdin.readline


def solution1():
    n = int(input())
    a = sorted(list(map(int, input().split())))
    b = {f'{value}-{idx}': [value, idx] for idx, value in enumerate(list(map(int, input().split())))}
    b = dict(sorted(b.items(), key=lambda x: x[1][0], reverse=True))
    b = {value[0]: [*value[1], idx] for idx, value in enumerate(b.items())}
    b = dict(sorted(b.items(), key=lambda x: x[1][1]))
    answer = 0
    for key, value in b.items():
        answer += value[0] * a[value[2]]
    print(answer)
    return answer


solution1()



def solution2():
    n = int(input())
    a = sorted(list(map(int, input().split())))
    b = sorted(list(map(int, input().split())), reverse=True)
    answer = 0
    for idx, value in enumerate(a):
        answer += value * b[idx]
    print(answer)
    return answer


solution2()
