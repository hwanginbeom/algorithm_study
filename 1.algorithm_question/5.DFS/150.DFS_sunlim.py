import sys

input = sys.stdin.readline


def dfs(graph, v, visited):
    global cnt
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            cnt += 1
            dfs(graph, i, visited)


PC = int(input())
network = int(input())

graph = [[] for _ in range(PC + 1)]
visited = [False] * (PC + 1)
cnt = 0  # global variable

for i in range(network):
    node1, node2 = map(int, input().split())
    graph[node1].append(node2)
    graph[node2].append(node1)

dfs(graph, 1, visited)
print(cnt)