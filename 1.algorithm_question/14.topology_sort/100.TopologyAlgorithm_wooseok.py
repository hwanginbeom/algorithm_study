# 문제집
# https://www.acmicpc.net/problem/1766
import heapq


def solution3() :
    n, m = map(int, input().split())

    # 각 노드의 진입차수
    indegree = [0] * (n + 1)

    graph = [[] for _ in range(n + 1)]

    for _ in range(m) :
        a, b = map(int, input().split())

        graph[a].append(b)
        indegree[b] += 1

    # print('graph :', graph)

    # 위상 정렬 함수
    def topology_sort():
        # 알고리즘 수행 결과를 담을 리스트
        result = []

        # 우선순위 큐 사용
        q = []

        # 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
        for i in range(1, n + 1):
            if indegree[i] == 0:
                heapq.heappush(q, i)

        # 큐가 빌 때까지 반복
        while q:

            # print('queue :', q)

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


solution3()
