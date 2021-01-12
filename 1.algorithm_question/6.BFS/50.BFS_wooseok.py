# 바이러스
from collections import deque


# BFS 메소드 정의
def bfs(graph, start, visited):
    count = 0

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
                queue.append(i)
                visited[i] = True

                count += 1

    return count


n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]
for _ in range(m) :
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 각 노드가 방문된 정보를 표현 (1차원 리스트)
visited = [False] * (n + 1)

# 정의된 BFS 함수 호출
answer = bfs(graph, 1, visited)
print(answer)
