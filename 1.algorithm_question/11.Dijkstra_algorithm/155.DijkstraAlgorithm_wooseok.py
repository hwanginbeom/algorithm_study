# 파티
# https://www.acmicpc.net/problem/1238
import heapq


def dijkstra(start, distance, graph) :
    q = []

    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q :
        dist, now = heapq.heappop(q)

        if distance[now] < dist :
            continue

        for i in graph[now] :
            cost = dist + i[1]

            if cost < distance[i[0]] :
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

    return distance


def solution() :
    n, m, x = map(int, input().split())
    graph = [[] for _ in range(n + 1)]

    for _ in range(m) :
        a, b, t = map(int, input().split())
        graph[a].append((b, t))

    INF = int(1e9)
    check = []
    for i in range(1, n + 1) :
        if i != x :
            distance = [INF] * (n + 1)
            out_distance = dijkstra(i, distance, graph)
            out_time = out_distance[x]

            distance = [INF] * (n + 1)
            in_distance = dijkstra(x, distance, graph)
            in_time = in_distance[i]

            check.append(out_time + in_time)

    print(max(check))


solution()
