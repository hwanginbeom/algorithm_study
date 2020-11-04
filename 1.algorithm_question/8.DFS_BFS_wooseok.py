from collections import deque


# BFS 메소드 정의
def bfs(graph, start, visited):
    global kevin_bacon
    global kevin_bacon_a

    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque([start])

    # 현재 노드를 방문 처리
    visited[start] = True

    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력하기
        v = queue.popleft()

        # 아직 방문하지 않은 인접한 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                kevin_bacon += 1

                kevin_bacon_a[i] = kevin_bacon

                queue.append(i)
                visited[i] = True

            kevin_bacon -= 1

        kevin_bacon += 1


n, m = map(int, input().split())

connection = [[] for i in range(n + 1)]
visited = [False] * (n + 1)

kevin_bacon = 0
kevin_bacon_a = [0] * (n + 1)
kevin_bacon_sum = []

for i in range(m) :
    a, b = map(int, input().split())

    if b not in connection[a] :
        connection[a].append(b)
        connection[b].append(a)

print(connection)

for i in range(1, n + 1) :
    kevin_bacon = 0
    kevin_bacon_a = [0] * (n + 1)
    visited = [False] * (n + 1)

    bfs(connection, i, visited)

    print(kevin_bacon_a)
    kevin_bacon_sum.append(sum(kevin_bacon_a))

print(kevin_bacon_sum)

