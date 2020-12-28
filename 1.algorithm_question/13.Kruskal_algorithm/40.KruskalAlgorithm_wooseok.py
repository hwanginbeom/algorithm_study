# 네트워크 연결
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


def solution() :
    n = int(input())
    m = int(input())
    parent = [0] * (n + 1)

    # 모든 노드에 대하여 부모 노드를 자기 자신으로 초기화
    for i in range(1, n + 1) :
        parent[i] = i

    edges = []
    cost = 0

    for _ in range(m) :
        a, b, c = map(int, input().split())
        edges.append((c, a, b))

    # 비용순으로 오름차순 정렬
    edges.sort()

    for edge in edges :
        c, a, b = edge

        # 두 노드의 부모가 다르다면
        # 아직 추가되지 않은 간선이므로 부모를 합친다.
        if find_parent(parent, a) != find_parent(parent, b) :
            union_parent(parent, a, b)
            cost += c

    print(cost)


solution()
