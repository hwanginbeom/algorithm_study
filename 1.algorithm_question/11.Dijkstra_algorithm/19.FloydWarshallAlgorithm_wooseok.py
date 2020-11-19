# 1. 플로이드
def solution1() :
    INF = int(1e9)  # 무한을 의미하는 값으로 10억을 설정

    # 노드의 개수 및 간선의 개수 입력
    n = int(input())
    m = int(input())

    # 2차원 리스트(그래프 표현)를 만들고, 무한으로 초기화
    graph = [[INF] * (n + 1) for _ in range(n + 1)]

    # 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            if a == b:
                graph[a][b] = 0

    # 각 간선에 대한 정보를 입력받아, 그 값으로 초기화
    for _ in range(m):
        # A에서 B로 가는 비용은 C라고 설정
        a, b, c = map(int, input().split())

        # 경로가 하나가 아닐수도 있다고 했으므로 최소 경로를 골라준다.
        graph[a][b] = min(c, graph[a][b])

    # 점화식에 따라 플로이드 워셜 알고리즘 수행
    for k in range(1, n + 1):
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

    # 수행된 결과를 출력
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            # 도달할 수 없는 경우, 무한(INFINITY)이라고 출력
            if graph[a][b] == INF:
                print(0, end=' ')
            # 도달할 수 있는 경우 거리를 출력
            else:
                print(graph[a][b], end=' ')

        print()


# solution1()



# 2. 운동
def solution2() :
    INF = int(1e9)  # 무한을 의미하는 값으로 10억을 설정

    # 노드의 개수 및 간선의 개수 입력
    v, e = map(int, input().split())

    # 2차원 리스트(그래프 표현)를 만들고, 무한으로 초기화
    graph = [[INF] * (v + 1) for _ in range(v + 1)]

    # 각 간선에 대한 정보를 입력받아, 그 값으로 초기화
    for _ in range(e):
        # A에서 B로 가는 비용은 C라고 설정
        a, b, c = map(int, input().split())
        graph[a][b] = c

    # 점화식에 따라 플로이드 워셜 알고리즘 수행
    for k in range(1, v + 1):
        for a in range(1, v + 1):
            for b in range(1, v + 1):
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

    # 최단 사이클 찾기
    min_cycle = INF
    for i in range(1, v + 1) :
        # graph[i][i]는 출발지에서 출발후 다시 돌아오는 경로를 담는다.
        min_cycle = min(min_cycle, graph[i][i])

    if min_cycle == INF :
        print(-1)
    else :
        print(min_cycle)


solution2()
