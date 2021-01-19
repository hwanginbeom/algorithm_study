# 2021-01-19

# 출처 : https://www.acmicpc.net/problem/18352

# 특정 거리의 도시 찾기

#어떤 나라에는 1번부터 N번까지의 도시와 M개의 단방향 도로가 존재한다. 모든 도로의 거리는 1이다.
#이 때 특정한 도시 X로부터 출발하여 도달할 수 있는 모든 도시 중에서, 최단 거리가 정확히 K인 모든 도시들의 번호를 출력하는 프로그램을 작성하시오.
# 또한 출발 도시 X에서 출발 도시 X로 가는 최단 거리는 항상 0이라고 가정한다.
# N=4, K=2, X=1일 때 다음과 같이 그래프가 구성되어 있다고 가정하자.

# 이 때 1번 도시에서 출발하여 도달할 수 있는 도시 중에서, 최단 거리가 2인 도시는 4번 도시 뿐이다.
# 2번과 3번 도시의 경우, 최단 거리가 1이기 때문에 출력하지 않는다.

import sys
from collections import deque

def Dijkstra(N, K, X, graph):
    visit = [False] * (N + 1)
    dq = deque()
    dq.append((X, 0))
    visit[X] = 0

    while dq:
        vertex, weight = dq.popleft()
        for v in graph[vertex]:
            if visit[v] is False:
                visit[v] = weight + 1
                dq.append((v, weight + 1))

    ret = []
    for i in range(len(visit)):
        if visit[i] == K:
            ret.append(i)

    if not ret:
        print(-1)
        return
    ret.sort()
    for i in ret:
        print(i)

def solution():
    N, M, K, X = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        A, B = map(int, sys.stdin.readline().split())
        graph[A].append(B)

    Dijkstra(N, K, X, graph)

solution()