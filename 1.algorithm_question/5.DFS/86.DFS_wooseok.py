# 촌수계산
# https://www.acmicpc.net/problem/2644


def dfs(graph, v, visited, count) :
    visited[v] = count

    # 재귀를 들어갈 때마다 촌수를 1 더하기 위한 변수
    count += 1

    for i in graph[v] :
        if visited[i] is False :
            dfs(graph, i, visited, count)

    # 재귀에서 빠져나오면 1 빼줘야 한다.
    count -= 1


def solution() :
    n = int(input())
    a, b = map(int, input().split())
    m = int(input())

    graph = [[] for _ in range(n + 1)]
    for _ in range(m) :
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)

    visited = [False] * (n + 1)
    count = 0

    dfs(graph, a, visited, count)

    if visited[b] is False :
        print(-1)
    else :
        print(visited[b])


solution()
