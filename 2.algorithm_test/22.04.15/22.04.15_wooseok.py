# 거리두기 확인하기
# https://programmers.co.kr/learn/courses/30/lessons/81302


def check_rule(graph, x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= 5 or ny < 0 or ny >= 5:
            continue

        if graph[nx][ny] == 'P':
            return False

        if graph[nx][ny] == 'O':
            for j in range(4):
                nnx = nx + dx[j]
                nny = ny + dy[j]

                if nnx == x and nny == y:
                    continue

                if nnx < 0 or nnx >= 5 or nny < 0 or nny >= 5:
                    continue

                if graph[nnx][nny] == 'P':
                    return False

    return True


def solution(places):
    answer = []

    for place in places:
        place_list = []
        isFlag = True

        for i in place:
            place_list.append(list(i))
        # print(place_list)

        for i in range(5):
            for j in range(5):
                if place_list[i][j] == 'P':
                    if not check_rule(place_list, i, j):
                        isFlag = False
                        break
            if not isFlag:
                break

        if isFlag:
            answer.append(1)
        else:
            answer.append(0)

    return answer


places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
print(solution(places))
