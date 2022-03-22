from collections import deque
import sys

input = sys.stdin.readline


def bfs(x, y, weight, time, eat, n, dx, dy, graph):
    q, eat_ok = deque(), []
    q.append([x, y])
    time_graph = [[-1] * n for _ in range(n)]
    time_graph[x][y] = time
    while q:
        q_len = len(q)
        while q_len:
            x, y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < n:
                    if time_graph[nx][ny] == -1:
                        if graph[nx][ny] == 0 or graph[nx][ny] == weight:
                            time_graph[nx][ny] = time_graph[x][y] + 1
                            q.append([nx, ny])
                        elif 0 < graph[nx][ny] < weight:
                            eat_ok.append([nx, ny])
            q_len -= 1
        if eat_ok:
            nx, ny = min(eat_ok)
            eat += 1
            if eat == weight:
                eat = 0
                weight += 1
            graph[nx][ny] = 0
            return nx, ny, weight, time_graph[x][y] + 1, eat, n, dx, dy, graph
    print(time)
    sys.exit()


def solution():
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(n)]
    x, y = [(idx, value.index(9)) for idx, value in enumerate(graph) if 9 in value][0]
    dx = [-1, 0, 0, 1]
    dy = [0, -1, 1, 0]
    graph[x][y] = 0
    weight, time, eat = 2, 0, 0
    while True:
        x, y, weight, time, eat, n, dx, dy, graph = bfs(x, y, weight, time, eat, n, dx, dy, graph)

solution()