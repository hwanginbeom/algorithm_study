# 안전 영역
# https://www.acmicpc.net/problem/2468
import copy
from collections import deque


def bfs(area, n, x, y) :
    queue = deque()
    queue.append((x, y))
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    while queue :
        x, y = queue.popleft()

        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= n :
                continue

            if area[nx][ny] == 0 :
                continue
            else :
                area[nx][ny] = 0
                queue.append((nx, ny))

    return area


def solution() :
    n = int(input())
    area = []
    max_height = 1

    for _ in range(n) :
        temp = list(map(int, input().split()))

        # 주어진 2차원 배열의 최대값 구하기
        max_value = max(temp)
        max_height = max(max_height, max_value)

        area.append(temp)

    count_list = []

    # 물에 잠기는 높이를 0 부터 (최대값 -1) 까지 각각의 안전영역 구하기
    for i in range(max_height) :
        count = 0
        area_copy = copy.deepcopy(area)

        for a in range(n) :
            for b in range(n) :
                if area_copy[a][b] <= i :
                    area_copy[a][b] = 0

        for a in range(n) :
            for b in range(n) :
                if area_copy[a][b] != 0 :
                    area_copy = bfs(area_copy, n, a, b)
                    count += 1

        count_list.append(count)

    print(max(count_list))


solution()
