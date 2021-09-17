# 주몽
# https://www.acmicpc.net/problem/1940


def solution() :
    n = int(input())
    m = int(input())
    num_list = list(map(int, input().split()))

    num_list.sort()
    start, end = 0, n - 1
    count = 0

    while start < end :
        total = num_list[start] + num_list[end]

        if total == m :
            count += 1
            end -= 1
        else :
            if total < m :
                start += 1
            else :
                end -= 1

    print(count)


solution()
