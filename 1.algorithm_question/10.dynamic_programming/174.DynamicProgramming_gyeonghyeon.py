import sys

input = sys.stdin.readline


def solution():
    n = int(input())
    triangle = [list(map(int, input().split())) for _ in range(n)]
    for i in range(1, n):
        for j in range(len(triangle[i])):
            if j == 0:
                triangle[i][j] += triangle[i-1][j]
            elif j == i:
                triangle[i][j] += triangle[i-1][j-1]
            else:
                triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])
    return max(triangle[-1])


print(solution())
