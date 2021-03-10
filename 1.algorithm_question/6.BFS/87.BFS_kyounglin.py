# 2021-03-10

# 출처 : https://www.acmicpc.net/problem/11725

# 트리의 부모 찾기

# 루트 없는 트리가 주어진다. 이때, 트리의 루트를 1이라고 정했을 때, 각 노드의 부모를 구하는 프로그램을 작성하시오.


from collections import deque
import sys

input=sys.stdin.readline

n=int(input())

graph=[[] for _ in range(n+1)]
visited=[0]*(n+1) # 방문처리
visited[1]=1

for _ in range(n-1):
    x,y=map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

def bfs(graph,start,visited):
    queue=deque([start])
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 원소 뽑아 출력
        v=queue.popleft()
        # 아직 방문하지 않은 인접한 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                visited[i]=v
                queue.append(i)

    for j in visited[2:]:
        print(j)

# 함수 호출
bfs(graph,1,visited)