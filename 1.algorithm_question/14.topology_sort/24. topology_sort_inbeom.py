# 2252 - 줄세우기
from collections import deque

# 노드의 개수와 간선의 개수를 입력받기
v, e = map(int, input().split())

# 모든 노드에 대한 집입차수는 0으로 초기화
indegree = [0] * (v + 1)

# 각 노드에 연결된 간선 정보를 담기위한 연결 리스트 초기화
graph = [[] for i in range(v + 1)]

# 방향 그래프의 모든 간선 정보를 입력 받기
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)  # 정점 A에서 B로 이동 가능

    # 진입 차수를 1증가
    indegree[b] += 1


# 위상정렬함수
def topology_sort():
    result = []  # 알고리즘 수행 결과를 담을 리스트
    q = deque()  # 큐 기능을 위한 deque 라이브러리 사용
    # 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입

    for i in range(1, v + 1):
        if indegree[i] == 0:
            q.append(i)
    # 큐가 빌 때까지 반복
    while q:
        # 큐에서 원소 꺼내기
        now = q.popleft()
        result.append(now)

        # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
    for i in result:
        print(i, end=' ')
topology_sort()


from collections import deque
import sys

input = sys.stdin.readline


def topologicalSort():
    global isImpossible, isAmbiguous

    for _ in range(n):
        if not dq:
            isImpossible = True
            return
        if len(dq) > 1:
            isAmbiguous = True
            return

        target = dq.popleft()
        sequence.append(target)

        for x in adjList[target]:
            indegree[x] -= 1

            if not indegree[x]:
                dq.append(x)


T = int(input())

for _ in range(T):
    n = int(input())

    isImpossible = False
    isAmbiguous = False
    sequence = []
    indegree = [0] * (n + 1)
    adjList = [[] for _ in range(n + 1)]

    lastYear = list(map(int, input().split()))

    for i in range(0, n):
        for j in range(i + 1, n):
            indegree[lastYear[j]] += 1
            adjList[lastYear[i]].append(lastYear[j])

    m = int(input())
    for _ in range(m):
        a, b = map(int, input().split())

        isNotFound = True

        for x in adjList[a]:
            if x == b:
                isNotFound = False
                indegree[b] -= 1
                indegree[a] += 1
                adjList[a].remove(b)
                adjList[b].append(a)

        if isNotFound:
            indegree[a] -= 1
            indegree[b] += 1
            adjList[b].remove(a)
            adjList[a].append(b)

    dq = deque()
    for i in range(1, n + 1):
        if not indegree[i]:
            dq.append(i)

    topologicalSort()

    if isImpossible:
        print("IMPOSSIBLE")
    elif isAmbiguous:
        print("?")
    else:
        print(*sequence)