## 수 찾기

n = int(input())

n_nums = list(map(int, input().split()))
n_nums.sort()

m = int(input())
m_nums = list(map(int, input().split()))

answer_list = [0] * m

def binary_search(array, target, start, end):
    if start > end:
        return 0
    mid = (start + end) // 2

    if array[mid] == target:
        return 1

    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid + 1, end)


for idx , num in enumerate(m_nums):
    if binary_search(n_nums, num, 0, n-1) == 1:
        answer_list[idx] += 1

for answer in answer_list:
    print(answer, end = " ")


## 숫자 카드 2

from bisect import bisect_left, bisect_right

def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index


n = int(input())

n_nums = list(map(int, input().split()))
n_nums.sort()

m = int(input())
m_nums = list(map(int, input().split()))

for i in m_nums:
    cnt = count_by_range(n_nums, i,i )
    print(cnt, end= " ")