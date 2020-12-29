# Strahler 순서
from collections import deque


def solution() :
    t = int(input())

    for _ in range(t) :
        k, m, p = map(int, input().split())

        # 진입차수와 strahler 순서를 같이 저장
        indegree = [[0, []] for _ in range(m + 1)]

        graph = [[] for _ in range(m + 1)]

        for _ in range(p) :
            a, b = map(int, input().split())
            graph[a].append(b)

            indegree[b][0] += 1

        # 위상 정렬 함수
        def topology_sort():
            # 알고리즘 수행 결과를 담을 리스트
            result = []

            # 큐 기능을 위한 deque 라이브러리 사용
            q = deque()

            # 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
            for i in range(1, m + 1):
                if indegree[i][0] == 0:
                    indegree[i][1].append(1)
                    q.append(i)

            # 큐가 빌 때까지 반복
            while q:
                # 큐에서 원소 꺼내기
                now = q.popleft()
                result.append(now)

                # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
                for i in graph[now]:
                    indegree[i][0] -= 1

                    # 해당 원소(now)의 strahler 순서를 추가해준다.
                    indegree[i][1].extend(indegree[now][1])

                    # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
                    if indegree[i][0] == 0:
                        # 진입차수가 0이 되었을 경우
                        # 해당 노드의 상위 노드들의 모든 strahler 순서가 저장되었기 때문에
                        # strahler 순서 계산과정 수행
                        strahler = max(indegree[i][1])

                        if indegree[i][1].count(strahler) == 1 :
                            indegree[i][1] = []
                            indegree[i][1].append(strahler)
                        else :
                            indegree[i][1] = []
                            indegree[i][1].append(strahler + 1)

                        q.append(i)

            print(k, end = ' ')
            print(indegree[result[-1]][1][0])

        topology_sort()


solution()
