# 키 순서
def solution() :
    INF = int(1e9)  # 무한을 의미하는 값으로 10억을 설정

    n, m = map(int, input().split())

    # 2차원 리스트(그래프 표현)를 만들고, 무한으로 초기화
    graph = [[INF] * (n + 1) for _ in range(n + 1)]

    # 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            if a == b:
                graph[a][b] = 0

    # 각 간선에 대한 정보를 입력받아, 그 값으로 초기화
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a][b] = 1

    # 점화식에 따라 플로이드 워셜 알고리즘 수행
    for k in range(1, n + 1):
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

    count = 0

    # 특정 노드에 대하여, 이 노드까지 도달할 수 있는 노드의 종류와
    # 이 노드에서 갈 수 있는 노드의 종류의 합집합이
    # 모든 노드가 되면, 전제에서 자신의 키가 몇번째인지 알 수 있게 된다.
    # 로직 구현
    for i in range(1, n + 1) :
        INF_list = []

        for j in range(1, n + 1) :
            if graph[i][j] == INF :
                INF_list.append(j)

        for j in INF_list :
            if graph[j][i] == INF :
                break
        else :
            count += 1

    print(count)


solution()
