import sys
sys.setrecursionlimit(10**7)

m, n, k = map(int, input().split())

arr = [[0] * (n + 1) for _ in range(m + 1)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]


def dfs(arr, i, j) :
    cnt = 1
    for k in range(4) :
        i_ = i + dx[k]
        j_ = j + dy[k]
        if (0 <= i_ < m) and (0 <= j_ < n) :
            if arr[i_][j_] == 0 :
                arr[i_][j_] = -1
                cnt += dfs(arr, i_, j_)
    return cnt


# 왼쪽 위가 기준이 아니라 왼쪽 아래에서 0,0으로 시작
for k in range(k) :
    lx, ly, rx, ry = map(int, input().split())

    while ly < ry :
        ux = lx
        while ux < rx :
            arr[m - 1 - ly][ux] = 1
            ux += 1
        ly += 1


square = 0
answer = []

# 깊이 우선 탐색
for i in range(m) :
    for j in range(n) :
        if arr[i][j] == 0 :
            arr[i][j] = -1
            answer.append(dfs(arr, i, j))
            square += 1


print(square)
answer.sort()
for i in range(len(answer)):
    print(answer[i], end=' ')
