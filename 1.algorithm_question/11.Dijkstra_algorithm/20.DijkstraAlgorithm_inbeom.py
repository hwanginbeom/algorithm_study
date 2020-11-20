# 9370 번
from heapq import heappush, heappop
import sys
input = sys.stdin.readline

def dijkstra(start):
    heap = []
    heappush(heap,[0,start])
    dp = [100000000 for i in range(n+1)]
    dp[start] = 0
    while heap:
        we,nu = heappop(heap)
        for ne,nw in s[nu]:
            wei = we +nw
            if dp[ne] > wei:
                dp[ne] = wei
                heappush(heap, [wei, ne])
    return dp

t = int(input())

for _ in range(t):
    # n = 교차로 / m = 도로 / c= 목적지
    n, m, c = map(int, input().split())

    # start = 출발지 / g  - h = 교차로 사이 도로를 나타낸다.
    start, g, h = map(int, input().split())

    # s에 교차로 개수 만큼의 공간을 만든다
    s = [[] for i in range(n+1)]
    de = []
    # a와 b사이의 d라는 거리가 있다.
    for j in range(m):
        a, b, d = map(int, input().split())
        # s라는 교차로에 a와 b라는 도로가 있고 그 거리를 나타낸다.
        s[a].append([b, d])
        # s라는 교차로에 a와 b라는 도로가 있고 그 거리를 나타낸다.
        s[b].append([a, d])
    # 목적지를 넣는다.
    for k in range(c):
        de.append(int(input()))
    # start 에 대한 다익스트라 알고리즘을 돌리고
    start_ = dijkstra(start)
    # g 에 대한 다익스트라 알고리즘을 돌리고
    g_ = dijkstra(g)
    # h 에 대한 다익스트라 알고리즘을 돌리고
    h_ = dijkstra(h)
    an = []
    # start에서 출발하는데 g로 출발하고 h를 들려 목적지로 가는것
    for l in de: # ㅣ는 목적지
        if start_[g] + g_[h] + h_[l] == start_[l] or start_[h] + h_[g] + g_[l] == start_[l]:
            an.append(l)
    an.sort()
    for f in an:
        print(f, end=' ')
    print()

# 10217번
input = __import__('sys').stdin.readline
Max = float('INF')
# 테스트 케이스
for __ in range(int(input())):
    # n - 공항의 수 / m - 총 지원비용 / k 티켓정보
    n, m, k=map(int, input().split())
    D = [[] for _ in range(n+1)]
    for i in range(k):
        #u=티켓의 출발공항 , v- 도착공항, c-비용,d-소요시간
        u, v, c, d=map(int, input().split())
        # 출발공항에서 도착공항/비용/소요시간
        D[u].append((v, c, d))
    S=[[Max]*(m+1) for _ in range(n+1)]
    S[1][0] = 0
    for e in range(m+1):
        for x in range(1, n+1):
            if S[x][e] == Max: continue
            t = S[x][e]
            for nx, ne, nt in D[x]:
                if ne+e > m: continue
                S[nx][ne+e] = min(S[nx][ne+e], t+nt)
    k = min(S[n])
    print([k, 'Poor KCM'][k == Max])