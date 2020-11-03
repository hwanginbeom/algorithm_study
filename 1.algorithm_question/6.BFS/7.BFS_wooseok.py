from collections import deque


# BFS 메소드 정의
def bfs(x, y):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque()
    queue.append((x, y))

    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 원소를 뽑아 출력하기
        x, y = queue.popleft()

        # 현재 위치에서 4가지 방향으로의 위치 확인
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]

            # 미로 찾기 공간을 벗어난 경우 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m :
                continue

            # 벽인 경우 무시
            if maze[nx][ny] == 0 :
                continue

            # 해당 노드를 처음 방문하는 경우에만 최단거리 기록
            if maze[nx][ny] == 1 :
                maze[nx][ny] = maze[x][y] + 1
                queue.append((nx, ny))

    return maze[n - 1][m - 1]


# 미로의 가로, 세로 길이 입력
n, m = map(int, input().split())

# 미로 생성
maze = []
for i in range(n) :
    row = input()
    flag = []

    for j in range(m) :
        flag.append(int(row[j]))

    maze.append(flag)

# 이동할 4가지 방향 정의 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 정의된 BFS 함수 호출
print(bfs(0, 0))
