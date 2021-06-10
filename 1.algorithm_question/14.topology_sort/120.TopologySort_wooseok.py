# 장난감 조립
# https://www.acmicpc.net/problem/2637
from collections import deque


def solution() :
    n = int(input())
    m = int(input())

    graph = [[] for _ in range(n + 1)]
    indegree = [0] * (n + 1)
    index = [i for i in range(1, n + 1)]

    for _ in range(m) :
        x, y, k = map(int, input().split())

        graph[y].append((x, k))
        indegree[x] += 1

        if x in index :
            index.remove(x)

    # print(graph)
    # print(len(index))
    count_list = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

    def topology_sort():
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

            # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
            for i in graph[now]:
                indegree[i[0]] -= 1

                if now in index :
                    count_list[i[0]][now] += i[1]
                else :
                    for j in range(1, n + 1) :
                        if count_list[now][j] != 0 :
                            count_list[i[0]][j] += count_list[now][j] * i[1]

                # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
                if indegree[i[0]] == 0:
                    q.append(i[0])

    topology_sort()

    for idx, i in enumerate(count_list[-1]) :
        if i != 0 :
            print(idx, i)


solution()
