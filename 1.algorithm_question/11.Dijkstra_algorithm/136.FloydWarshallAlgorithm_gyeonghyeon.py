import sys

input = sys.stdin.readline

INF = int(1e9)
n,m=map(int,input().split())

board = [[INF]*n for _ in range(n)]

stopover = [[0]*n for _ in range(n)]


for _ in range(m):
    a,b,c = map(int,input().split())
    board[a-1][b-1]=c
    board[b-1][a-1]=c
    stopover[a-1][b-1]=b
    stopover[b-1][a-1]=a

for a in range(n):
    for b in range(n):
        if a==b:
            board[a][b]=0
            stopover[a][b]=-1


for k in range(n):
    for a in range(n):
        for b in range(n):
            if board[a][b] > board[a][k]+board[k][b]:
                board[a][b] = board[a][k]+board[k][b]
                stopover[a][b] = stopover[a][k]

for a in range(n):
    for b in range(n):
        if a==b :
            print("-",end=' ')
        else:
            print(stopover[a][b], end=' ')
    print()