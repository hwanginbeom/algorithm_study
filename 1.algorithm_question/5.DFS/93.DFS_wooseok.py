# 연결 요소의 개수
# https://www.acmicpc.net/problem/11724
import sys
sys.setrecursionlimit(10 ** 3) # 값을 너무 크게 잡으면 메모리초과 발생


def dfs(graph, v, visited):
    visited[v] = True

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


def solution():
    n, m = map(int, input().split())

    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    visited = [False] * (n + 1)
    count = 0

    for i in range(1, n + 1):
        if not visited[i]:
            dfs(graph, i, visited)

            count += 1

    print(count)


solution()
