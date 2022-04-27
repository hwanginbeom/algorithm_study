#백준 16398

#행성노드를 최소 플로우 비용으로 연결하고 최소 신장트리를 만들기!
#크루스칼 알고리즘
#1. 입력받은 행렬에서 플로우비용을 뽑아 정렬
#2. 최소 비용의 플로우부터 사이클 발생 여부를 판별 > 사이클 돌면 패스 안돌면 연결시키고 집합에 포함


import sys
input=sys.stdin.readline

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n = int(input())
parent = [i for i in range(n)]
graph = [list(map(int, input().split())) for _ in range(n)]
edges = []

for a in range(n):
    for b in range(a + 1, n):
        edges.append((graph[a][b], a, b))

edges.sort()

result = 0

for edge in edges:
    cost, a, b = edge

    if find_parent(a) != find_parent(b):
        union_parent(a, b)
        result += cost

print(result)