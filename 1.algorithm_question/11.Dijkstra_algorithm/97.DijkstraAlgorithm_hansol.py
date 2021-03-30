# Dajikstra Algorithm
# 파티
# https://www.acmicpc.net/problem/1238

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m, x = map(int, input().split())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
graph = [[] for i in range(n + 1)]
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n + 1)

# 모든 간선 정보를 입력받기
for _ in range(m):
    a, b, c = map(int, input().split())
    # a번 노드에서 b번 노드로 가는 비용이 c라는 의미
    graph[a].append((b, c))

def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 거리는 0으로 설정하여, 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q: # 큐가 비어있지 않다면
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

# x에서 각 노드까지의 최단거리 저장하기 위해 다익스트라 알고리즘 수행
dijkstra(x)
# x에서 각 노드까지의 최단거리 저장
x_distance = distance.copy()

cost_sum = 0
# X로 갔다가 X에서 자기 자신으로 돌아오는 모든 비용을 확인
for i in range(1, n + 1) :
    # 자기 자신일 경우 무시
    if i == x :
        continue
    # x에서 다른 노드까지의 거리를 계산하기 위해 활용한 distance 초기화
    distance = [INF] * (n + 1)
    # 다익스트라 알고리즘 수행
    dijkstra(i)
    # i에서 x로 비용 + x에서 i로 비용 값 중 최댓값을 찾기
    cost_sum = max(cost_sum, (distance[x] + x_distance[i]))

print(cost_sum)