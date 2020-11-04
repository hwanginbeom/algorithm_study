from collections import deque


# BFS 메소드 정의
def bfs(graph, start, visited) :
    global kevin_bacon_a

    queue = deque()

    # 큐에 리스트를 삽입
    # 첫번째 원소 : 노드 번호
    # 두번째 원소 : 시작 노드에서 현재 노드까지의 최단 거리
    queue.append([start, 0])

    # 현재 노드를 방문 처리
    visited[start] = True

    # 큐가 빌 때까지 반복
    while queue :
        # 큐에서 맨 앞의 원소(리스트) 추출
        v = queue.popleft()

        # 아직 방문하지 않은 인접한 원소들을 큐에 삽입
        for i in graph[v[0]] :
            if not visited[i] :
                # 이전 노드의 최단 거리에 1을 더하고
                # 현재 노드 번호와 더한 값을 리스트로 큐에 삽입
                kevin_bacon = v[1] + 1
                queue.append([i, kevin_bacon])

                # 나중에 최단 거리를 모두 더하기 위한 저장 리스트
                kevin_bacon_a[i] = kevin_bacon

                # 방문 처리
                visited[i] = True

                # print('i = {}, kevin_bacon = {}'.format(i, kevin_bacon))


# 사람의 수, 친구 관계의 수 입력
n, m = map(int, input().split())

# 관계를 표현할 이중리스트 생성
connection = [[] for i in range(n + 1)]

# 방문 처리를 위한 리스트 생성
visited = [False] * (n + 1)

# 한 사람의 다른 모든 사람에 대한 케빈 베이컨의 수를 저장할 리스트
kevin_bacon_a = [0] * (n + 1)

# 한 사람의 케빈 베이컨의 수를 모두 더하여 저장할 리스트
kevin_bacon_sum = []

# 관계 그래프 생성
for i in range(m) :
    a, b = map(int, input().split())

    if b not in connection[a] :
        connection[a].append(b)
        connection[b].append(a)

# print(connection)

for i in range(1, n + 1) :
    # 사람이 바뀔 때 마다 초기화한다.
    kevin_bacon_a = [0] * (n + 1)
    visited = [False] * (n + 1)

    bfs(connection, i, visited)

    # print(kevin_bacon_a)
    kevin_bacon_sum.append(sum(kevin_bacon_a))

mini = min(kevin_bacon_sum)
answer = kevin_bacon_sum.index(mini) + 1  # 리스트에서 원하는 요소의 인덱스를 찾는 함수

print(answer)
