# 소수 사이 수열
# https://www.acmicpc.net/problem/3896
import math


def solution() :
    t = int(input())
    num_list = []

    for _ in range(t) :
        num_list.append(int(input()))

    sieve = [True for _ in range(1299709 + 1)]

    for i in range(2, int(math.sqrt(1299709 + 1))):
        if sieve[i]:
            j = 2

            while i * j <= 1299709:
                sieve[i * j] = False
                j += 1

    answer = []

    for num in num_list :
        check = 0

        for i in range(len(sieve)) :
            if sieve[i] :
                if num == i :
                    answer.append(0)
                    break
                elif num < i :
                    answer.append(i - check)
                    break

            if sieve[i] :
                check = i

    for i in answer :
        print(i)


solution()
