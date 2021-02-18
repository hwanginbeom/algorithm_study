# 서강그라운드
import heapq


def solution() :
    n, m, r = map(int, input().split())
    item_num = list(map(int, input().split()))

    graph = [[] for _ in range(n + 1)]
    for _ in range(r) :
        a, b, c = map(int, input().split())

        graph[a].append((b, c))
        graph[b].append((a, c))

    distance = [int(1e9)] * (n + 1)

    # 다익스트라 알고리즘
    def dijkstra(start) :
        q = []

        heapq.heappush(q, (0, start))
        distance[start] = 0

        while q :
            dist, now = heapq.heappop(q)

            if distance[now] < dist :
                continue

            for i in graph[now] :
                cost = dist + i[1]

                if cost < distance[i[0]] :
                    distance[i[0]] = cost
                    heapq.heappush(q, (cost, i[0]))

    answer = 0

    for i in range(1, n + 1) :
        # 시작 노드를 바꿔가면서 최단거리 계산
        dijkstra(i)
        item = 0

        for j in range(1, len(distance)) :
            # 수색범위가 m 이하인 노드에 대해 아이템 개수 +
            if distance[j] <= m :
                item += item_num[j - 1]

        answer = max(answer, item)

        # 최단거리 기록 변수 초기화
        distance = [int(1e9)] * (n + 1)

    print(answer)


solution()
