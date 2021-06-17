# 기상청 인턴 신현수
# https://www.acmicpc.net/problem/2435


def solution() :
    n, k = map(int, input().split())
    temp_list = list(map(int, input().split()))

    prefix_sum = [0]
    _sum = 0
    for i in temp_list :
        _sum += i
        prefix_sum.append(_sum)

    temp_sum_list = []
    for i in range(k, len(prefix_sum)) :
        temp_sum_list.append(prefix_sum[i] - prefix_sum[i - k])

    print(max(temp_sum_list))


solution()
