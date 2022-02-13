import math
import sys

input = sys.stdin.readline
sys.setrecursionlimit(100000000)


def is_prime_number(x):
    if x == 1:
        return False
    else:
        for i in range(2, int(math.sqrt(x)) + 1):
            if x % i == 0:
                return False
        return True


def dfs(x, n, end_number):
    if len(x) == n:
        print(x)
        return
    for j in end_number:
        if is_prime_number(int(x + j)):
            dfs(x + j, n, end_number)


def solution():
    n = int(input())
    start_list = ['2', '3', '5', '7']
    end_list = ['1', '3', '7', '9']
    for i in start_list:
        dfs(i, n, end_list)


solution()
