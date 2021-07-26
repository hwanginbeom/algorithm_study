# 거리두기 확인하기
# https://programmers.co.kr/learn/courses/30/lessons/81302
from collections import deque


def bfs(place, x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque()
    queue.append((x, y))

    # 큐가 빌 때까지 반복
    while queue:
        x, y = queue.popleft()

        # 현재 위치에서 4가지 방향으로의 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 대기실 공간을 벗어난 경우 무시
            if nx < 0 or nx >= 5 or ny < 0 or ny >= 5:
                continue

            # 상하좌우 중 한곳이 파티션일 경우
            if place[nx][ny] == 'X':
                continue

            # 상하좌우 중 한곳이 응시자일 경우
            if place[nx][ny] == 'P':
                return False

            # 상하좌우 중 한곳이 빈 자리일 경우
            # 빈자리에서 상하좌우로 이어진 자리가 응시자인지 검사
            if place[nx][ny] == 'O':
                for j in range(4):
                    nnx = nx + dx[j]
                    nny = ny + dy[j]

                    # 상하좌우 중 한곳이 원래 자리일 경우
                    if nnx == x and nny == y:
                        continue

                    if nnx < 0 or nnx >= 5 or nny < 0 or nny >= 5:
                        continue

                    # 빈 자리에서 바로 이어진 자리 중 응시자가 있는 경우
                    if place[nnx][nny] == 'P':
                        return False

    return True


def solution(places):
    answer = []

    for place in places:
        isFlag = True

        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    result = bfs(place, i, j)

                    if result is True:
                        continue
                    else:
                        isFlag = False
                        break

            if isFlag is False:
                answer.append(0)
                break

        if isFlag is True:
            answer.append(1)

    return answer


places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
print(solution(places))
