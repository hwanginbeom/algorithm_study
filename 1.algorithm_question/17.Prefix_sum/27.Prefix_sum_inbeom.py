#11659 구간 합 구하기 4
import sys

n, m = map(int, input().split())

data = list(map(int, sys.stdin.readline().split()))

sum_value = 0
prefix_sum = [0]
for i in data:
    sum_value += i
    prefix_sum.append(sum_value)

for _ in range(m):
    left, right = map(int, sys.stdin.readline().split())
    print(prefix_sum[right] - prefix_sum[left - 1])



# 11660 구간 합 구하기 5

import sys

n, m = map(int, input().split())
matrix_list = []
for _ in range(n):
    data = list(map(int, sys.stdin.readline().split()))
    matrix_list.append(data)

sum_value = 0
prefix_sum = []

for i in range(n):
    sum_value = 0

    array_list = []
    for j in matrix_list[i]:
        sum_value += j
        array_list.append(sum_value)
    else:
        prefix_sum.append(array_list)
for _ in range(m):
    data = list(map(int, sys.stdin.readline().split()))
    sum = 0
    for i in range(data[0]-1,data[2]):
        if data[1] == 1:
            sum += prefix_sum[i][data[3]-1]
        else:
            sum += prefix_sum[i][data[3]-1] - prefix_sum[i][data[1]-2]
    else:
        print(sum)
