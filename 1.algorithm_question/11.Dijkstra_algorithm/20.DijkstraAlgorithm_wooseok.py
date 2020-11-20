# 1. 미확인 도착지
import heapq


def solution1() :
    def dijkstra(start):
        INF = int(1e9)  # 무한을 의미하는 값으로 10억을 설정

        q = []
        distance = [INF] * (n + 1)

        # 시작 노드로 가기 위한 최단 거리는 0으로 설정하여, 큐에 삽입
        heapq.heappush(q, (0, start))
        distance[start] = 0

        while q:  # 큐가 비어있지 않다면
            # 가장 최단 거리가 짧은 노드에 대한 정보를 꺼내기
            dist, now = heapq.heappop(q)

            if distance[now] < dist:
                continue

            # 현재 노드와 연결된 다른 인접한 노드들을 학완
            for i in graph[now]:
                cost = dist + i[1]

                # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
                if cost < distance[i[0]]:
                    distance[i[0]] = cost
                    heapq.heappush(q, (cost, i[0]))

        return distance

    T = int(input())

    for _ in range(T):
        n, m, t = map(int, input().split())
        start, g, h = map(int, input().split())

        graph = [[] for _ in range(n + 1)]
        destination = []

        for j in range(m):
            a, b, d = map(int, input().split())
            graph[a].append([b, d])
            graph[b].append([a, d])

        for k in range(t):
            destination.append(int(input()))

        start_ = dijkstra(start)
        g_ = dijkstra(g)
        h_ = dijkstra(h)

        answer = []

        for l in destination:
            if start_[g] + g_[h] + h_[l] == start_[l] or start_[h] + h_[g] + g_[l] == start_[l]:
                answer.append(l)

        answer.sort()

        for f in answer:
            print(f, end=' ')

        print()


# solution1()



# 2. KCM Travel
import sys


def solution2() :
    t = int(input())
    INF = sys.maxsize

    for _ in range(t):
        # 공항수, 지원비용, 티켓정보수
        n, m, k = map(int, input().split())
        ticket = [[] for _ in range(n + 1)]

        for _ in range(k):
            # 출발, 도착, 비용, 소요시간
            u, v, c, d = map(int, input().split())
            ticket[u].append([v, c, d])

        # 열 : 비용, 행 : n까지 갈때
        DP = [[INF for _ in range(m + 1)] for _ in range(n + 1)]
        DP[1][0] = 0  # 1 -> 1로 갔을때 비용은 0, 시간도 0

        for c in range(m + 1):
            for d in range(1, n + 1):
                # c의 비용으로 d에 도착하는 경우가 없다면
                if DP[d][c] == INF:
                    continue

                    # c의 비용으로 d에 도착했을 때의 소요시간
                t = DP[d][c]

                # d에서 출발하는 모든경우
                for dv, dc, dd in ticket[d]:
                    # 비용이 초과될경우 넘어간다
                    if dc + c > m:
                        continue

                    # 이전에 저장된값과 비교하여 작다면 갱신해준다
                    DP[dv][dc + c] = min(DP[dv][dc + c], t + dd)

        # N에 도착할때 최소소요시간
        result = min(DP[n])

        if result == INF:
            print('Poor KCM')
        else:
            print(result)


solution2()
