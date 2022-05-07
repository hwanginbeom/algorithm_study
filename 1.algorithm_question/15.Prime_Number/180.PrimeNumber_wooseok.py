# 소인수분해
# https://www.acmicpc.net/problem/11653
import math


def solution() :
    n = int(input())

    sieve = [True for _ in range(n + 1)]

    for i in range(2, int(math.sqrt(n + 1))) :
        if sieve[i] :
            j = 2

            while i * j <= n :
                sieve[i * j] = False
                j += 1

    prime_factor = []
    isFlag = False

    while True :
        if n == 1 :
            break

        for i in range(2, len(sieve) + 1) :
            if n == i :
                prime_factor.append(i)
                isFlag = True
                break

            if sieve[i] :
                if n % i == 0 :
                    n = n // i
                    prime_factor.append(i)
                    break

        if isFlag :
            break

    prime_factor.sort()

    for i in prime_factor :
        print(i)


solution()
