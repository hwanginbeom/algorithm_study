#11404
n = int(input())
m = int(input())
inf = 100000000
s = [[inf] * n for i in range(n)]

for i in range(m):
    a, b, c = map(int,input().split())
    if s[a-1][b-1] > c:
        s[a-1][b-1] = c
for k in range(n):
    for i in range(n):
        for j in range(n):
            if i != j and s[i][j] > s[i][k] + s[k][j]:
                s[i][j] = s[i][k] + s[k][j]
for i in s:
    for j in i:
        if j == inf:
            print(0, end='')
        else:
            print(j, end='')
    print()


# 1956
import sys
#n은 마을 m은 도로
n,m = map(int,sys.stdin.readline().split())
inf = 100000000
s = [[inf] * n for i in range(m)]
for i in range(m):
    a, b, c = map(int,sys.stdin.readline().split())
    s[a-1][b-1] = c
for k in range(n):
    for i in range(n):
        for j in range(n):
            if s[i][j] > s[i][k] + s[k][j]:
                s[i][j] = s[i][k] + s[k][j]
result = inf
for i in range(n):
    result = min(result, s[i][i])
if result == inf:
    print(-1)
else:
    print(result)



# INF = int(1e9)  # 무한을 의미하는 값으로 10억을 설정
#
# # 노드의 개수 및 간선의 개수를 입력 받기
#
# n = int(input())
# m = int(input())
#
# # 2차원 리스트(그래프 표현)를 만들고, 무한 으로 초기화
# graph = [[INF] * (n + 1) for _ in range(n + 1)]
#
# # 자기 자신에서 자기 자신으로 가는 비용은 0 으로 초기화
# for a in range(1, n + 1):
#     for b in range(1, n + 1):
#         if a == b:
#             graph[a][b] = 0
#
# # 각 간선에 대한 정보를 입력 받아, 그 값으로 초기화
# for _ in range(m):
#     # A 에서 B로 가는 비용은 C라고 설정
#     a, b, c = map(int, input().split())
#     graph[a][b] = c
#
# # 점화식에 따라 플로이드 워셜 알고리즘을 수행
# for k in range(1, n + 1):
#     for a in range(1, n + 1):
#         for b in range(1, n + 1):
#             graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])
#
# # 수행된 결과를 출력
# for a in range(1, n + 1):
#     for b in range(1, n + 1):
#         if graph[a][b] == INF:
#             print("INFINITY", end=" ")
#         else:
#             print(graph[a][b], end=" ")
#     print()