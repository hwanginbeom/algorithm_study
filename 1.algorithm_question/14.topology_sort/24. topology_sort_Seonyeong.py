## 2252번: 줄 세우기

from collections import deque

n, m = map(int, input().split())
indegree = [0] * (n+1)
graph = [[] for i in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1
print(graph)
print(indegree)

def topology_sort():
    result = []
    q = deque()
    for i in range(1, m+1):
        if indegree[i] == 0:
            q.append(i)
    while q:
        now = q.popleft()
        result.append(now)

        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

        for i in result:
            print(i, end= ' ')

topology_sort()



## 3665번: 최종 순위
from collections import deque
import sys

T = int(input())

for t in range(T):
    n = int(input())
    indegree = [0] * (n+1)
    graph = [[False]*(n+1) for _ in range(n+1)]
    rank = list(map(int, input().split()))

    for i in range(n):
        for j in range(i+1, n):
            graph[rank[i]][rank[i]] = True
            indegree[rank[i]] += 1

    m = int(input())
    for i in range(m):
        a,b = map(int, input().split())
        if graph[a][b]:
            graph[a][b] = False
            graph[b][a] = True
            indegree[a] += 1
            indegree[b] -= 1
        else:
            graph[a][b] = True
            graph[b][a] = False
            indegree[a] -= 1
            indegree[b] += 1

        cycle = False
        flag = True
        result = []
        q = deque()

        for i in range(1, n+1):
            if indegree[i] == 0:
                q.append(i)

        for i in range(n):
            if len(q) == 0:
                cycle = True
                break
            if len(q) >= 2:
                flag = False
                break

            cur = q.popleft()
            result.append(cur)
            for i in range(1, n+1):
                if graph[cur][i]:
                    indegree[i] -= 1
                    if indegree[i] == 0:
                        q.append(i)

        if cycle:
            print('IMPOSSIBLE')
        elif not flag:
            print('?')
        else:
            for x in result:
                print(x, end=' ')
            print()
