# 해킹
# https://www.acmicpc.net/problem/10282
import heapq


def dijkstra(start, graph, distance) :
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
                heapq.heappush(queue, (cost, i[0]))

    return distance


def solution() :
    answer = []
    t = int(input())
    INF = int(1e9)

    for _ in range(t) :
        n, d, c = map(int, input().split())
        graph = [[] for _ in range(n + 1)]
        distance = [INF] * (n + 1)

        for _ in range(d) :
            a, b, s = map(int, input().split())
            graph[b].append((a, s))

        distance = dijkstra(c, graph, distance)
        # print(distance)

        time_list = []
        for i in distance :
            if i != INF :
                time_list.append(i)

        answer.append([len(time_list), max(time_list)])

    for i in answer :
        print(i[0], i[1])


solution()
# 다익스트라 알고리즘은
# 결국 시작 노드에서 다른 노드로 갈 수 있는 최단 거리를 구하는 알고리즘이기 때문에
# distance 리스트에서 INF 값을 제외한 값들 중 최대값이
# 감염될 수 있는 모든 컴퓨터들 중에서 가장 마지막으로 감염되는 컴퓨터까지의 시간의 최소값이 된다.
