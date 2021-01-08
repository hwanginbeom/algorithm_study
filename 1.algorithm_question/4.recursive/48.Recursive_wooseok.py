# 피보나치 수 5
import sys


def fibo(n) :
    if n == 0 :
        return 0

    if n == 1 :
        return 1

    return fibo(n - 1) + fibo(n - 2)


def solution() :
    sys.setrecursionlimit(10 ** 7)

    n = int(input())
    print(fibo(n))


solution()
