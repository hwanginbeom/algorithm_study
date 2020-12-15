## 1149번: RGB거리

n = int(input())
cost = []

for _ in range(n):
    cost.append(list(map(input().split())))

graph = [[0] * 3 for _ in range(n)]

for i in range(n):
    if i == 0:
        graph[i][0] = cost[0][0]
        graph[i][1] = cost[0][1]
        graph[i][2] = cost[0][2]

    # 빨간색 선택
    graph[i][0] = cost[i][0] + min(graph[i-1][1], graph[i-1][2])
    # 초록색 선택
    graph[i][1] = cost[i][1] + min(graph[i-1][0], graph[i-1][2])
    # 파란색 선택
    graph[i][2] = cost[i][2] + min(graph[i-1][0], graph[i-1][1])

min_cost = min(graph[n-1][0], graph[n-1][1], graph[n-1][2])

print(min_cost)
