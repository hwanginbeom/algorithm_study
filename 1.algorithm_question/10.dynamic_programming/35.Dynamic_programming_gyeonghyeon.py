def min(a, b):
    return a if a <= b else b

n = int(input())
house = [list(map(int, input().split())) for _ in range(n)]
matrix2 = [[0] * 3 for i in range(n)]

for i in range(n):
    if i == 0:
        matrix2[i] = house[i]
    else:
        matrix2[i][0] = house[i][0] + min(matrix2[i - 1][1], matrix2[i - 1][2])
        matrix2[i][1] = house[i][1] + min(matrix2[i - 1][0], matrix2[i - 1][2])
        matrix2[i][2] = house[i][2] + min(matrix2[i - 1][0], matrix2[i - 1][1])

print(min(min(matrix2[n - 1][0], matrix2[n - 1][1]), matrix2[n - 1][2]))


