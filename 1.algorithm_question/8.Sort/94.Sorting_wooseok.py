# 접미사 배열
# https://www.acmicpc.net/problem/11656


def solution() :
    s = input()

    _list = []
    for i in range(len(s)) :
        _list.append(s[i:])

    _list.sort()

    for i in _list :
        print(i)


solution()
