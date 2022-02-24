# 보물
# https://www.acmicpc.net/problem/1026


def solution() :
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a.sort()
    b.sort(reverse = True)

    answer = 0
    for i in range(n) :
        answer += a[i] * b[i]

    print(answer)


solution()
