from collections import deque as dq

move_x = [1,0,-1,0]
move_y = [0,-1,0,1]


def bfs(place, x, y):
    visited = [[0 for y in range(5)] for x in range(5)]
    q = dq()
    q.append([x, y, 0])
    visited[x][y] = 1

    while q:
        now = q.popleft()
        if 2 >= now[2] >= 1 and place[now[0]][now[1]] == "P":
            return False
        if now[2] >= 3:
            break

        for m in range(4):
            nxt = [0, 0, 0]
            nxt[0] = now[0] + move_x[m]
            nxt[1] = now[1] + move_y[m]
            nxt[2] = now[2] + 1
            if 0 <= nxt[0] < 5 and 0 <= nxt[1] < 5:
                if place[nxt[0]][nxt[1]] != "X" and visited[nxt[0]][nxt[1]] == 0:
                    q.append(nxt)
                    visited[nxt[0]][nxt[1]] = 1

    return True


def solution(places):
    answer = []

    for place in places:
        false_place = True
        for x in range(len(place)):
            for y in range(len(place[0])):
                if place[x][y] == "P":
                    if bfs(place, x, y) == False:
                        false_place = False
                        break
            if false_place == False:
                break
        if false_place == False:
            answer.append(0)
        else:
            answer.append(1)

    return answer


n = 5
places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
          ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
          ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
solution(places)
