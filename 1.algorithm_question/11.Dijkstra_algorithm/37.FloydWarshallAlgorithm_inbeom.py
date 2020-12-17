# 10159 저울

INF = int(1e9)  # 무한을 의미하는 값으로 10억을 설정

# 노드의 개수 및 간선의 개수를 입력 받기

n = int(input())
m = int(input())

# 2차원 리스트(그래프 표현)를 만들고, 무한 으로 초기화
graph = [[0] * (n + 1) for _ in range(n + 1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0 으로 초기화
# for a in range(1, n + 1):
#     for b in range(1, n + 1):
#         if a == b:
#             graph[a][b] = 1

# 각 간선에 대한 정보를 입력 받아, 그 값으로 초기화
for _ in range(m):
    # A 에서 B로 가는 비용은 C라고 설정
    a, b = map(int, input().split())
    graph[a][b] = 1

# 점화식에 따라 플로이드 워셜 알고리즘을 수행
for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if graph[i][k] and graph[k][j]:
                graph[i][j] = 1

# 수행된 결과를 출력
for i in range(1, n + 1):
    cnt = 0
    for j in range(1, n + 1):
        if not graph[i][j] and not graph[j][i]:
            cnt += 1
    print(cnt - 1)
