# Moo 게임
# https://www.acmicpc.net/problem/5904
import sys, math
sys.setrecursionlimit(10 ** 7)


def moo(n) :
    string = ''

    if n == 0 :
        return 'moo'
    else :
        string += moo(n - 1)
        string += 'm' + 'o' * (n + 2)
        string += moo(n - 1)

        return string


def solution() :
    n = int(input())

    s = moo(int(math.sqrt(n)))
    print(s[n - 1])


solution()
