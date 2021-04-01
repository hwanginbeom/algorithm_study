import heapq

n, m = map(int, input().split()) # n:문제의수, m:정보의수
# 모든 노드에 대한 진입차수는 0으로 초기화
indegree = [0] * (n + 1)
# 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트 초기화
graph = [[] for i in range(n + 1)]

# 방향 그래프의 모든 간선 정보를 입력 받기
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b) # a번 문제는 b번 문제보다 먼저 푸는 것이 좋다
    # 진입 차수를 1 증가
    indegree[b] += 1


# 위상 정렬 함수
def topology_sort():
    result = [] # 알고리즘 수행 결과를 담을 리스트
    q = []

    for i in range(1, n + 1):
        if indegree[i] == 0: #먼저 해야하는 얘들이 q에 들어간다
            heapq.heappush(q, i)

    # 큐가 빌 때까지 반복
    while q:
        # 큐에서 원소 꺼내기
        now = heapq.heappop(q)
        result.append(now)
        # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
        for i in graph[now]:
            indegree[i] -= 1
            # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
            if indegree[i] == 0:
                heapq.heappush(q, i)

    # 위상 정렬을 수행한 결과 출력
    for i in result:
        print(i, end=' ')

topology_sort()
