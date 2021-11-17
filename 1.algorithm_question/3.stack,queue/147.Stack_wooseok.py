# 막대기
# https://www.acmicpc.net/problem/17608


def solution() :
    n = int(input())
    stick_list = []

    for _ in range(n) :
        stick_list.append(int(input()))

    stick_list.reverse()

    first = stick_list[0]
    count = 1

    for stick in stick_list :
        if first < stick :
            count += 1
            first = stick

    print(count)


solution()
