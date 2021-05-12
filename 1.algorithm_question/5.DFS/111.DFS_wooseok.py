# 유기농 배추
# https://www.acmicpc.net/problem/1012
import sys
sys.setrecursionlimit(10 ** 7)


def dfs(x, y, dx, dy, graph) :
    n = len(graph)
    m = len(graph[0])

    for i in range(4) :
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= n or ny < 0 or ny >= m :
            continue

        if graph[nx][ny] == 1 :
            graph[nx][ny] = 0
            graph = dfs(nx, ny, dx, dy, graph)

    return graph


def solution() :
    t = int(input())

    answer = []
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for _ in range(t):
        m, n, k = map(int, input().split())
        graph = [[0 for i in range(m)] for j in range(n)]

        for i in range(k) :
            y, x = map(int, input().split())

            graph[x][y] = 1

        count = 0

        for i in range(n) :
            for j in range(m) :
                if graph[i][j] == 1 :
                    graph = dfs(i, j, dx, dy, graph)
                    count += 1

        answer.append(count)

    for i in answer :
        print(i)


solution()
