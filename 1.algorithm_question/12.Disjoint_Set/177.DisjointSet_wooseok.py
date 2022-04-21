# 중량제한
# https://www.acmicpc.net/problem/1939
from collections import deque


def bfs(graph, n, start_island, end_island, middle) :
    queue = deque([start_island])
    visited = [False] * (n + 1)
    visited[start_island] = True

    while queue :
        node = queue.popleft()

        if node == end_island :
            return True

        for i in graph[node] :
            if not visited[i[0]] :
                if i[1] >= middle :
                    queue.append(i[0])
                    visited[i[0]] = True

    return False


def solution() :
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    weight_list = []

    for _ in range(m) :
        a, b, c = map(int, input().split())
        graph[a].append([b, c])
        graph[b].append([a, c])

        weight_list.append(c)

    max_weight = max(weight_list)
    start_island, end_island = map(int, input().split())

    # 이분 탐색
    # 중량을 기준값로 해당 중량이 목적지까지 갈 수 있는지 없는지 검사
    start = 0
    end = max_weight
    answer = 0

    while start <= end :
        middle = (start + end) // 2

        if bfs(graph, n, start_island, end_island, middle) :
            answer = middle
            start = middle + 1
        else :
            end = middle - 1

    print(answer)


solution()
# 서로소 문제인줄 알았지만
# 이분탐색과 BFS 문제였다...
