import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


def dfs(x, y, graph):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    if graph[x][y] == 1:
        graph[x][y] = 0
        # 상하좌우
        dfs(x - 1, y, graph)
        dfs(x + 1, y, graph)
        dfs(x, y - 1, graph)
        dfs(x, y + 1, graph)
        # 대각선
        dfs(x - 1, y - 1, graph)
        dfs(x + 1, y - 1, graph)
        dfs(x + 1, y + 1, graph)
        dfs(x - 1, y + 1, graph)
        return True
    return False


def solution(n, m):
    graph = []
    for i in range(n):
        graph.append(list(map(int, input().split())))
    result = 0
    for i in range(n):
        for j in range(m):
            if dfs(i, j, graph) == True:
                result += 1
    print(result)


while True:
    w, h = map(int, input().split())
    if w != 0 and h != 0:
        n = h
        m = w
        solution(n, m)
    else:
        break
