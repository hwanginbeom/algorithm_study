# 미로 탐색
# https://www.acmicpc.net/problem/2178
from collections import deque


def bfs(x, y, dx, dy, n, m, graph) :
    queue = deque()
    queue.append((x, y))

    while queue :
        x, y = queue.popleft()

        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m :
                continue

            if graph[nx][ny] == 0 :
                continue

            if graph[nx][ny] == 1 :
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))


def solution() :
    n, m = map(int, input().split())

    graph = []
    for _ in range(n) :
        maze = list(map(int, input()))
        graph.append(maze)

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    bfs(0, 0, dx, dy, n, m, graph)

    print(graph[-1][-1])


solution()
