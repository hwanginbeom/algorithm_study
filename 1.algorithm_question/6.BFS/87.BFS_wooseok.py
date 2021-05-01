# 트리의 부모 찾기
# https://www.acmicpc.net/problem/11725
from collections import deque


def bfs(graph, visited, start, n) :
    answer = [0] * (n + 1)

    q = deque([start])
    visited[start] = True

    while q :
        v = q.popleft()

        for i in graph[v] :
            if not visited[i] :
                q.append(i)
                visited[i] = True

                answer[i] = v

    return answer


def solution() :
    n = int(input())
    graph = [[] for _ in range(n + 1)]

    for _ in range(n - 1) :
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    # print(graph)
    visited = [False] * (n + 1)
    answer = bfs(graph, visited, 1, n)

    for i in range(2, len(answer)) :
        print(answer[i])


solution()
