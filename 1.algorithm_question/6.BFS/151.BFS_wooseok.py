# 유기농 배추
# https://www.acmicpc.net/problem/1012
from collections import deque


def bfs(x, y, n, m, graph) :
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque()
    queue.append((x, y))

    while queue :
        x, y = queue.popleft()

        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m :
                continue

            if graph[nx][ny] == 1 :
                graph[nx][ny] = 0
                queue.append((nx, ny))

    return graph


def solution() :
    t = int(input())

    for _ in range(t) :
        m, n, k = map(int, input().split())
        graph = [[0 for _ in range(m)] for _ in range(n)]

        for _ in range(k) :
            x, y = map(int, input().split())
            graph[y][x] = 1

        count = 0
        for i in range(n) :
            for j in range(m) :
                if graph[i][j] == 1 :
                    graph = bfs(i, j, n, m, graph)
                    count += 1

        print(count)


solution()
