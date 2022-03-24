# 아기 상어
# https://www.acmicpc.net/problem/16236
from collections import deque
import copy


# 아기 상어의 다음 자리를 찾는 함수
def find_pos(fish_list) :
    # 상어가 갈 수 있는 자리 중 가장 거리가 짧은 자리 구하기
    new_list = list(map(list, zip(*fish_list)))
    min_dist = min(new_list[2])

    new_fish_list = []
    for i in fish_list :
        if i[2] == min_dist :
            new_fish_list.append(i)

    # 가장 위에 있고 가장 왼쪽에 있는 자리 찾기
    new_list = list(map(list, zip(*new_fish_list)))
    min_row_value = min(new_list[0])

    idx_list = []
    for i in range(len(new_fish_list)) :
        if min_row_value == new_fish_list[i][0]:
            idx_list.append(i)

    fish_idx = idx_list[0]
    min_col_value = 20

    for i in idx_list:
        if min_col_value > new_fish_list[i][1]:
            min_col_value = new_fish_list[i][1]
            fish_idx = i

    return new_fish_list[fish_idx]


def bfs(graph, n, x, y, shark_size) :
    queue = deque()
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    dist = 0
    fish_list = []

    queue.append((x, y, dist))
    graph[x][y] = 500

    while queue :
        x, y, dist = queue.popleft()

        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= n :
                continue
            
            # 빈 칸인 경우
            if graph[nx][ny] == 0 :
                queue.append((nx, ny, dist + 1))
                graph[nx][ny] = 500
            # 아기 상어의 크기보다 작은 물고기가 있는 경우
            elif graph[nx][ny] < shark_size :
                fish_list.append([nx, ny, dist + 1])
                queue.append((nx, ny, dist + 1))
                graph[nx][ny] = 500
            # 아기 상어의 크기와 같은 물고기가 있는 경우
            elif graph[nx][ny] == shark_size :
                queue.append((nx, ny, dist + 1))
                graph[nx][ny] = 500

    if not fish_list :
        return { 'result': 0 }
    elif len(fish_list) == 1 :
        return { 'result': 1, 'fish': [fish_list[0][0], fish_list[0][1], fish_list[0][2]] }
    else :
        # 갈 수 있는 자리가 여러 곳인 경우 조건에 맞는 자리를 찾아 반환
        fish = find_pos(fish_list)
        return { 'result': 1, 'fish': [fish[0], fish[1], fish[2]] }


def solution() :
    n = int(input())
    shark_size = 2
    x, y = 0, 0
    sec_count = 0
    fish_num = 0

    graph = []
    for i in range(n) :
        temp = list(map(int, input().split()))
        graph.append(temp)

        if 9 in temp :
            x = i
            y = temp.index(9)

    while True :
        result = bfs(copy.deepcopy(graph), n, x, y, shark_size)

        if result['result'] == 0 :
            break
        else :
            new_x, new_y, count = result['fish']

            if graph[new_x][new_y] < shark_size :
                fish_num += 1

            if fish_num == shark_size :
                shark_size += 1
                fish_num = 0

            graph[x][y] = 0
            graph[new_x][new_y] = 9
            sec_count += count

            x, y = new_x, new_y

    print(sec_count)


solution()
