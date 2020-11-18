################################
# 최단경로
# 1753

import sys
import heapq
input = sys.stdin.readline
INF = 7777777777

def dijkstra(v, start, g):
    dist = [INF] * (V + 1)
    dist[start] = 0
    q = []
    heapq.heappush(q, [0, start])
    while q:
        cost, loc = heapq.heappop(q)
        for l, c in g[loc]:
            c += cost
            if c < dist[l]:
                dist[l] = c
                heapq.heappush(q, [c, l])
    return dist[1:]


V, E = map(int, input().split())
K = int(input())
G = [[] for i in range(V + 1)]
for i in range(E):
    u, v, w = map(int, input().split())
    G[u].append([v, w])

for x in dijkstra(V, K, G):
    print(x if x != INF else "INF")

################################
# 특정한 최단 경로
# 1504

import sys, heapq
input = sys.stdin.readline


def BFS(hq):
    while hq:
        weight, vec = heapq.heappop(hq)

        if di[vec] > weight:
            di[vec] = weight

            for w, v in adjList[vec]:
                heapq.heappush(hq, (w + weight, v))


N, E = map(int, input().split())

ans = [0, 0]

INF = 7777777777
adjList = [[] for _ in range(N + 1)]

for _ in range(E):
    a, b, c = map(int, input().split())

    adjList[a].append((c, b))
    adjList[b].append((c, a))

stop = list(map(int, input().split()))
iter = [[1, stop[0], stop[1], N], [1, stop[1], stop[0], N]]

for i in range(2):
    for j in range(3):
        di = [INF] * (N + 1)
        di[iter[i][j]] = 0
        hq = []
        for w, v in adjList[iter[i][j]]:
            heapq.heappush(hq, (w, v))
        BFS(hq)
        ans[i] += di[iter[i][j + 1]]

print(min(ans) if min(ans) < INF else -1)