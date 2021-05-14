from collections import deque

def bfs(color, x, y):
    q = deque()
    q.append([x,y])

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if -1 < nx < n and -1 < ny < n and graph[nx][ny] in color and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny))


n = int(input())
graph = [list(map(str, input())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


visited = [[False] * n for _ in range(n)]
nblind = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            visited[i][j] = True
            bfs(list(graph[i][j]), i, j)
            nblind += 1


visited = [[False] * n for _ in range(n)]
blind = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            visited[i][j] = True
            if graph[i][j] == 'R' or graph[i][j] == 'G':
                bfs(['R', 'G'], i, j)
            else:
                bfs(['B'], i, j)
            blind += 1

print(nblind, blind)
