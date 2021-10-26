from collections import deque


def bfs(graph, start_x, start_y, end_x, end_y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    graph[start_x][start_y] = 0
    queue = deque()
    queue.append((start_x, start_y, 0))
    length_list = []

    while queue:
        x, y, length = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 다음 지점이 도착 지점과 같다면
            # 해당 지점까지의 길이를 저장
            if nx == end_x and ny == end_y :
                length_list.append(length)
                continue

            if nx < 0 or nx >= len(graph) or ny < 0 or ny >= len(graph):
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                length += 1
                queue.append((nx, ny, length))

    return length_list


def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    graph = [[0] * 101 for _ in range(101)]

    # 도형의 테두리는 1로, 나머지는 0으로 표현
    # 직사각형 좌표들을 두배 늘려서 찍는 이유 : 실제로는 길이 이어져있지 않지만
    # 바로 인접한 지점은 1이기 때문에 연결되어 있는 것으로 판단
    # 직사각형 전체는 1로 표현 후, 테두리를 제외한 직사각형의 내부들은 0으로 다시 표현
    for r in rectangle:
        for i in range(r[0] * 2, r[2] * 2 + 1):
            for j in range(r[1] * 2, r[3] * 2 + 1):
                graph[i][j] = 1

    for r in rectangle:
        for i in range(r[0] * 2 + 1, r[2] * 2):
            for j in range(r[1] * 2 + 1, r[3] * 2):
                graph[i][j] = 0

    start_x, start_y = characterX * 2, characterY * 2
    item_x, item_y = itemX * 2, itemY * 2

    # BFS로 아이템이 있는 지점까지의 두 갈래 길의 길이 계산
    length_list = bfs(graph, start_x, start_y, item_x, item_y)
    a, b = length_list[0] / 2, length_list[1] / 2

    answer = min(a, b)
    if int(answer) != answer :
        answer = int(answer) + 1
    else :
        answer = int(answer)

    return answer


rectangle = [[1, 1, 8, 4], [2, 2, 4, 9], [3, 6, 9, 8], [6, 3, 7, 7]]
characterX = 9
characterY = 7
itemX = 6
itemY = 1
print(solution(rectangle, characterX, characterY, itemX, itemY))
