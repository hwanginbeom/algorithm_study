import sys
input=sys.stdin.readline

n = int(input())  # n:컴퓨터수
m = int(input())  # m:컴퓨터쌍의수

graph = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split()) # a,b:연결되어있는컴퓨터쌍
    graph[a].append(b)
    graph[b].append(a)


def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

visited = [False] * (n+1)
dfs(graph, 1, visited)
print(sum(visited)-1)
