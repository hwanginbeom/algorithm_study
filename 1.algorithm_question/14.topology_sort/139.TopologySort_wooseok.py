# 선수과목
# https://www.acmicpc.net/problem/14567
from collections import deque


def solution() :
    n, m = map(int, input().split())

    indegree = [0] * (n + 1)
    graph = [[] for _ in range(n + 1)]
    for _ in range(m) :
        a, b = map(int, input().split())
        graph[a].append(b)

        indegree[b] += 1

    # 위상 정렬 함수
    def topology_sort():
        # 알고리즘 수행 결과를 담을 딕셔너리
        result_dict = {}
        semester = 1

        for i in range(1, n + 1) :
            result_dict[i] = 0

        # 큐 기능을 위한 deque 라이브러리 사용
        q = deque()

        # 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
        for i in range(1, n + 1):
            if indegree[i] == 0:
                q.append([i, semester]) # 직전 과목의 학기를 알기 위해 함께 저장
                result_dict[i] = semester

        # 큐가 빌 때까지 반복
        while q:
            # 큐에서 원소 꺼내기
            now, s = q.popleft()
            s += 1

            # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
            for i in graph[now]:
                indegree[i] -= 1

                # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
                if indegree[i] == 0:
                    q.append([i, s])
                    result_dict[i] = s

        # 위상 정렬을 수행한 결과 출력
        for i in result_dict.values():
            print(i, end = ' ')

    topology_sort()


solution()
