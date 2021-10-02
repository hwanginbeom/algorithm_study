# 퍼즐 조각 채우기
# https://programmers.co.kr/learn/courses/30/lessons/84021
import copy


def dfs(graph, x, y, position, n, num):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    ret = [position]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == num:
            graph[nx][ny] = 2
            ret = ret + dfs(graph, nx, ny, [position[0] + dx[i], position[1] + dy[i]], n, num)

    return ret


def rotate(graph):
    n = len(graph)

    ret = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            ret[j][n - 1 - i] = graph[i][j]

    return ret


def solution(game_board, table):
    answer = 0
    game_board_copy = copy.deepcopy(game_board)

    n = len(game_board)
    block = []

    for i in range(n):
        for j in range(n):
            if game_board_copy[i][j] == 0:
                game_board_copy[i][j] = 2
                result = dfs(game_board_copy, i, j, [0, 0], n, 0)[1:]
                block.append(result)

    for r in range(4):
        table = rotate(table)
        table_rotate_copy = copy.deepcopy(table)

        for i in range(n):
            for j in range(n):
                if table_rotate_copy[i][j] == 1:
                    table_rotate_copy[i][j] = 2
                    result = dfs(table_rotate_copy, i, j, [0, 0], n, 1)[1:]

                    if result in block:
                        block.pop(block.index(result))
                        answer += (len(result) + 1)
                        table = copy.deepcopy(table_rotate_copy)
                    else:
                        table_rotate_copy = copy.deepcopy(table)

    return answer


game_board = [
    [1, 1, 0, 0, 1, 0],
    [0, 0, 1, 0, 1, 0],
    [0, 1, 1, 0, 0, 1],
    [1, 1, 0, 1, 1, 1],
    [1, 0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0, 0]
]
table = [
    [1, 0, 0, 1, 1, 0],
    [1, 0, 1, 0, 1, 0],
    [0, 1, 1, 0, 1, 1],
    [0, 0, 1, 0, 0, 0],
    [1, 1, 0, 1, 1, 0],
    [0, 1, 0, 0, 0, 0]
]
print(solution(game_board, table))

# 참조 https://bladejun.tistory.com/164
# 너무 어렵다
