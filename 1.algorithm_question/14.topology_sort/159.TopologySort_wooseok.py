# 문제집
# https://www.acmicpc.net/problem/1766
import heapq


def topology_sort(n, indegree, graph) :
    result = []
    queue = []

    for i in range(1, n + 1) :
        if indegree[i] == 0 :
            heapq.heappush(queue, i)

    while queue :
        now = heapq.heappop(queue)

        result.append(now)

        for i in graph[now] :
            indegree[i] -= 1

            if indegree[i] == 0 :
                heapq.heappush(queue, i)

    return result


def solution() :
    n, m = map(int, input().split())

    indegree = [0] * (n + 1)
    graph = [[] for _ in range(n + 1)]

    for _ in range(m) :
        a, b = map(int, input().split())
        graph[a].append(b)

        indegree[b] += 1

    result = topology_sort(n, indegree, graph)

    for i in result :
        print(i, end = ' ')


solution()
