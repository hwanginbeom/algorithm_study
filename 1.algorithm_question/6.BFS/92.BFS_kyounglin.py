# 2021-03-19

# 출처 : https://www.acmicpc.net/problem/2178

# 미로탐색
#
# N×M크기의 배열로 표현되는 미로가 있다.
#
# 1	0	1	1	1	1
# 1	0	1	0	1	0
# 1	0	1	0	1	1
# 1	1	1	0	1	1
# 미로에서 1은 이동할 수 있는 칸을 나타내고, 0은 이동할 수 없는 칸을 나타낸다. 이러한 미로가 주어졌을 때, (1, 1)에서 출발하여 (N, M)의 위치로 이동할 때 지나야 하는 최소의 칸 수를 구하는 프로그램을 작성하시오. 한 칸에서 다른 칸으로 이동할 때, 서로 인접한 칸으로만 이동할 수 있다.
#
# 위의 예에서는 15칸을 지나야 (N, M)의 위치로 이동할 수 있다. 칸을 셀 때에는 시작 위치와 도착 위치도 포함한다.


from collections import deque

n,m=map(int,input().split())

graph=[]
for i in range(n):
    graph.append(list(map(int,input())))

# 이동할 네 방향 정의
dx=[-1,1,0,0] # 행
dy=[0,0,-1,1] # 열

def bfs(x,y): # x,y는 시작위치
    queue=deque()
    queue.append((x,y))
    while queue: # 큐가 빌때까지 반복
        x,y=queue.popleft()
        for i in range(4): # 현재 위치에서 상하좌우 확인
            nx=x+dx[i]
            ny=y+dy[i]
            # 공간을 벗어난 경우
            if nx<0 or ny<0 or nx>=n or ny>=m:
                continue
            # 0인 경우
            if graph[nx][ny]==0:
                continue
            # 처음 방문하는 경우
            if graph[nx][ny]==1:
                graph[nx][ny]=graph[x][y]+1
                queue.append((nx,ny))

    return graph[n-1][m-1] # (n,m) 위치 리턴

print(bfs(0,0)) # 시작위치

