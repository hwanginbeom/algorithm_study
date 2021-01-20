# 노드 : 회사, 간선 : 도로
# 노드의 개수 및 간선의 개수 입력받기
n, m = map(int, input().split())
# 2차원 리스트 만들고 무한으로 초기화
graph = [[0] * (n+1) for _ in range(n+1)]

# 각 간선에 대한 정보를 입력 받아 그 값을 초기화
for _ in range(m) :
# a에서 b로 가는 비용은 c라고 설정
    a, b = map(int, input().split())
    graph[a][b] = 1

# 점화식에 따라 플로이드 워셜 알고리즘 수행
for k in range(1, n+1) :
    for a in range(1, n+1) :
        for b in range(1, n+1) :
            if graph[a][k] + graph[k][b] == 2 :
                graph[a][b] =1

answer = [0] * (n+1)
for i in range(1, n+1) :
    for j in range(1, n+1) :
        if graph[i][j] == 1:
            answer[i] += 1
            answer[j] += 1

print(answer.count(n-1))