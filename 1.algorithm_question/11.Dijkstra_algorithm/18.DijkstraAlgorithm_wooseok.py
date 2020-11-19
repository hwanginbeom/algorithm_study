# 1. 최단경로
import heapq


def solution1() :
    INF = int(1e9)  # 무한을 의미하는 값으로 10억을 설정

    # 정점과 간선의 수 입력
    V, E = map(int, input().split())

    # 시작 노드 번호 입력
    start = int(input())

    # 노드들의 연결정보를 담을 리스트 생성
    graph = [[] for i in range(V + 1)]

    for _ in range(E) :
        u, v, w = map(int, input().split())
        graph[u].append((v, w))

    distance = [INF] * (V + 1)

    def dijkstra(start):
        q = []

        # 시작 노드로 가기 위한 최단 거리는 0으로 설정하여, 큐에 삽입
        heapq.heappush(q, (0, start))
        distance[start] = 0

        while q:  # 큐가 비어있지 않다면
            # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
            dist, now = heapq.heappop(q)

            # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
            if distance[now] < dist:
                continue

            # 현재 노드와 연결된 다른 인접한 노드들을 확인
            for i in graph[now]:
                cost = dist + i[1]

                # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
                if cost < distance[i[0]]:
                    distance[i[0]] = cost
                    heapq.heappush(q, (cost, i[0]))

    # 다익스트라 알고리즘을 수행
    dijkstra(start)

    # 모든 노드로 가기 위한 최단 거리를 출력
    for i in range(1, V + 1):
        # 도달할 수 없는 경우, 무한(INFINITY)이라고 출력
        if distance[i] == INF:
            print('INF')
        # 도달할 수 있는 경우 거리를 출력
        else:
            print(distance[i])



solution1()



# 2. 특정한 최단경로
import heapq


def solution2() :
    INF = int(1e9)  # 무한을 의미하는 값으로 10억을 설정

    V, E = map(int, input().split())
    start = 1

    graph = [[] for i in range(V + 1)]

    for _ in range(E):
        u, v, w = map(int, input().split())
        graph[u].append((v, w))
        graph[v].append((u, w))

    v1, v2 = map(int, input().split())

    def dijkstra(start):
        distance = [INF] * (V + 1)
        q = []

        # 시작 노드로 가기 위한 최단 거리는 0으로 설정하여, 큐에 삽입
        heapq.heappush(q, (0, start))
        distance[start] = 0

        while q:  # 큐가 비어있지 않다면
            # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
            dist, now = heapq.heappop(q)

            # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
            if distance[now] < dist:
                continue

            # 현재 노드와 연결된 다른 인접한 노드들을 확인
            for i in graph[now]:
                cost = dist + i[1]

                # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
                if cost < distance[i[0]]:
                    distance[i[0]] = cost
                    heapq.heappush(q, (cost, i[0]))

        return distance

    # 다익스트라 알고리즘을 수행
    start = dijkstra(start)
    v1_path = dijkstra(v1)
    v2_path = dijkstra(v2)

    cnt = min(start[v1] + v1_path[v2] + v2_path[V], start[v2] + v2_path[v1] + v1_path[V])

    print(cnt if cnt < INF else -1)


solution2()
