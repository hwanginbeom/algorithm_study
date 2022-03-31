import sys

input = sys.stdin.readline


def solution():
    answer = {}
    n = int(input())
    for _ in range(n):
        name, korea, eng, math = list(input().split())
        answer[name] = {'korea': int(korea), 'eng': int(eng), 'math': int(math)}
    answer = list(dict(sorted(answer.items(), key=lambda x: (-x[1]['korea'], x[1]['eng'], -x[1]['math'], x[0]))).keys())
    print('\n'.join(answer))


solution()
