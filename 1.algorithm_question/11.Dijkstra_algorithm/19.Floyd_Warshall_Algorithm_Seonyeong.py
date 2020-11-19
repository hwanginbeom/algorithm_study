# 11404번 플로이드

# 도시의 개수
n = int(input())
# 버스의 개수
m = int(input())
# 노선 정리 그래프
INF = int(1e9)
graph = [[INF] * (n+1) for _ in range(n+1)]


for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a][b] = min(c, graph[a][b])

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            if a==b:
                graph[a][b] = 0
            else:
                graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

for a in range(1,n+1):
    for b in range(1,n+1):
        if graph[a][b] == INF:
            print(0, end=' ')
        else:
            print(graph[a][b], end=' ')
    print()



# 1956번 운동

# 마을, 도로의 개수
v,e = map(int,input().split())
# 노선 정리 그래프
INF = int(1e9)
graph = [[INF] * (v+1) for _ in range(v+1)]

# 자기 자신에게 가는 방법은 0
for t in range(1, v+1):
    for j in range(1, v+1):
        if t == j:
            graph[t][j] = 0

for _ in range(e):
    a,b,c = map(int, input().split())
    graph[a][b] = c

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            if a == b:
                graph[a][b] = 0
            else:
                graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

shortest = INF
for a in range(1,n+1):
    for b in range(1,n+1):
        if ( graph[a][b] + graph[b][a]) <= shortest:
            if graph[a][b] != 0 and graph[a][b] != 0:
                shortest = (graph[a][b] + graph[b][a])

if shortest < INF:
    print(shortest)
else:
    print(-1)