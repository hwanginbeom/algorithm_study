import sys
sys.setrecursionlimit(10000)

def dfs(y, x):
    graph[y][x] = 0
    for dy, dx in d:
        Y, X = y+dy, x+dx
        if (0 <= Y < h) and (0 <= X < w) and graph[Y][X] == 1:
            dfs(Y, X)

while 1:
    w, h = map(int, input().split())
    if w == h == 0:
        break
    graph = [list(map(int, input().split())) for _ in range(h)]
    d = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    cnt = 0
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                dfs(i, j)
                cnt += 1
    print(cnt)