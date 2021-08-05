from collections import deque


def bfs(x, y):
    distance = 0
    q = deque()
    q.append((x, y, 0))
    visit[x][y] = 1

    while q:
        x, y, d = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if nx < 0 or ny < 0 or nx >= a or ny >= b:
                continue
            if graph[nx][ny] == 'L' and visit[nx][ny] == 0:
                q.append((nx, ny, d + 1))
                visit[nx][ny] = 1
                distance = d + 1

    return distance


dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
a, b = map(int, input().split())
graph = [input() for _ in range(a)]
max_dis = 0

for i in range(a):
    for j in range(b):
        if graph[i][j] == 'L':
            visit = [[0] * b for _ in range(a)]
            max_dis = max(max_dis, bfs(i, j))

print(max_dis)