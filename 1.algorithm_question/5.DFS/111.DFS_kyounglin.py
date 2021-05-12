# 2021-05-12

# 출처 : https://www.acmicpc.net/problem/1012

# 유기농 배추

# dfs로 특정 노드를 방문하고 연결된 모든 노드들도 방문

import sys
sys.setrecursionlimit(10**7)

def dfs(x, y):
    # 주어진 좌표/ 공간을 벗어나면 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    # 현재 노드를 아직 방문하지 않았다면 0인 상태
    if graph[x][y] == 1:
        # 노드를 방문처리
        graph[x][y] = 0
        # 상,하,좌,우 위치들도 모두 재귀적으로 호출
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False


t=int(input())
answer=[]

for _ in range(t):

    m,n,k=map(int,input().split())

    # 2차원 리스트의 맵 정보 입력받기
    graph=[[0]*m for _ in range(n)]

    for _ in range(k):
        b,a=map(int,input().split())
        graph[a][b]=1

    result=0
    for i in range(n):
        for j in range(m):
            # 현재 위치에서 dfs 수행
            if dfs(i,j)==True:
                result+=1
    answer.append(result)

for i in answer:
    print(i)