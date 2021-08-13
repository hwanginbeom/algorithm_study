# 1 1 1 2 2 3 4 5 7 9 12 16
#   0 0 1 0 1 1 1 2 2  3 4
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())

    d = [0] * 100
    d[0] = 1
    d[1] = 1
    d[2] = 1
    d[3] = 2
    d[4] = 2

    if n>5:
        for i in range(5, n):
            d[i] = d[i-1] + d[i-5]
    print(d[n-1])
