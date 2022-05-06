import heapq
import sys

input = sys.stdin.readline


def dijkstra(graph, distance, start, end):
    q = []
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)
        dist *= -1
        if now == end:
            return dist
        if distance[now] > dist:
            continue
        for i in graph[now]:
            if dist == 0:
                distance[i[1]] = i[0]
                heapq.heappush(q, (-distance[i[1]], i[1]))
            elif distance[i[1]] < i[0] and distance[i[1]] < dist:
                distance[i[1]] = min(dist, i[0])
                heapq.heappush(q, (-distance[i[1]], i[1]))


def solution():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a].append((c, b))
        graph[b].append((c, a))
    for i in range(1, n + 1):
        graph[i].sort(reverse=True)
    distance = [0] * (n + 1)
    start, end = map(int, input().split())
    return dijkstra(graph, distance, start, end)


print(solution())
