import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

n, m = int(input()), int(input())

graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])

start, end = map(int, input().split())


def dijkstra(start, end):
    q = []
    heapq.heappush(q, (0, start, [start]))
    distance[start] = 0
    while q:
        dist, now, path = heapq.heappop(q)
        if now == end:
            return dist, path
        if distance[now] < dist:
            continue
        for now2, cost2 in graph[now]:
            cost = dist + cost2
            if cost < distance[now2]:
                distance[now2] = cost
                heapq.heappush(q, (cost, now2, path + [now2]))
                # print(q)


minCost, path = dijkstra(start, end)
print(minCost)
print(len(path))
print(*path)
