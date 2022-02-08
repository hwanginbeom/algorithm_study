# 신기한 소수
# https://www.acmicpc.net/problem/2023
import math


def is_prime(n) :
    for i in range(2, int(math.sqrt(n)) + 1) :
        if n % i == 0 :
            return False

    return True


def dfs(n, num) :
    if len(str(num)) == n :
        print(num)
    else :
        for i in range(10) :
            new_num = num * 10 + i

            if is_prime(new_num) :
                dfs(n, new_num)


def solution() :
    n = int(input())
    prime_list = [2, 3, 5, 7]

    for i in prime_list :
        dfs(n, i)


solution()
