N = int(input())
M = int(input())
graph = [[0] * (N+1) for _ in range(N+1)]
p = [0] * (N+1)
for i in range(M):
    X, Y, K = map(int, input().split())
    graph[X][Y] = K
    p[Y] += 1
base = []
for i in range(1, N+1):
    if graph[i].count(0) == N + 1:
        base.append(i)
queuelist = [N]
visited = [0] * (N+1)
dp = [0] * (N+1)
dp[N] = 1
while queuelist:
    for i in range(len(queuelist)):
        now = queuelist.pop(0)
        for j in range(N+1):
            if graph[now][j]:
                visited[j] += 1
                dp[j] += dp[now] * graph[now][j]
                if visited[j] == p[j]:
                    queuelist.append(j)
for i in base:
    if dp[i]:
        print(i, dp[i])
