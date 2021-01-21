# 8. 기타 그래프 이론
# 크루스칼 알고리즘 (최소 간선 트리 알고리즘)
# 별자리 만들기
# https://www.acmicpc.net/problem/4386

# 별들이 2차원 평면 위에 놓여 있다.
# 선을 하나 이을 때마다 두 별 사이의 거리만큼의 비용이 든다고 할 때,
# 별자리를 만드는 최소 비용을 구하시오.

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

# 두 점 사이의 거리 계산
def distance(a, b):
    return (((a[0] - b[0]) ** 2) + ((a[1] - b[1]) ** 2)) ** 0.5


# 노드의 개수와 간선(Union 연산)의 개수 입력 받기
n = int(input())
parent = [0] * (n + 1)  # 부모 테이블 초기화하기

# 모든 간선을 담을 리스트와 최종 비용을 담을 변수
edges = []
result = 0

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, n + 1):
    parent[i] = i

# 두 점을 입력받아 리스트 안의 리스트로 구성
point = []
for i in range(n):
    x, y = map(float, input().split())
    point.append([x, y])

# 두 점 사이의 거리를 계산하고 입력 받는 순서대로 노드 번호를 매겨 튜플 형태로 설정
for i in range(n):
    for j in range(n):
        cost = distance(point[i], point[j])
        edges.append((cost, i, j))

# 간선을 비용 순으로 정렬
edges.sort()

# 간선을 하나씩 확인하며
for edge in edges:
    cost, a, b = edge
    # 사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print('%0.2f'%result)
