import sys
input = sys.stdin.readline
from bisect import bisect_left

n = int(input())
x = list(map(int, input().split()))

x_sorted = sorted(list(set(x)))
for i in x:
    print(bisect_left(x_sorted, i), end=' ')

# 시간초과
#
# n = int(input())
# x = list(map(int, input().split()))
#
# x_sorted = sorted(list(set(x)))
# for i in x:
#     print(x_sorted.index(i), end=' ')
