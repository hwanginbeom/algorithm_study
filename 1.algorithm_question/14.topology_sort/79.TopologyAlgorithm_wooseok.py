# 음악프로그램
from collections import deque


def solution() :
    n, m = map(int, input().split())

    graph = [[] for _ in range(n + 1)]
    indegree = [0] * (n + 1)

    # 그래프 만들기
    for _ in range(m) :
        _list = list(map(int, input().split()))

        for i in range(1, len(_list) - 1) :
            if _list[i + 1] not in graph[_list[i]] :
                graph[_list[i]].append(_list[i + 1])
                indegree[_list[i + 1]] += 1

    # 위상 정렬 함수
    def topology_sort():
        # 알고리즘 수행 결과를 담을 리스트
        result = []

        # 큐 기능을 위한 deque 라이브러리 사용
        q = deque()

        # 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
        for i in range(1, n + 1):
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

                # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
                if indegree[i] == 0:
                    q.append(i)

        return result

    answer = topology_sort()

    if len(answer) == n :
        for i in answer :
            print(i)
    else :
        print(0)


solution()
