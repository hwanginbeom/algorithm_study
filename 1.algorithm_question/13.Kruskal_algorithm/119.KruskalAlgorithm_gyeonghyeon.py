import sys

input = sys.stdin.readline


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


while True:
    v, e = map(int, input().split())
    if v == 0 and e == 0:
        break
    parent = [i for i in range(v)]
    edges = []
    result = 0
    for _ in range(e):
        a, b, cost = map(int, input().split())
        edges.append((cost, a, b))
    edges.sort()
    for edge in edges:
        cost, a, b = edge
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
        else:
            result += cost
    print(result)
