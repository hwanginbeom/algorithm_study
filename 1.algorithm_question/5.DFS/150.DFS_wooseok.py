# 바이러스
# https://www.acmicpc.net/problem/2606


def dfs(graph, v, visited, count) :
    visited[v] = True

    for i in graph[v] :
        if not visited[i] :
            count += 1
            count = dfs(graph, i, visited, count)

    return count


def solution() :
    n = int(input())
    m = int(input())

    graph = [[] for _ in range(n + 1)]
    for _ in range(m) :
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    visited = [False] * (n + 1)
    count = 0
    count = dfs(graph, 1, visited, count)

    print(count)


solution()
