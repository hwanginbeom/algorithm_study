## 10217번 KCM Travel

import sys
input = sys.stdin.readline
INF = int(1e9)

# 테스트 개수
T = int(input())
# 공항의 수, 총 지원비용, 티켓 정보의 수
for _ in range(T):
    n, m, k = map(int, input().split())

    graph = [[] for _ in range(n + 1)]

    # 출발공항, 도착공항, 비용, 소요시간
    for _ in range(k):
        u,v,c,d = map(int, input().split())
        # u번 노드에서 v번 노드로 가는 비용이 c, 소요시간 d
        graph[u].append([v,c,d])

    dp = [[INF for _ in range(m+1)] for _ in range(n+1)]
    dp[1][0] = 0 # 1로 갔을 때 비용 0, 시간 0

    for c in range(m+1):
        for d in range(1, n+1):
            if dp[d][c]==INF: continue
            t = dp[d][c]
            for dv, dc, dd in graph[d]:
                if dc + c > m:
                    continue
                dp[dv][dc+c]=min(dp[dv][dc+c], t+dd)

    result = min(dp[n])

    if result == INF:
        print('Poor KCM')
    else:
        print(result)



## 9370번 미확인 도착지

import sys, heapq
INF = float('inf')

T = int(input())

for _ in range(T):
    n,m,t = map(int, input().split()) # 교차로, 도로, 목적지 후보
    s,g,h = map(int, input().split()) # 출발지, 거쳐야 하는 지점 두개

graph = [[] for _ in range(n+1)]
for _ in range(m):
    # a와 b 사이에 길이 d의 양방향 도로가 있다.
    a,b,d = map(int, input().split())
    if (a == g and b == h) or (a == h and b == g):
        d -= 0.1
    graph[a].append([b,d])
    graph[b].append([a,d])

targets = []
for _ in range(t):
    targets.append(int(input()))
targets.sort()


def dijkstra(n, s, graph):
    d = [INF] * (n+1)
    d[s] = 0

    hq = []
    heapq.heappush(hq, [0,s])

    while hq:
        tmp = heapq.heappop(hq)
        cost = tmp[0]
        node = tmp[1]

        if cost > d[node]:
            continue

        for v in graph[node]:
            neighbor = v[0]
            n_cost = d[node] + v[1]

            if n_cost < d[neighbor]:
                d[neighbor] = n_cost
                heapq.heappush(hq, [n_cost, neighbor])
    return d


ans = dijkstra(n, s, graph)

for target in targets:
    if ans[target] != INF and type(ans[target]) == float:
        print(target, end=' ')
print()