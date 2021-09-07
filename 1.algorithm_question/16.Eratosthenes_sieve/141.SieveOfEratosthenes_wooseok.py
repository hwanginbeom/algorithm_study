# 소수 구하기
# https://www.acmicpc.net/problem/1929
import math


def solution() :
    n, m = map(int, input().split())
    num_list = [True for _ in range(m + 1)]
    num_list[1] = False

    for i in range(2, int(math.sqrt(m)) + 1) :
        if num_list[i] :
            j = 2

            while i * j <= m :
                num_list[i * j] = False
                j += 1

    for i in range(n, m + 1) :
        if num_list[i] :
            print(i)


solution()
