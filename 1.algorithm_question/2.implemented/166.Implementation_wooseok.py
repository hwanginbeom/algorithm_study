# 단어의 개수
# https://www.acmicpc.net/problem/1152


def solution() :
    s = input()
    split_list = s.split()

    count = 0
    for _ in split_list :
        count += 1

    print(count)


solution()
