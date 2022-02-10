# 소수 찾기
# https://www.acmicpc.net/problem/1978
import math


def is_prime(n) :
    if n == 1 :
        return False

    for i in range(2, int(math.sqrt(n)) + 1) :
        if n % i == 0 :
            return False

    return True


def solution() :
    n = int(input())
    num_list = list(map(int, input().split()))
    count = 0

    for num in num_list :
        if is_prime(num) :
            count += 1

    print(count)


solution()
