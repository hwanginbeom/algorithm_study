# Kruskal Algorithm
# 도시 분할 계획
# https://www.acmicpc.net/problem/1647

# Solution
# 크루스칼 알고리즘 구현 후 연결된 경로 중 가장 큰 비용인 간선을 제거하면
# 최소 비용으로 두 개로 분할된 마을을 만들 수 있다.

# 특정 원소가 속한 집합을 찾기
def find_parent(x):
    # 루트 노드를 찾을 때까지 재귀 호출
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)
    parent[a] = b


# 노드의 개수와 간선(Union 연산)의 개수 입력 받기
n, m = map(int, input().split())
parent = [0] * (n + 1)  # 부모 테이블 초기화하기

# 모든 간선을 담을 리스트와 최종 비용을 담을 변수
edges = []
result = 0

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, n + 1):
    parent[i] = i

# 두 점을 입력받아 리스트 안의 리스트로 구성
for _ in range(m):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

# 간선을 비용 순으로 정렬
edges.sort()

# 선택된 간선 중 비용이 가장 큰 것을 선택하기 위한 초기값 설정
max_cost = 0
# 간선을 하나씩 확인하며
for edge in edges:
    cost, a, b = edge
    # 사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parent(a) != find_parent(b):
        union_parent(a, b)
        result += cost
        # 선택된 간선 중 비용이 가장 큰 것을 선택
        max_cost = max(max_cost, cost)

print(result - max_cost)