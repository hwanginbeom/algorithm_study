def dfs(graph, v, visited) :
    # 현재 노드를 방문처리
    visited[v] = True

    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v] :
        if not visited[i] :
            dfs(graph, i, visited)


# 전체 컴퓨터의 개수
n = int(input())

# 연결되어있는 컴퓨터 쌍의 개수
connect_cnt = int(input())

graph = [[] for i in range(n + 1)]

# 이중리스트로 연결상태 표현
for i in range(connect_cnt) :
    connect = input()
    n1 = int(connect.split()[0])
    n2 = int(connect.split()[1])

    graph[n1].append(n2)
    graph[n2].append(n1)

# 해당 노드를 방문했는지 안했는지 체크하는 리스트 생성
visited = [False] * (n + 1)

dfs(graph, 1, visited)

# 0번 인덱스는 쓰이지 않으므로 1을 뺀다.
print(visited.count(True) - 1)
