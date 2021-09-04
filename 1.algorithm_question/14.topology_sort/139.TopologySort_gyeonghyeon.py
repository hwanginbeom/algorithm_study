from collections import deque


def solution():
    n, m = map(int, input().split())

    indegree = [0] * (n + 1)
    answer = [0] * (n + 1)

    graph = [[] for i in range(n + 1)]

    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        indegree[b] += 1


    q = deque()

    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)
            answer[i] = 1

    while q:
        now = q.popleft()
        for i in graph[now]:
            indegree[i] -= 1
            answer[i] = answer[now] + 1
            if indegree[i] == 0:
                q.append(i)

    for i in answer[1:]:
        print(i, end=' ')


solution()
