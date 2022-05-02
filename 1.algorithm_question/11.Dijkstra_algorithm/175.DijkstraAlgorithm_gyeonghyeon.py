import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)


def dijkstra(start, distance, graph):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, node = heapq.heappop(q)
        if distance[node] < dist:
            continue
        for i in graph[node]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

    cnt, sec = 0, 0
    for i in distance:
        if i != INF:
            cnt += 1
            sec = max(sec, i)
    print(cnt, sec)


def solution():
    t = int(input())
    while t:
        n, d, c = map(int, input().split())
        graph = [[] for _ in range(n + 1)]
        distance = [INF] * (n + 1)
        for _ in range(d):
            a, b, s = map(int, input().split())
            graph[b].append((a, s))
        dijkstra(c, distance, graph)
        t -= 1


solution()
