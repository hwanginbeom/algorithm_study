# 여행 가자
# https://www.acmicpc.net/problem/1976
from collections import deque


def bfs(graph, visited, start, next) :
    if start == next : # 함정카드
        return True

    queue = deque([start])
    isFlag = False

    visited[start] = True

    while queue :
        v = queue.popleft()

        for i in graph[v] :
            if i == next :
                isFlag = True
                break

            if not visited[i] :
                queue.append(i)
                visited[i] = True

        if isFlag :
            break

    return isFlag


def solution() :
    answer = 'YES'
    n = int(input())
    m = int(input())

    graph = [[] for _ in range(n + 1)]

    for i in range(n) :
        conn_list = list(map(int, input().split()))

        for j in range(len(conn_list)) :
            if conn_list[j] == 1 :
                graph[i + 1].append(j + 1)

    travel_plan = list(map(int, input().split()))

    for i in range(m) :
        visited = [False] * (n + 1)

        if i != m - 1 :
            if not bfs(graph, visited, travel_plan[i], travel_plan[i + 1]) :
                answer = 'NO'
                break

    print(answer)


solution()
