# 적록색약
# https://www.acmicpc.net/problem/10026
from collections import deque
import copy


def bfs(x, y, dx, dy, graph, n) :
    queue = deque()
    queue.append((x, y))

    color = graph[x][y]
    graph[x][y] = 'O'

    while queue :
        x, y = queue.popleft()

        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n :
                continue

            if graph[nx][ny] == color :
                queue.append((nx, ny))
                graph[nx][ny] = 'O'

    return graph


def solution() :
    n = int(input())
    graph = []

    for _ in range(n) :
        string = input()
        graph.append(list(string))

    color_blind_graph = copy.deepcopy(graph)

    for i in range(n) :
        for j in range(n) :
            if color_blind_graph[i][j] == 'G' :
                color_blind_graph[i][j] = 'R'

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    count = 0
    color_blind_count = 0

    for i in range(n) :
        for j in range(n) :
            if graph[i][j] != 'O' :
                graph = bfs(i, j, dx, dy, graph, n)
                count += 1

            if color_blind_graph[i][j] != 'O' :
                color_blind_graph = bfs(i, j, dx, dy, color_blind_graph, n)
                color_blind_count += 1

    print(count, color_blind_count)


solution()
