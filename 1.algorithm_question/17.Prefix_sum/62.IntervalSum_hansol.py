# 9. 기타 알고리즘
# 누적합 (부분합, 접두사 합, Prefix Sum)
# https://www.acmicpc.net/problem/11441

# input() 이 시간초과로 오래 걸린다면 sys.stdin.readline() 을 사용하여 시간을 줄일 수 있다.

import sys

N = sys.stdin.readline()

data = list(map(int, sys.stdin.readline().split()))

# Prefix Sum 배열 계산
sum_value = 0
prefix_sum = [0]

for i in data:
    sum_value += i
    prefix_sum.append(sum_value)

# 구간 합 계산
M = int(sys.stdin.readline())
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    print(prefix_sum[b] - prefix_sum[a - 1])
