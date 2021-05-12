def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False

    if graph[x][y] == 1:
        graph[x][y] = 0
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False

T = int(input()) # T:테스트 케이스

for _ in range(T):
    m, n, k = map(int, input().split()) # m:가로길이, n:세로길이, k:배추심어진위치
    graph = [[0]*m for _ in range(n)]

    for _ in range(k):
        a, b = map(int, input().split()) # a:배추x위치, b:배추y위치
        graph[b][a] = 1

    result = 0
    answer = []
    for i in range(n):
        for j in range(m):
            if dfs(i, j) == True:
                result += 1
    print(result)

