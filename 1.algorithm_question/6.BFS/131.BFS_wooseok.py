# 보물섬
# https://www.acmicpc.net/problem/2589
from collections import deque
import copy


def bfs(treasure_map, x, y, n, m) :
    copy_map = copy.deepcopy(treasure_map)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # 시작 지점과 탐색해나가는 지점과의 거리 저장 변수
    count = 0

    queue = deque([[x, y, count]])
    copy_map[x][y] = 'W' # 시작 지점은 거쳐갔다는 표시

    while queue :
        x, y, cnt = queue.popleft()
        count = cnt # 다음 지점의 좌표를 꺼낼 때마다 거리를 갱신한다.

        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m :
                continue

            if copy_map[nx][ny] == 'L' :
                copy_map[nx][ny] = 'W'
                queue.append([nx, ny, cnt + 1])

    return count


def solution() :
    n, m = map(int, input().split())
    treasure_map = []
    count_list = []

    for _ in range(n) :
        temp = list(input())
        treasure_map.append(temp)

    # 완전 탐색
    for i in range(n) :
        for j in range(m) :
            if treasure_map[i][j] == 'L' :
                count_list.append(bfs(treasure_map, i, j, n, m))

    print(max(count_list))


solution()
