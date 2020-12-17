# 저울
def solution() :
    n = int(input())
    m = int(input())

    INF = int(1e9)
    graph = [[INF] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1) :
        for j in range(1, n + 1) :
            if i == j :
                graph[i][j] = 0

    for _ in range(m) :
        a, b = map(int, input().split())
        # graph[a][b]는 a가 b보다 큰가? 로 지정하여
        # 맞으면 1, 아니면 -1을 저장
        graph[a][b] = 1
        graph[b][a] = -1

    for k in range(1, n + 1):
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                if graph[a][b] == INF :
                    # a가 k보다 크고 k가 b보다 크면
                    # a가 b보다 크다 라는 결론 도달
                    if graph[a][k] == 1 and graph[k][b] == 1 :
                        graph[a][b] = 1
                        graph[b][a] = -1
                    # 반대!
                    elif graph[a][k] == -1 and graph[k][b] == -1 :
                        graph[a][b] = -1
                        graph[b][a] = 1

    for i in range(1, n + 1) :
        sum = 0

        for j in range(1, n + 1) :
            if graph[i][j] == INF :
                sum += 1

        print(sum)


solution()
