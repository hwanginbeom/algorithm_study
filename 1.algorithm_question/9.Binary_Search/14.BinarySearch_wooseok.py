# 1-1
def solution1_1() :
    n = int(input())
    arr = list(map(int, input().split()))

    m = int(input())
    find = list(map(int, input().split()))

    for i in find :
        if i in arr :
            print(1)
        else :
            print(0)


# solution1_1()



# 1-2
def binary_search(arr, target, start, end) :
    while start <= end :
        mid = (start + end) // 2

        if arr[mid] == target :
            return mid
        elif arr[mid] >= target :
            end = mid - 1
        else :
            start = mid + 1

    return None


def solution1_2() :
    n = int(input())
    arr = list(map(int, input().split()))

    arr.sort()

    m = int(input())
    find = list(map(int, input().split()))

    for i in find :
        result = binary_search(arr, i, 0, n - 1)
        if result is None :
            print(0)
        else :
            print(1)


# solution1_2()



# 2
from bisect import bisect_left, bisect_right


def count_by_range(arr, left_value, right_value) :
    left_index = bisect_left(arr, left_value)
    right_index = bisect_right(arr, right_value)

    return right_index - left_index


def solution2() :
    n = int(input())
    card = list(map(int, input().split()))

    card.sort()

    m = int(input())
    find = list(map(int, input().split()))

    for i in find :
        print(count_by_range(card, i, i))


solution2()
