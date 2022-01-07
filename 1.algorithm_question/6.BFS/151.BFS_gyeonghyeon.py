import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
t = int(input())

def dfs(graph, x,y, m , n):
    if x <= -1 or x >= m or y <= -1 or y >= n:
        return False
    if graph[x][y] == 1:
        graph[x][y] = 0
        dfs(graph, x - 1, y, m , n)
        dfs(graph, x, y - 1, m , n)
        dfs(graph, x + 1, y, m , n)
        dfs(graph, x, y + 1,m , n)
        return True
    return False

def solution():
    m, n, k = map(int, input().split())
    graph = [  [0 for _ in range(n)] for _ in range(m)]
    for i in range(k):
        a, b = map(int, input().split())
        graph[a][b] = 1
    result = 0
    for i in range(m):
        for j in range(n):
            if dfs(graph, i, j, m , n) == True:
                result += 1
    print(result)

for _ in range(t):
    solution()