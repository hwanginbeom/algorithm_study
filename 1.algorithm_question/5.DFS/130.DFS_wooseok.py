# 섬의 개수
# https://www.acmicpc.net/problem/4963
import sys
sys.setrecursionlimit(10 ** 7)


def dfs(island, x, y, h, w) :
    # 주어진 범위를 벗어나는 경우 즉시 종료
    if x <= -1 or x >= h or y <= -1 or y >= w:
        return False

    if island[x][y] == 1 :
        island[x][y] = 0

        # 상하좌우
        dfs(island, x - 1, y, h, w)
        dfs(island, x, y - 1, h, w)
        dfs(island, x + 1, y, h, w)
        dfs(island, x, y + 1, h, w)

        # 대각
        dfs(island, x - 1, y - 1, h, w)
        dfs(island, x - 1, y + 1, h, w)
        dfs(island, x + 1, y - 1, h, w)
        dfs(island, x + 1, y + 1, h, w)

        return True

    return False


def solution() :
    answer = []

    while True :
        w, h = map(int, input().split())

        if w == 0 and h == 0 :
            break

        island = []
        count = 0

        for _ in range(h) :
            temp = list(map(int, input().split()))
            island.append(temp)

        for i in range(h) :
            for j in range(w) :
                if island[i][j] == 1 :
                    dfs(island, i, j, h, w)
                    count += 1

        answer.append(count)

    for i in answer :
        print(i)


solution()
