# 국영수
# https://www.acmicpc.net/problem/10825


def solution() :
    n = int(input())
    info_list = []

    for _ in range(n) :
        info = list(input().split())
        info_list.append(info)

    sorted_list = sorted(info_list, key = lambda x : (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

    for i in sorted_list :
        print(i[0])


solution()
