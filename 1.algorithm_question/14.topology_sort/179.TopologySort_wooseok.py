# 작업
# https://www.acmicpc.net/problem/2056
from collections import deque


def topology_sort(n, graph, indegree, time_dict):
    result = {}
    order_list = [[] for _ in range(n + 1)]
    q = deque()

    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append({i: time_dict[i]})

    while q:
        _dict = q.popleft()
        now = list(_dict.keys())[0]
        add_time = _dict[now]

        result[now] = add_time

        for i in graph[now]:
            indegree[i] -= 1
            order_list[i].append(now)

            # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
            if indegree[i] == 0:
                max_value = 0

                # 현재 작업의 선행 작업들 중에서 가장 시간이 오래걸린 작업 찾기
                for j in order_list[i] :
                    max_value = max(max_value, result[j])

                q.append({i: max_value + time_dict[i]})

    return result


def solution() :
    n = int(input())

    graph = [[] for _ in range(n + 1)]
    indegree = [0] * (n + 1)
    time_dict = {}

    for i in range(n) :
        job_list = list(map(int, input().split()))
        time_dict[i + 1] = job_list[0]

        if job_list[1] > 0 :
            for j in range(2, len(job_list)) :
                graph[job_list[j]].append(i + 1)
                indegree[i + 1] += 1

    result = topology_sort(n, graph, indegree, time_dict)
    print(max(list(result.values())))


solution()
