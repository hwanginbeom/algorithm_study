# 도시 분할 계획
# https://www.acmicpc.net/problem/1647


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
    n, m = map(int, input().split())

    edges = []
    for _ in range(m) :
        a, b, c = map(int, input().split())
        edges.append((c, a, b))

    edges.sort()

    parent = [i for i in range(n + 1)]
    result = 0
    cost_list = []

    for edge in edges:
        cost, a, b = edge

        # 사이클이 발생하지 않는 경우에만 집합에 포함
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            result += cost
            cost_list.append(cost)

    print(result - max(cost_list))


solution()
