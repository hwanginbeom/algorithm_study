# 1. N으로 표현
def solution(N, number):
    answer = -1
    s = [set() for x in range(8)]

    for i, x in enumerate(s, start=1):
        x.add(int(str(N)*i))

    for i in range(1, len(s)):
        for j in range(i):
            for a in s[j]:
                for b in s[i-j-1]:
                    s[i].add(a+b)
                    s[i].add(a-b)
                    s[i].add(a*b)
                    if b != 0:
                        s[i].add(a//b)
        if number in s[i]:
            answer = i + 1
            break
            
    return answer


# 2. 정수 삼각형
def solution2(triangle):
    answer = 0
    dp = []

    for i in triangle:
        dp.append(i)

    for i in range(1, len(dp)):
        for j in range(len(dp[i])):
            if j == 0:
                left_up = 0
            else:
                left_up = dp[i-1][j-1]

            if j == len(dp[i]) - 1:
                right_up = 0
            else:
                right_up = dp[i-1][j]

            dp[i][j] = dp[i][j] + max(left_up, right_up)

            answer = max(dp[len(dp) - 1])

            return answer


# 3. 가장 먼 노드
import heapq

def solution3(n, edge):
    answer = 0
    start = 1
    INF = int(1e9)

    graph = [[] for _ in range(n+1)]

    for node in edge:
        start_node = node[0]
        end_node = node[1]

        graph[start_node].append([end_node, 1])
        graph[end_node].append([start_node, 1])

    distance = [INF] * (n+1)

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

    for d in distance:
        if d < INF:
            max_distance = max(max_distance, d)

    for d in distance:
        if d == max_distance:
            answer += 1

    return answer
