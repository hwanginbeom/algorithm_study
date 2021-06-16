# 세 개의 소수 문제
# https://www.acmicpc.net/problem/11502
import math


def check(n, _list) :
    for i in range(2, len(_list)):
        if not _list[i]:
            continue
        for j in range(2, len(_list)):
            if not _list[j]:
                continue
            for k in range(2, len(_list)):
                if not _list[k]:
                    continue

                if n == i + j + k:
                    return [i, j, k]

    return 0


def solution() :
    t = int(input())
    answer = []

    for _ in range(t) :
        n = int(input())

        _list = [True for _ in range(n + 1)]

        for i in range(2, int(math.sqrt(n)) + 1):
            if _list[i] is True:
                j = 2
                while i * j <= n:
                    _list[i * j] = False
                    j += 1

        answer.append(check(n, _list))

    for i in answer :
        if len(i) == 3 :
            print(i[0], i[1], i[2])
        else :
            print(0)


solution()
