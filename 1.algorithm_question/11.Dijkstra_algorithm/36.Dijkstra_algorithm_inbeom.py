import sys
from heapq import heappush, heappop
input = sys.stdin.readline
n, m, x = map(int, input().split())
inf = 100000000

# 정방향과 역방향을 구한다.
s = [[] for i in range(n + 1)]
dp = [inf] * (n + 1)
s_r = [[] for i in range(n + 1)]
dp_r = [inf] * (n + 1)
def dijkstra(start, dp, s):
    heap = []
    dp[start] = 0
    heappush(heap, [0, start])
    while heap:
        w, n = heappop(heap)
        if dp[n] < w:
            continue
        for n_n, wei in s[n]:
            n_w = wei + w
            if n_w < dp[n_n]:
                dp[n_n] = n_w
                heappush(heap, [n_w, n_n])

# 값을 받을 때 정방향과 역방향에대해 단선을 만들어준다.
for i in range(m):
    a, b, t = map(int, input().split())
    s[a].append([b, t])
    s_r[b].append([a, t])
# 2가지 경우에 대해 구해준다.
dijkstra(x, dp, s)
dijkstra(x, dp_r, s_r)
max_ = 0
# 2가지 값을 더해준다.
for i in range(1, n + 1):
    max_ = max(max_, dp[i] + dp_r[i])
print(max_)