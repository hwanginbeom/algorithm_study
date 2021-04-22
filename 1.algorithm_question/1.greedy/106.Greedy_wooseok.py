# 병든 나이트
# https://www.acmicpc.net/problem/1783


def solution() :
    n, m = map(int, input().split())

    # 세로의 길이가 1 이면 아무런 이동도 할 수 없다.
    if n == 1 :
        count = 1
    # 세로의 길이가 2 이면 가로 길이에 따라 달라진다.
    elif n == 2 :
        count = min(4, (m - 1) // 2 + 1)
    # 세로의 길이가 3 이상이면
    # 가로의 길이가 7보다 작으면 4가지 경로를 모두 이용할 수 없으므로
    # 조건의 기준이 된다.
    elif m < 7 :
        count = min(4, m)
    else :
        count = (2 + (m - 5)) + 1

    print(count)


solution()
