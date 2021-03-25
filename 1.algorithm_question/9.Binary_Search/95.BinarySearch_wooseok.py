# 두 용액
# https://www.acmicpc.net/problem/2470


def binary_search(_list) :
    start, end = 0, 0

    start_index = 0
    end_index = len(_list) - 1

    num = 2000000000

    while start_index < end_index :
        mid = _list[start_index] + _list[end_index]

        if abs(num) > abs(mid) :
            start = _list[start_index]
            end = _list[end_index]

            num = mid

        # 한 쪽의 인덱스만 너무 증가하거나 감소하지 않도록
        # 또 다른 기준 생성
        if mid < 0 :
            start_index += 1
        else :
            end_index -= 1

    return start, end


def solution() :
    n = int(input())
    sol = list(map(int, input().split()))

    sol.sort()

    _min, _max = binary_search(sol)
    print('{} {}'.format(_min, _max))


solution()
