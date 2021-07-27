# 2021-07-27

# 출처 : https://programmers.co.kr/learn/courses/30/lessons/81302

# 거리두기 확인하기

# 구글링 참고 ㅠㅠ - https://ckd2806.tistory.com/entry/%ED%8C%8C%EC%9D%B4%EC%8D%AC-python-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EA%B1%B0%EB%A6%AC%EB%91%90%EA%B8%B0-%ED%99%95%EC%9D%B8%ED%95%98%EA%B8%B0

from collections import deque

move_x = [1, 0, -1, 0]
move_y = [0, -1, 0, 1]


def bfs(place, x, y):
    visited = [[0 for y in range(5)] for x in range(5)]
    deq = deque()
    deq.append([x, y, 0])
    visited[x][y] = 1  # 각 인원별로 BFS를 돌면서 한 블록씩 이동할 때마다 1씩 가중치를 둠

    while deque:
        now = deq.popleft()

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
                    deq.append(nxt)
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