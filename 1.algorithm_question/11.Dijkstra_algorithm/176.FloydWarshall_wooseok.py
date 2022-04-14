# 역사
# https://www.acmicpc.net/problem/1613


def solution() :
    INF = int(1e9)
    n, k = map(int, input().split())
    graph = [[INF] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1) :
        for j in range(1, n + 1) :
            if i == j :
                graph[i][j] = 0

    for _ in range(k) :
        a, b = map(int, input().split())
        graph[a][b] = 1

    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    s = int(input())
    event_list = []

    for _ in range(s) :
        a, b = map(int, input().split())
        event_list.append([a, b])

    answer = []

    for event in event_list :
        if graph[event[0]][event[1]] != INF :
            answer.append(-1)
        elif graph[event[1]][event[0]] != INF :
            answer.append(1)
        else :
            answer.append(0)

    for i in answer :
        print(i)


solution()
