import sys
input = sys.stdin.readline

def solution():
    INF = int(1e9)

    n = int(input())
    m = int(input())

    graph = [[INF] * (n + 1) for _ in range(n + 1)]

    for a in range(1, n + 1):
        graph[a][a] = 0

    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a][b] = min(graph[a][b], c)

    for k in range(1, n + 1):
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

    for idx, value in enumerate(graph[1:]):
        for idx2, value2 in enumerate(value):
            if value2 == INF:
                graph[idx+1][idx2] = 0
        print(*graph[idx+1][1:], sep=" ")

solution()