# 2021-03-23

# 출처 : https://www.acmicpc.net/problem/11724

# 연결 요소의 개수

# 방향 없는 그래프가 주어졌을 때, 연결 요소 (Connected Component)의 개수를 구하는 프로그램을 작성하시오.

# 왜 python3는 런타임 에러이고 pypy3는 정답일까....ㅎ

import sys
input=sys.stdin.readline

N,M=map(int,input().split())

graph=[[] for _ in range(N+1)]
visited=[False]*(N+1)
answer=0

for _ in range(M):
    u,v=map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)


def dfs(graph,v,visited):
    visited[v]=True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)

for i in range(1,N+1):
    if not visited[i]:
        dfs(graph,i,visited)
        answer+=1

print(answer)