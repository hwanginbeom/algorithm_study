# 택배
# https://www.acmicpc.net/problem/1719
import heapq


def solution() :
    n, m = map(int, input().split())

    graph = [[] for _ in range(n + 1)]
    for _ in range(m) :
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
        graph[b].append((a, c))

    INF = int(1e9)

    # 다익스트라 알고리즘
    def dijkstra(start) :
        queue = []

        heapq.heappush(queue, (0, start))
        distance[start] = 0

        while queue :
            dist, now = heapq.heappop(queue)

            if distance[now] < dist :
                continue

            for i in graph[now] :
                cost = dist + i[1]

                if cost < distance[i[0]] :
                    distance[i[0]] = cost
                    path[i[0]] = now # 경로를 역추적하기 위해 인덱스 번호 노드에 연결된 노드 번호 저장
                    heapq.heappush(queue, (cost, i[0]))

    answer = [['-'] * (n + 1) for _ in range(n + 1)]

    # 다익스트라 알고리즘을 활용한 플로이드-워셜 알고리즘
    for i in range(1, n + 1) :
        distance = [INF] * (n + 1)
        path = [-1 for _ in range(n + 1)]
        dijkstra(i)

        for j in range(1, n + 1) :
            if i == j :
                continue

            shortest_path = []
            end = j

            # 경로 역추적
            while True :
                shortest_path.append(end)
                end = path[end]

                if end == i :
                    break

            answer[i][j] = shortest_path[-1]

    for i in range(1, n + 1) :
        for j in range(1, n + 1) :
            print(answer[i][j], end = ' ')
        print()


solution()
