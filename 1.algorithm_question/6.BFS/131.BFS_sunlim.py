from collections import deque
import sys
input = sys.stdin.readline
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(i, j):
    q = deque()
    q.append([i, j])
    max_n = 0
    while q:
        a, b = q.popleft()
        for k in range(4):
            x = a + dx[k]
            y = b + dy[k]
            if 0 <= x < n and 0 <= y < m and visit[x][y] == 0 and s[x][y] != "W":
                visit[x][y] = 1
                s[x][y] = s[a][b] + 1
                max_n = max(max_n, s[x][y])
                q.append([x, y])
    return max_n
n, m = map(int, input().split())
s = []
result = 0
for i in range(n):
    s.append(list(input().strip()))
for i in range(n):
    for j in range(m):
        if s[i][j] != "W":
            visit = [[0] * m for _ in range(n)]
            s[i][j] = 0
            visit[i][j] = 1
            result = max(result, bfs(i, j))
print(result)