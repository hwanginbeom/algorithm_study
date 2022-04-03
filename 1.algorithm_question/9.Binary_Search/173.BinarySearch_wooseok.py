# 구간 나누기 2
# https://www.acmicpc.net/problem/13397


def divide_part(arr, n, x) :
    max_value = arr[0]
    min_value = arr[0]
    cnt = 1

    for i in range(1, n) :
        max_value = max(max_value, arr[i])
        min_value = min(min_value, arr[i])

        if max_value - min_value > x :
            cnt += 1
            max_value = arr[i]
            min_value = arr[i]

    return cnt


def solution() :
    n, m = map(int, input().split())
    num_list = list(map(int, input().split()))

    start = 0
    end = max(num_list)
    result = 0

    while start <= end :
        mid = (start + end) // 2

        if divide_part(num_list, n, mid) <= m :
            end = mid - 1
            result = mid
        else :
            start = mid + 1

    print(result)


solution()
# 아직도 잘 모르겠다...
