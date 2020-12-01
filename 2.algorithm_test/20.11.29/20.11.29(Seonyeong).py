## 4386번: 별자리 만들기

# 크루스칼 알고리즘

# def find_parent(parent, x):
#     # 루트 노드를 찾을 때까지 재귀 호출
#     if parent[x] != x:
#         return find_parent(parent, parent[x])
#     return x
#
# # 두 원소가 속한 집합을 합치기
# def union_parent(parent, a, b):
#     root_a = find_parent(parent, a)
#     root_b = find_parent(parent, b)
#     parent[root_b] = root_a
#
# n = int(input())
# parent = [_ for _ in range(n)]
# stars = [list(map(float, input().split())) for _ in range(n)]
# costs = {} # {(별1, 별2): distance} 형태
#
#
# for i in range(n):
#     for j in range(i+1, n):
#         a = stars[i]
#         b = stars[j]
#         dist = round(((a[0]-b[0])**2 + (a[1]-b[1])**2)**0.5, 2)
#         costs[(i, j)] = dist
#
# costs = sorted(costs.items(), key=lambda x: x[1])
# print(costs)
# print(type(costs))
#
# answer = 0
# while costs:
#     current = costs.pop(0)
#     print(current)
#     print(current[0])
#     a, b = current[0]
#     cost = current[1]
#
#     if find_parent(parent, a) != find_parent(parent, b):
#         answer += cost
#         union_parent(parent, a, b)
#
# print(answer)




# ## 골드바흐의 추측
# import math
#
# T = int(input())
#
# for t in range(T):
#     n = int(input())
#
#     for number1 in range(1,n+1):
#         for i in range(2, int(math.sqrt(n)+1)):
#             if number1 % i != 0:
#                 number2 = n - number1
#                 for t in range(2, int(math.sqrt(n)+1)):
#                     if number2 % t != 0:
#                         print(number1, number2, end=" ")
#


## 1766번: 문제집


# import heapq
#
#
# def solution3() :
#     n, m = map(int, input().split())
#
#     # 각 노드의 진입차수
#     indegree = [0] * (n + 1)
#
#     graph = [[] for _ in range(n + 1)]
#
#     for _ in range(m) :
#         a, b = map(int, input().split())
#
#         graph[a].append(b)
#         indegree[b] += 1
#
#     print('graph :', graph)
#     print('indegree :', indegree)
#
#     # 위상 정렬 함수
#     def topology_sort():
#         # 알고리즘 수행 결과를 담을 리스트
#         result = []
#
#         # 우선순위 큐 사용
#         q = []
#
#         # 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
#         for i in range(1, n + 1):
#             if indegree[i] == 0:
#                 heapq.heappush(q, i)
#         print('queue :', q)
#
#         # 큐가 빌 때까지 반복
#         while q:
#
#             print('queue :', q)
#
#             # 큐에서 원소 꺼내기
#             now = heapq.heappop(q)
#             print('queue :', q)
#
#             result.append(now)
#
#             # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
#             for i in graph[now]:
#                 indegree[i] -= 1
#
#                 # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
#                 if indegree[i] == 0:
#                     heapq.heappush(q, i)
#
#         # 위상 정렬을 수행한 결과 출력
#         for i in result:
#             print(i, end=' ')
#
#     topology_sort()
#
#
# solution3()
