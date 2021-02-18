import heapq
import sys
input = sys.stdin.readline

n, m, r = map(int, input().split()) #n:지역개수, m:수색범위, r길의개수
t = [0]
t.extend(list(map(int, input().split()))) #t:지역아이템수(1~)


# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트 만들기
graph = [[] for _ in range(n + 1)]

# 모든 간선 정보를 입력받기
for _ in range(r):
    a, b, l = map(int, input().split()) #a,b:길존재하는지역번호, l:길의길이
    # a번 노드에서 b번 노드로 가는 비용이 l이라는 의미
    graph[a].append([b, l])
    graph[b].append([a, l])


def dijkstra(start) :
    # 최단 거리 테이블을 모두 무한 => m+1 로 초기화
    distance = [m + 1] * (n + 1)  # m+1이 최대가 되는것
    q = []

    # 시작 노드로 가기 위한 최단 거리는 0으로 설정하여 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0

    # 큐가 비어있지 않다면
    while q:
        # 가장 최단 거리가 짧은 노드에 대한 정보를 꺼내기
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]

            # 현재 노드를 거쳐, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    return distance

def total(x) :
    total_item = 0
    for i in range(len(x)):
        # 도달할 수 있는 노드의 경우
        if x[i] < m+1 :
            total_item += t[i]
    return total_item


answer = 0
for i in range(1,n+1) :
   answer = max(answer, total(dijkstra(i)))
print(answer)


