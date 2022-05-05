from collections import deque

move_x = [1, 0, -1, 0]
move_y = [0, -1, 0, 1]


def bfs(place, x, y):
    visited = [[0] * 5 for _ in range(5)]
    q = deque()
    q.append([x, y, 0])
    visited[x][y] = 1

    while q:
        now_0, now_1, now_2 = q.popleft()
        if 1 <= now_2 <= 2 and place[now_0][now_1] == 'P':
            return False
        if 3 <= now_2:
            break
        for m in range(4):
            nxt = [0, 0, 0]
            nxt[0] = now_0 + move_x[m]
            nxt[1] = now_1 + move_y[m]
            nxt[2] = now_2 + 1

            if 0 <= nxt[0] < 5 and 0 <= nxt[1] < 5:
                if place[nxt[0]][nxt[1]] != 'X' and visited[nxt[0]][nxt[1]] == 0:
                    q.append(nxt)
                    visited[nxt[0]][nxt[1]] = 1
    return True


def solution(places):
    answer = []

    for place in places:
        false_place = True
        for x in range(len(place)):
            for y in range(len(place[0])):
                if place[x][y] == 'P':
                    if not bfs(place, x, y):
                        false_place = False
                        break
            if not false_place:
                break
        if false_place:
            answer.append(1)
        else:
            answer.append(0)
    return answer


places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
solution(places)