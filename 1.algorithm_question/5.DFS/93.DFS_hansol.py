# DFS
# 연결 요소의 개수
# https://www.acmicpc.net/problem/11724

# N, M 값 입력
N, M = map(int, input().split())
# graph[a][b] 이면 a와 b가 연결되어 있다는 정보를 표시하기 위한 리스트 안의 리스트
graph = [[0] * (N + 1) for _ in range(N + 1)]
# 방문처리를 위한 리스트
visited = [False] * (N + 1)

# 간선 양 끝점 입력
for _ in range(M):
    u, v = map(int, input().split())
    # 연결처리
    graph[u][v] = 1
    graph[v][u] = 1

# DFS 정의
def dfs(x):
    # 현재 노드를 방문 처리
    visited[x] = True
    # 방문하지 않고 연결은 되어있는 노드에 재귀적으로 방문
    for i in range(1, N + 1):
        if not visited[i] and graph[x][i] == 1:
            dfs(i)


count = 0
# 방문하지 않았다면 dfs 를 적용해 연결된 모든 노드를 방문처리하고 count 를 + 1
for i in range(1, N + 1):
    if not visited[i]:
        dfs(i)
        count += 1

print(count)