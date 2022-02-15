# 수열
# https://www.acmicpc.net/problem/2559


def solution() :
    n, k = map(int, input().split())
    temp_list = list(map(int, input().split()))

    sum_list = []
    sum_value = 0

    for i in range(k) :
        sum_value += temp_list[i]

    sum_list.append(sum_value)

    for i in range(k, n) :
        sum_value = sum_value + temp_list[i] - temp_list[i - k]
        sum_list.append(sum_value)

    print(max(sum_list))


solution()
