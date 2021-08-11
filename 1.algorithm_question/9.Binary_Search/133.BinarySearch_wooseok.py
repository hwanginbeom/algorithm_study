# 반도체 설계
# https://www.acmicpc.net/problem/2352
from bisect import bisect_left


def solution() :
    n = int(input())
    port_list = list(map(int, input().split()))
    max_list = []

    for port in port_list :
        if not max_list or max_list[-1] < port :
            max_list.append(port)
        else :
            max_list[bisect_left(max_list, port)] = port

    print(len(max_list))


solution()
