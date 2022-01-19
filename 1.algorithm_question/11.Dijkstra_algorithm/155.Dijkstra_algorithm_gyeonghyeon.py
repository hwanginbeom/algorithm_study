import heapq
import sys
input = sys.stdin.readline

INF = int(1e9)

def solution():
    n, m, start = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
    answer = [0] * (n + 1)
    for i in range(1, n + 1):
        distance_temp = dijkstra(n, i, graph)
        answer[i] += distance_temp[start]
        distance_temp = dijkstra(n, start, graph)
        answer[i] += distance_temp[i]
    print(max(answer))


def dijkstra(n, start, graph):
    distance = [INF] * (n + 1)
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    return distance

solution()