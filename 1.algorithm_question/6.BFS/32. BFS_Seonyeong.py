## 7576번: 토마토

from collections import deque

def bfs():
    q = deque()
    day = 0

    for i in range(n):
        for j in range(m):
            if tomatoes[i][j] == 1:
                q.append((i,j))

    while q:
        for _ in range(len(q)):
            x, y = q.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or nx > n or ny <0 or ny > m:
                    continue
                if tomatoes[nx][ny] == 1 or tomatoes[nx][ny] == -1:
                    continue
                if tomatoes[nx][ny] == 0:
                    tomatoes[nx][ny] = 1
                    q.append((nx, ny))
        day += 1

        for li in tomatoes:
            if 0 in li:
                return -1
        else:
            return day-1



m, n = map(int, input())

tomatoes = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

print(bfs())



