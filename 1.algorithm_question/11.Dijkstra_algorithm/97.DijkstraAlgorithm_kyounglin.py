# 2021-03-29

# 출처 : https://www.acmicpc.net/problem/1238

# 파티

# N개의 숫자로 구분된 각각의 마을에 한 명의 학생이 살고 있다.
#
# 어느 날 이 N명의 학생이 X (1 ≤ X ≤ N)번 마을에 모여서 파티를 벌이기로 했다. 이 마을 사이에는 총 M개의 단방향 도로들이 있고 i번째 길을 지나는데 Ti(1 ≤ Ti ≤ 100)의 시간을 소비한다.
#
# 각각의 학생들은 파티에 참석하기 위해 걸어가서 다시 그들의 마을로 돌아와야 한다. 하지만 이 학생들은 워낙 게을러서 최단 시간에 오고 가기를 원한다.
#
# 이 도로들은 단방향이기 때문에 아마 그들이 오고 가는 길이 다를지도 모른다. N명의 학생들 중 오고 가는데 가장 많은 시간을 소비하는 학생은 누구일지 구하여라.

import sys
input = sys.stdin.readline
import heapq

INF = int(1e9)

# 노드의 수, 간선의 수 입력받기
N,M,X=map(int,input().split())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트
graph=[[] for i in range(N)]
# 최단 거리 테이블을 모두 무한으로 초기화



# 모든 간선의 정보 입력받기
for _ in range(M):
    s,e,t = map(int,input().split())
    # a번 노드에서 b번 노드로 가는 비용 c
    graph[s-1].append([e-1,t])


def dijkstra(n,x):
    distance = [INF] * (N)
    q=[]
    # 시작 노드로 가기 위한 최단 거리는 0으로 설정하여, 큐에 삽입
    heapq.heappush(q,(0,x))
    # 시작노드에 대해 초기화
    distance[x]=0

    while q: # 큐가 비어있지 않다면
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist,now=heapq.heappop(q)

        # 현재 노드와 연결된 다른 인접한 노드를을 확인
        for i in graph[now]:
            cost=dist+i[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost<distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))

    return distance

answer=[0]*(N)

for i in range(N):
    check=dijkstra(N,i)
    if i==X:
        for idx,j in enumerate(check):
            answer[idx]+=j
    else:
        answer[i]+=check[X]



print(max(answer))


