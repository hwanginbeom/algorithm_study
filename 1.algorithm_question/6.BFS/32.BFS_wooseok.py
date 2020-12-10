# 토마토
from collections import deque


def bfs() :
    q = deque()
    day = 0

    for i in range(n) :
        for j in range(m) :
            if graph[i][j] == 1 :
                # 익은 토마토 자리를 큐에 삽입
                q.append((i, j))

    while q :
        q_length = len(q)

        for _ in range(q_length) :
            x, y = q.popleft()

            for i in range(4) :
                # 이동을 한 후의 좌표
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or nx >= n or ny < 0 or ny >= m :
                    continue

                # 이동했을 때
                # 익은 토마토거나 토마토가 없는 자리일 경우
                if graph[nx][ny] == 1 or graph[nx][ny] == -1 :
                    continue

                # 이동했을 때
                # 안익은 토마토일 경우
                if graph[nx][ny] == 0 :
                    graph[nx][ny] = 1
                    q.append((nx, ny))

        day += 1

    for li in graph :
        if 0 in li :
            return -1
    else :
        return day - 1


m, n = map(int, input().split())
graph = []

for _ in range(n) :
    graph.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

print(bfs())
