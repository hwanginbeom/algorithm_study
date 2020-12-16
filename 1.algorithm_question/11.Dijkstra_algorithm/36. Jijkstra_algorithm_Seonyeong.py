## 1238번: 파티

import heapq
import sys
input = sys.stdin.readline()
INF = int(1e9)

def dijkstra(n,x,graph):
    q = []
    dist = [INF] * n
    dist[x] = 0
    heapq.heappush(q, [0,x])

    while q:
        cost, pos = heapq.heappop(q)
        for p, c in graph[pos]:
            c += cost
            if c < dist[p]:
                dist[p] = c
                heapq.heappush(q, [c, p])
    return dist


# 학생의 수, 도로의 수, 파티를 열 마을 번호
n, m, x = map(int, input().split())

graph = [[] for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a-1].append([b-1,c])

answer = [0] * n
for i in range(n):
    ret = dijkstra(n,i,graph)
    if i == x-1:
        for idx, r in enumerate(ret):
            answer[idx] += r
    else:
        answer[i] += ret[x-1]
print(max(answer))





