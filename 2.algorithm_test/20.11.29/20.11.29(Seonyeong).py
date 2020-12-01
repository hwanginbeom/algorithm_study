## 4386번: 별자리 만들기

# 크루스칼 알고리즘

# def find_parent(parent, x):
#     # 루트 노드를 찾을 때까지 재귀 호출
#     if parent[x] != x:
#         parent[x] = find_parent(parent, parent[x])
#     return parent[x]

# 두 원소가 속한 집합을 합치기
# def union_parent(parent, a, b):
#     a = find_parent(parent, a)
#     b = find_parent(parent, b)
#     parent[b] = a
#
# n = int(input())
# parent = [0] * n
# stars = [list(map(float, input().split())) for _ in range(n)]
# cost = {} # {(별1, 별2): distance} 형태
#
#
# for i in range(n):
#     for j in range(i+1, n):
#         a = stars[i]
#         b = stars[j]
#         dist = round(((a[0]-b[0])**2 + (a[1]-b[1])**2)**0.5, 2)
#         cost[(i,j)] = dist
#
# cost = sorted(cost.items(), key=lambda x: x[1])
#
#
# answer = 0
# while cost:
#     current = cost.pop()
#     a,b = current[0]
#     cost = current[1]
#
#     if find_parent(parent, a) != find_parent(parent, b):
#         answer += cost
#         union_parent(parent, a, b)
#
# print(answer)


## 골드바흐의 추측
import math

T = int(input())

for t in range(T):
    n = int(input())

    for number1 in range(1,n+1):
        for i in range(2, int(math.sqrt(n)+1)):
            if number1 % i != 0:
                number2 = n - number1
                for t in range(2, int(math.sqrt(n)+1)):
                    if number2 % t != 0:
                        print(number1, number2, end=" ")

## 1766번: 문제집

# 위상 정렬 이용
# from collections import deque
#
# n, m = map(int, input().split())
# # 진입차수 0으로 초기화
# indegree = [0] * (n + 1)
# graph = [[] for i in range(n+1)]
#
# for _ in range(m):
#     a, b = map(int, input().split())
#     graph[a].append(b) # a에서 b로 이동
#     indegree[b] += 1
#
# def topology_sort():
#     result = []
#     q = deque()
#
#     for i in range(1, n+1):
#         if indegree[i] == 0:
#             q.append(i)
#
#     while q:
#         now = q.popleft()
#         result.append(now)
#         for i in graph[now]:
#             indegree[i] -= 1
#             q.append(i)
#         for i in result:
#             print(i, end=' ')
# topology_sort()
