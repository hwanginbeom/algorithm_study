# 프렌즈4블록
# https://programmers.co.kr/learn/courses/30/lessons/17679
from collections import deque


def search(dx, dy, x, y, graph):
    friend = graph[x][y]
    friend_list = [(x, y)]

    for i in range(3):
        nx = x + dx[i]
        ny = y + dy[i]

        if graph[nx][ny] == '':
            break

        if friend != graph[nx][ny]:
            break
        else:
            friend_list.append((nx, ny))
    else:
        return friend_list


def solution(m, n, board):
    answer = 0

    # 오른쪽, 아래, 오른쪽 아래 이동 변위
    dx = [0, 1, 1]
    dy = [1, 0, 1]

    graph = []

    for i in board:
        graph.append(list(i))
    # print(graph)

    while True:
        result = []

        # 터지는 블록 개수 및 인덱스 찾기
        for i in range(m - 1):
            for j in range(n - 1):
                if graph[i][i] != '':
                    temp = search(dx, dy, i, j, graph)

                if temp:
                    result.extend(temp)

        if not result:
            break

        result = list(set(result))
        answer += len(result)

        # 터진 블록자리를 공백으로 변환
        for idx in result:
            graph[idx[0]][idx[1]] = ''

        # 블록 떨어지는 로직
        queue = deque([])
        for i in range(n):
            for j in range(m - 1, -1, -1):
                if graph[j][i] == '':
                    queue.append((j, i))
                else:
                    if queue:
                        temp_idx = queue.popleft()
                        graph[temp_idx[0]][temp_idx[1]] = graph[j][i]
                        graph[j][i] = ''

                        queue.append((j, i))

            queue.clear()

    return answer


m = 4
n = 5
board = ["CCBDE", "AAADE", "AAABF", "CCBBF"]
print(solution(m, n, board))
