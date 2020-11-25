## 9372번: 상근이의 여행

# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드를 찾을 때까지 재귀 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


T = int(input())

for t in range(T):
    n, m = map(int, input().split())
    parent = [0] * (n+1)
    cnt = 0
    # edges = []

    for i in range(1, n+1):
        parent[i] = i

    # for _ in range(m):
    #     a, b = map(int, input().split())
    #     edges.append((1,a,b))
    # for edge in edges:
    #     cost,a,b = edge
    #     if find_parent(parent, a) != find_parent(parent, b):
    #         union_parent(parent, a, b)
    #         cnt += cost

    for _ in range(m):
        a, b = map(int, input().split())
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            cnt += 1
    print(cnt)


## 1197번 최소 스패닝 트리

# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드를 찾을 때까지 재귀 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


# 노드의 개수와 간선의 개수 입력 받기
v, e = map(int, input().split())
parent = [0] * (v + 1)  # 부모 테이블 초기화

# 모든 간선을 담을 리스트와, 최종 비용을 담을 변수
edges = []
result = 0

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i

# 모든 간선에 대한 정보 입력 받기
for _ in range(e):
    a, b, c = map(int, input().split())
    # 비용순으로 정렬하기 위해서 튜플의 첫 번째 원소를 비용으로 설정
    edges.append((c, a, b))

edges.sort()

for edge in edges:
    cost, a, b = edge
    # 사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result)