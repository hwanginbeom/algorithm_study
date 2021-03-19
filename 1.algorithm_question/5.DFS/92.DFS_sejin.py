from math import inf
import sys
sys.setrecursionlimit(10**7)

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().rstrip())))

shortest = [[inf] * m for _ in range(n)]
shortest[0][0] = 1


# DFS 알고리즘으로 미로 찾기
def find_path(r, c, end_r, end_c, dist):

    if r < end_r:
        if (graph[r + 1][c] == 1) and (dist[r + 1][c] > dist[r][c] + 1):
            dist[r + 1][c] = dist[r][c] + 1
            find_path(r + 1, c, end_r, end_c, dist)

    if c < end_c:
        if (graph[r][c + 1] == 1) and (dist[r][c + 1] > dist[r][c] + 1):
            dist[r][c + 1] = dist[r][c] + 1
            find_path(r, c + 1, end_r, end_c, dist)

    if r > 0:
        if (graph[r - 1][c] == 1) and (dist[r - 1][c] > dist[r][c] + 1):
            dist[r - 1][c] = dist[r][c] + 1
            find_path(r - 1, c, end_r, end_c, dist)

    if c > 0:
        if (graph[r][c - 1] == 1) and (dist[r][c - 1] > dist[r][c] + 1):
            dist[r][c - 1] = dist[r][c] + 1
            find_path(r, c - 1, end_r, end_c, dist)

    return dist[end_r][end_c]

print(find_path(0, 0, n - 1, m - 1, shortest))