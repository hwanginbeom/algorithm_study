import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)
def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
cnt = 0
visited = [False] * (n+1)

for i in range(1, n+1):
    if visited[i] == False:
        dfs(graph, i, visited)
        cnt += 1

print(cnt)

