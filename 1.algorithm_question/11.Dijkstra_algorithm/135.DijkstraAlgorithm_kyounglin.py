# 2021-08-17

# 출처 : https://www.acmicpc.net/problem/11779

# 최소비용구하기2

import heapq

INF = 1e9

n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]

# 간선 정보 입력받기

for _ in range(m):
    start, end, cost = map(int, input().split())
    graph[start].append((end, cost))

s_city, e_city = map(int, input().split())

# 최단거리 테이블을 무한으로 초기화
distance = [INF] * (n + 1)
# 경로 담기
path = [[] for _ in range(n + 1)]
path[s_city].append(s_city)
q = [(0, s_city)]
heapq.heapify(q)  # 리스트를 힙으로변환

# 다익스트라

while q:
    now_cost, now = heapq.heappop(q)
    if now_cost > distance[now]:
        continue
    if now == s_city:
        distance[now] = 0
    for next, next_cost in graph[now]:
        path_cost = next_cost + now_cost
        if path_cost < distance[next]:
            distance[next] = path_cost
            heapq.heappush(q, (path_cost, next))
            path[next] = []
            for i in path[now]:
                path[next].append(i)
            path[next].append(next)

print(distance[e_city])
print(len(path[e_city]))
print(' '.join(map(str, path[e_city])))
