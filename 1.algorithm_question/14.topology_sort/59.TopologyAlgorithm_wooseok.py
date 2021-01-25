# 게임 개발
from collections import deque


def solution() :
    n = int(input())

    build_list = []
    for _ in range(n) :
        build_list.append(list(map(int, input().split())))

    # 모든 노드에 대한 진입차수는 0으로 초기화
    indegree = [0] * (n + 1)

    # 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트 초기화
    graph = [[] for _ in range(n + 1)]

    # 빌드 순서를 그래프로 나타내고 진입차수 설정
    for i in range(len(build_list)) :
        for j in range(1, len(build_list[i])) :
            if build_list[i][j] == -1 :
                break

            graph[build_list[i][j]].append(i + 1)
            indegree[i + 1] += 1

    # 위상 정렬 함수
    def topology_sort():
        # 알고리즘 수행 결과를 담을 리스트
        result = [0] * (n + 1)

        # 큐 기능을 위한 deque 라이브러리 사용
        q = deque()

        # 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
        for i in range(1, n + 1):
            if indegree[i] == 0:
                q.append(i)
                result[i] = build_list[i - 1][0]

        # 큐가 빌 때까지 반복
        while q:
            # 큐에서 원소 꺼내기
            now = q.popleft()

            # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
            for i in graph[now]:
                indegree[i] -= 1

                # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
                if indegree[i] == 0:
                    q.append(i)

                    # 현재 노드(i)에 진입하는 노드들 중
                    # 가장 시간이 오래 걸리는 노드 찾기

                    # 여러 개의 건물을 동시에 지을 수 있으므로
                    # 가장 오래걸리는 빌드 이후에 현재 노드가 지어질 수 있다.
                    maximum = 0
                    for j in range(1, len(build_list[i - 1]) - 1) :
                        if maximum < result[build_list[i - 1][j]] :
                            maximum = result[build_list[i - 1][j]]

                    result[i] = maximum + build_list[i - 1][0]

        return result

    result = topology_sort()

    for i in range(1, len(result)) :
        print(result[i])


solution()
