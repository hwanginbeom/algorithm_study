import sys

input = sys.stdin.readline


def solution():
    n = int(input())
    a = sorted(list(map(int, input().split())))
    b = sorted(list(map(int, input().split())), reverse=True)
    answer = 0
    for idx, value in enumerate(a):
        answer += value * b[idx]
    print(answer)
    return answer


solution()
