# 베르트랑 공준
# https://www.acmicpc.net/problem/4948
import math


def is_prime_number(n) :
    count = 0

    for i in range(n + 1, 2 * n + 1) :
        isFlag = True

        for j in range(2, int(math.sqrt(i)) + 1) :
            if i % j == 0 :
                isFlag = False
                break

        if isFlag :
            count += 1

    return count


def solution() :
    answer = []

    while True :
        n = int(input())

        if n == 0 :
            break
        else :
            answer.append(is_prime_number(n))

    for i in answer :
        print(i)


solution()
