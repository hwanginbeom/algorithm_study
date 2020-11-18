#1753
import sys
import heapq

input = sys.stdin.readline
INF = sys.maxsize
V, E = map(int, input().split())
K = int(input())
dp = [INF]*(V+1)
heap = []
graph = [[] for _ in range(V + 1)]

def Dijkstra(start):
    dp[start] = 0
    heapq.heappush(heap,(0, start))

    while heap:
        wei, now = heapq.heappop(heap)

        if dp[now] < wei:
            continue

        for w, next_node in graph[now]:
            next_wei = w + wei
            if next_wei < dp[next_node]:
                dp[next_node] = next_wei
                heapq.heappush(heap,(next_wei,next_node))

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))


Dijkstra(K)
for i in range(1,V+1):
    print("INF" if dp[i] == INF else dp[i])


# 1504
from heapq import heappop, heappush
import sys


def dijkstra(arr, start):
    dist = arr[:]
    dist[start] = 0
    heappush(node, [0, start])
    while len(node) != 0:
        item = heappop(node)
        for value in info[item[1]]:
            if dist[value[1]] > value[0] + dist[item[1]]:
                dist[value[1]] = value[0] + dist[item[1]]
                heappush(node, [dist[value[1]], value[1]])
    return dist


input = sys.stdin.readline
V, E = map(int, input().split())
MAX = 99999999
node = []
info = [[] for i in range(V+1)]
dist = [MAX] * (V+1)
for i in range(E):
    u, v, w = map(int, input().split())
    info[u].append([w, v])
    info[v].append([w, u])
p, q = map(int, input().split())
c1 = dijkstra(dist, 1)
c2 = dijkstra(dist, p)
c3 = dijkstra(dist, q)
ans = min((c1[p]+c2[q]+c3[V]), (c1[q]+c3[p]+c2[V]))
print(-1 if ans >= MAX or
      ans < 0 else ans)
