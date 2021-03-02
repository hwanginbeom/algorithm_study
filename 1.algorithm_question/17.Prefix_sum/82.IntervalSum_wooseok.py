# 수열
def solution() :
    n, k = map(int, input().split())
    temp_list = list(map(int, input().split()))

    prefix_sum = [0]
    _sum = 0

    # 접두사 합 구하기
    for temp in temp_list :
        _sum += temp
        prefix_sum.append(_sum)

    temp_sum_list = []

    # 접두사 합으로 구간합 구하기
    for i in range(len(prefix_sum) - k) :
        x = prefix_sum[i + k] - prefix_sum[i]
        temp_sum_list.append(x)

    print(max(temp_sum_list))


solution()
