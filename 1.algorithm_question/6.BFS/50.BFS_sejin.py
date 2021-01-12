n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
for _ in range(m) :
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

visited = [False] * 9

from collections import deque

# BFS 메서드 정의
def bfs(graph, start, visited):
    # 큐 구현을 위해 deque 라이브러리 사용
    queue = deque([start])

    visited[start] = True
    count = 0

    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력하기
        v = queue.popleft()
        count += 1

        # 아직 방문하지 않은 인접한 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
    return count-1

print(bfs(graph, 1, visited))