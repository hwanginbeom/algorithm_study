# 2021-01-19

# 출처 : https://www.acmicpc.net/problem/18352

# 특정 거리의 도시 찾기

#어떤 나라에는 1번부터 N번까지의 도시와 M개의 단방향 도로가 존재한다. 모든 도로의 거리는 1이다.
#이 때 특정한 도시 X로부터 출발하여 도달할 수 있는 모든 도시 중에서, 최단 거리가 정확히 K인 모든 도시들의 번호를 출력하는 프로그램을 작성하시오.
# 또한 출발 도시 X에서 출발 도시 X로 가는 최단 거리는 항상 0이라고 가정한다.
# N=4, K=2, X=1일 때 다음과 같이 그래프가 구성되어 있다고 가정하자.

# 이 때 1번 도시에서 출발하여 도달할 수 있는 도시 중에서, 최단 거리가 2인 도시는 4번 도시 뿐이다.
# 2번과 3번 도시의 경우, 최단 거리가 1이기 때문에 출력하지 않는다.

import heapq
import sys
INF=int(1e9)
input = sys.stdin.readline

# 도시의 수 거리의 수 거리의 정보 출발 도시 번호 입력

n,m,k,x=map(int,input().split())

# 도시와 거리 연결
graph=[[] for _ in range(n+1)]
# 최단 거리 모두 초기화
distance=[INF]*(n+1)

# 모든 거리 정보 입력받기
for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append((b,1))


def dijkstra(x):
    q=[]
    heapq.heappush(q,(0,x))
    distance[x]=0
    while q: # 큐가 비어있지 않을 때까지
        dist,now =heapq.heappop(q) # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        if distance[now]<dist: # 이미 처리된 노드 무시하기
            continue
        # 인접한 노드 확인
        for i in graph[now]:
            cost = dist + i[1]

            if cost<distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))


dijkstra(x)

if k in distance:
    for i in range(len(distance)):
        if distance[i]==k:
            print(i)

else:
    print(-1)


