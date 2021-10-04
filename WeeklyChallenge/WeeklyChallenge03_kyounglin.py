# 2021-10-04

# 출처 : https://programmers.co.kr/learn/courses/30/lessons/84021

# 위클리 챌린지 - 3주차_퍼즐 조각 채우기

# 문제를 이해 못해서 - 블로그에서 가져옴

# 블로그 답 출처 : https://ssooyn.tistory.com/29


from collections import defaultdict
from collections import deque


def bfs(start, end, table, visited, target):
    n = len(table)
    stack = deque([(start, end)])
    route = set([(0, 0)])

    while stack:
        x, y = stack.popleft()
        for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n:
                if table[nx][ny] == target and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    stack.append((nx, ny))
                    route.add((nx - start, ny - end))  # 시작점 (0, 0)으로 이동
    return route


def rotate_block(block_info, n):
    new_info = set()
    for x, y in block_info:
        new_info.add((y, n - x - 1))  # rotate

    return new_info


def find_block(block_info, set_of_blocks, n):
    for _ in range(4):
        dx, dy = min(block_info)
        new_info = set()
        for x, y in block_info:
            new_info.add((x - dx, y - dy))  # 시작점 (0, 0)으로 이동
        if new_info in set_of_blocks:
            set_of_blocks.remove(new_info)  # 사용된 블럭지우기
            return len(new_info)

        block_info = rotate_block(block_info, n)

    return 0


def solution(game_board, table):
    answer = 0
    num_of_blocks = defaultdict(list)
    n = len(table)

    # 블럭의 개수별로 블럭의 위치 저장
    visited = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if table[i][j] == 1 and visited[i][j] == 0:
                visited[i][j] = 1
                block_info = bfs(i, j, table, visited, 1)
                num_of_blocks[len(block_info)].append(block_info)

    # 빈공간찾기
    visited = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if game_board[i][j] == 0 and visited[i][j] == 0:
                visited[i][j] = 1
                empty_block = bfs(i, j, game_board, visited, 0)
                # print(empty_block)
                if len(empty_block) in num_of_blocks:
                    answer += find_block(empty_block, num_of_blocks[len(empty_block)], n)

    return answer