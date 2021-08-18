# 최소비용 구하기 2
# https://www.acmicpc.net/problem/11779
import heapq


def solution() :
    n = int(input())
    m = int(input())

    graph = [[] for _ in range(n + 1)]
    for _ in range(m) :
        a, b, c = map(int, input().split())
        graph[a].append((b, c))

    start, end = map(int, input().split())

    INF = int(1e9)
    distance = [INF] * (n + 1)
    path = [-1 for _ in range(n + 1)]

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

    dijkstra(start)
    print(distance[end])

    shortest_path = []

    # 경로 역추적
    while True :
        shortest_path.append(str(end))
        end = path[end]

        if end == -1 :
            break

    print(len(shortest_path))
    print(' '.join(shortest_path[::-1]))


solution()
