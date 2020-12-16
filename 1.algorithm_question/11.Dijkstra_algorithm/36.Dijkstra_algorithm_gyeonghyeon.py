import heapq
INF = int(1e9)

def dijkstra(x):
    distance = [INF]*(n+1)
    heapq.heappush(heap, [0, x])
    distance[x] = 0
    while heap:
        w, x = heapq.heappop(heap)
        for nw, nx in graph[x]:
            nw += w
            if nw < distance[nx]:
                distance[nx] = nw
                heapq.heappush(heap, [nw, nx])
    return distance

n, m, t = map(int, input().split())
graph = [[]*n for _ in range(n + 1)]
heap = []

for i in range(m):
    x, y, w = map(int, input().split())
    graph[x].append([w, y])

ans = [0]*(n+1)
for i in range(1,n+1):
    distance = dijkstra(i)
    ans[i] += distance[t]
    distance = dijkstra(t)
    ans[i] += distance[i]
print(max(ans))