# 1. N으로 표현



# 2. 정수 삼각형
def solution2(triangle):
    answer = 0
    dp = []

    for i in triangle:
        dp.append(i)

    # 인덱스 표시
    # 0
    # 0 1
    # 0 1 2
    # 0 1 2 3

    # 다이나믹 프로그래밍
    for i in range(1, len(dp)):
        for j in range(len(dp[i])):
            # 왼쪽 위에서 오는 경우
            if j == 0:
                left_up = 0
            else:
                left_up = dp[i - 1][j - 1]

            # 오른쪽 위에서 오는 경우
            if j == len(dp[i]) - 1:
                right_up = 0
            else:
                right_up = dp[i - 1][j]

            dp[i][j] = dp[i][j] + max(left_up, right_up)

    # print(dp)

    answer = max(dp[len(dp) - 1])

    return answer


triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
# print(solution2(triangle))



# 3. 가장 먼 노드
import heapq


def solution3(n, edge):
    answer = 0
    start = 1
    INF = int(1e9)

    graph = [[] for _ in range(n + 1)]

    for node in edge:
        start_node = node[0]
        end_node = node[1]

        # 양방향, 거리는 1
        graph[start_node].append([end_node, 1])
        graph[end_node].append([start_node, 1])

    distance = [INF] * (n + 1)

    # 다익스트라 알고리즘
    def dijkstra(start):
        q = []

        heapq.heappush(q, (0, start))
        distance[start] = 0

        while q:
            dist, now = heapq.heappop(q)

            if distance[now] < dist:
                continue

            for i in graph[now]:
                cost = dist + i[1]

                if cost < distance[i[0]]:
                    distance[i[0]] = cost
                    heapq.heappush(q, (cost, i[0]))

    dijkstra(start)

    max_distance = 0

    # print(distance)

    # INF보다 작은 최대 거리 구하기
    for d in distance:
        if d < INF:
            max_distance = max(max_distance, d)

    # print(max_distance)

    # 최대 거리를 가진 노드 개수 구하기
    for d in distance:
        if d == max_distance:
            answer += 1

    return answer


n = 6
vertex = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
print(solution3(n, vertex))
