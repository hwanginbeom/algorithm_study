import sys
input=sys.stdin.readline
from collections import deque

t = int(input()) # t:테스트케이스

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(graph, x, y):
    queue = deque()
    queue.append((x,y))
    graph[x][y] = 0

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx,ny))
    return graph


for _ in range(t):
    m, n, k = map(int, input().split())  # m:가로길이, n:세로길이, k:배추심어진위치개수
    cnt = 0

    graph = [[0] * m for _ in range(n)]
    for i in range(k):
        x, y = map(int, input().split())  # x,y:배추위치
        graph[y][x] = 1

    for a in range(n):
        for b in range(m):
            if graph[a][b] == 1:
                bfs(graph, a, b)
                cnt += 1
    print(cnt)
