# 11650 문제 - 좌표정렬
import sys

def quick_sort(array):
    if len(array) <= 1:
        return array
    pivot = array[0]
    tail = array[1:]
    left_side = [x for x in tail if x <= pivot] # 분할된 왼쪽 부분
    right_side = [x for x in tail if x > pivot] # 분할된 오른쪽 부분
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬수행하고 , 전체 리스트 반환
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)


N = int(input())

numbers = []
for i in range(N):
    numbers.append(list(map(int, input().split())))

sort_value = quick_sort(numbers)
for i in range(N):
    print(sort_value[i][0], sort_value[i][1])


    
# 11650 문제 - 좌표정렬2

import sys

def quick_sort(array):
    if len(array) <= 1:
        return array
    pivot = array[0]
    tail = array[1:]
    left_side = [x for x in tail if x <= pivot] # 분할된 왼쪽 부분
    right_side = [x for x in tail if x > pivot] # 분할된 오른쪽 부분
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬수행하고 , 전체 리스트 반환
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)


N = int(input())

numbers = []
for i in range(N):
    [a, b] = map(int, input().split())
    numbers.append([b,a])

sort_value = quick_sort(numbers)
for i in range(N):
    print(sort_value[i][1], sort_value[i][0])