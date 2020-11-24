# 1. N으로 표현
def solution1(N, number) :
    if N == number:
        return 1

    # 1. [ SET x 8 ] 초기화
    s = [set() for x in range(8)]

    # 2. 각 set마다 기본 수 "N" * i 수 초기화
    for i, x in enumerate(s, start=1):
        x.add(int(str(N) * i))

    # 3. n 일반화
    #   {
    #       "n" * i U
    #       1번 set 사칙연산 n-1번 set U
    #       2번 set 사칙연산 n-2번 set U
    #       ...
    #       n-1번 set 사칙연산 1번 set,
    #    }
    # number를 가장 최소로 만드는 수 구함.
    for i in range(1, 8):
        for j in range(i):
            for op1 in s[j]:
                for op2 in s[i - j - 1]:
                    s[i].add(op1 + op2)
                    s[i].add(op1 - op2)
                    s[i].add(op1 * op2)
                    if op2 != 0:
                        s[i].add(op1 // op2)

        if number in s[i]:
            answer = i + 1
            break

    else:
        answer = -1

    return answer


N = 5
number = 12
print(solution1(N, number))



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
# print(solution3(n, vertex))
