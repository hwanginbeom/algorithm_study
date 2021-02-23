# 정복자
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def solution() :
    n, m, t = map(int, input().split())

    edges = []
    for _ in range(m) :
        a, b, cost = map(int, input().split())

        edges.append((cost, a, b))

    edges.sort()

    parent = [i for i in range(n + 1)]
    cost_list = []

    for edge in edges :
        cost, a, b = edge

        if find_parent(parent, a) != find_parent(parent, b) :
            union_parent(parent, a, b)
            cost_list.append(cost)

    answer = 0
    for i in range(len(cost_list)) :
        answer += cost_list[i] + (t * i)

    print(answer)


solution()
