# 플로이드
#########################
import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
INF = int(1e9)
city = [[INF for _ in range(n)] for _ in range(n)]
for _ in range(m):
    i, j, cost = map(int, input().split())
    city[i-1][j-1] = min(city[i - 1][j - 1], cost)

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            city[i][j] = min(city[i][j], city[i][k] + city[k][j])

for row in city:
    for i in range(n):
        if row[i] == INF:
            row[i] = 0
    print(*row)

# 운동
#############################
import sys

# V: 마을, E: 도로
V, E = map(int, sys.stdin.readline().split())

INF = int(1e9)
arr = [[INF for _ in range(V)] for _ in range(V)]

for _ in range(E):
    i, j, c = map(int, sys.stdin.readline().split())
    arr[i-1][j-1] = c

for k in range(V):  # 거쳐가는애
    for i in range(V):  # from
        for j in range(V):  # to
            arr[i][j] = min(arr[i][j], arr[i][k] + arr[k][j])

result = INF
#  계속 갱신한 뒤 사이클은 본인부터 본인까지에 저장됨
for i in range(V):
    result = min(result, arr[i][i])

if result == INF:
    print(-1)
else:
    print(result)