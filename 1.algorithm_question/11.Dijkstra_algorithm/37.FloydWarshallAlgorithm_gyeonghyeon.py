n, m = int(input()), int(input())
a = [[0]*(n+1) for _ in range(n+1)]
INF = int(1e9)
for _ in range(m):
    x, y = map(int, input().split())
    a[x][y] = 1

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if a[i][k] and a[k][j]:
                a[i][j] = 1

for i in range(1,n+1):
    cnt = 0
    for j in range(1,n+1):
        if not a[i][j] and not a[j][i]:
            cnt += 1
    print(cnt-1)