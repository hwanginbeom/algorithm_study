# 1. 줄 세우기
from collections import deque


def solution1() :
    # 학생의 수(노드)와 비교한 횟수(간선) 입력
    v, e = map(int, input().split())

    # 모든 노드에 대한 진입차수는 0으로 초기화
    indegree = [0] * (v + 1)

    # 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트 초기화
    graph = [[] for _ in range(v + 1)]

    # 방향 그래프의 모든 간선 정보 입력
    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)  # 정점 A에서 B로 이동 가능

        # 진입 차수를 1 증가
        indegree[b] += 1

    # 위상 정렬 함수
    def topology_sort():
        # 알고리즘 수행 결과를 담을 리스트
        result = []

        # 큐 기능을 위한 deque 라이브러리 사용
        q = deque()

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

                # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
                if indegree[i] == 0:
                    q.append(i)

        # 위상 정렬을 수행한 결과 출력
        for i in result:
            print(i, end=' ')

    topology_sort()


# solution1()



# 2. 최종 순위
from collections import deque


def solution2() :
    t = int(input())

    for _ in range(t) :
        n = int(input())
        rank = list(map(int, input().split()))

        indegree = [0] * (n + 1)
        graph = [[False] * (n + 1) for _ in range(n + 1)]

        # 그래프 그리기
        # 순위 정보가 주어지면, 자기보다 낮은 등수를 가진 팀을 가리키도록 방향 그래프를 만든다.
        for i in range(n) :
            for j in range(i + 1, n) :
                graph[rank[i]][rank[j]] = True
                indegree[rank[j]] += 1

        m = int(input())

        # 순위를 서로 바꾸는 작업을 수행한다.
        for _ in range(m) :
            a, b = map(int, input().split())

            # 간선방향을 반대로 하는 작업 수행
            # a의 값이 b의 값보다 큰 경우
            # 작년에 a의 순위가 b보다 높았을 경우
            if graph[a][b] :
                graph[a][b] = False
                graph[b][a] = True
                indegree[a] += 1
                indegree[b] -= 1
            # b의 값이 a의 값보다 작은 경우
            # 작년에 b의 순위가 a보다 높았을 경우
            else :
                graph[a][b] = True
                graph[b][a] = False
                indegree[a] -= 1
                indegree[b] += 1

        cycle = False   # 사이클 판별
        flag = True     # 일관성 판별

        # 위상 정렬
        # 알고리즘 수행 결과를 담을 리스트
        result = []

        # 큐 기능을 위한 deque 라이브러리 사용
        q = deque()

        # 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
        for i in range(1, n + 1) :
            if indegree[i] == 0 :
                q.append(i)

        # 큐가 빌 때까지 반복
        for _ in range(n) :
            # 사이클이 있을 경우
            if len(q) == 0 :
                cycle = True
                break

            # 들어온 노드의 개수가 2개 이상일 때
            # 일관성이 없다는 것이다.
            if len(q) >= 2 :
                flag = False
                break

            now = q.popleft()
            result.append(now)

            for i in range(1, n + 1) :
                if graph[now][i] :
                    indegree[i] -= 1

                    if indegree[i] == 0 :
                        q.append(i)

        if cycle :
            print('IMPOSSIBLE')
        elif not flag :
            print('?')
        else:
            for x in result:
                print(x, end=' ')
            print()


solution2()
