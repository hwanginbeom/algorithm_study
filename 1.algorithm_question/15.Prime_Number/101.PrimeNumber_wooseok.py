# 골드바흐 파티션
# https://www.acmicpc.net/problem/17103
import math


def solution() :
    t = int(input())

    answer = []
    for _ in range(t) :
        n = int(input())
        _list = [True for i in range(n + 1)]

        for i in range(2, int(math.sqrt(n)) + 1) :
            if _list[i] :
                j = 2

                while i * j <= n :
                    _list[i * j] = False
                    j += 1

        count = 0
        center = n // 2

        if _list[center] :
            count += 1

        left = center - 1
        right = center + 1
        while True :
            if left == 1 :
                break

            if _list[left] and _list[right] :
                count += 1

            left -= 1
            right += 1

        answer.append(count)

    for i in answer :
        print(i)


solution()
