# 개똥벌레
# https://www.acmicpc.net/problem/3020


def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if array[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    return start


def solution() :
    n, h = map(int, input().split())

    stalagmite = [] # 석순
    stalactite = [] # 종유석

    for i in range(n) :
        stone = int(input())

        if i % 2 == 0 :
            stalagmite.append(stone)
        else :
            stalactite.append(stone)

    stalagmite.sort()
    stalactite.sort()

    _min = n
    count = 0

    for i in range(1, h + 1) :
        up = binary_search(stalagmite, i - 0.5, 0, len(stalagmite) - 1)
        down = binary_search(stalactite, h - i + 0.5, 0, len(stalactite) - 1)

        # 시간초과 원인
        # _sum = len(stalagmite[up:]) + len(stalactite[down:])

        _sum = len(stalagmite) - up + len(stalactite) - down

        if _min == _sum :
            count += 1
        elif _min > _sum :
            count = 1
            _min = _sum

    print(_min, count)


solution()
