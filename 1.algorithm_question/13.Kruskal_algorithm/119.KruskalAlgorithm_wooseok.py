# 전력난
# https://www.acmicpc.net/problem/6497


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
    while True :
        m, n = map(int, input().split())

        if m == 0 and n == 0 :
            break

        parent = [0] * (m + 1)
        for i in range(1, m + 1) :
            parent[i] = i

        edges = []
        result = 0
        _sum = 0

        for _ in range(n) :
            x, y, z = map(int, input().split())
            edges.append((z, x, y))
            _sum += z

        edges.sort()

        for edge in edges :
            cost, x, y = edge

            if find_parent(parent, x) != find_parent(parent, y):
                union_parent(parent, x, y)
                result += cost

        print(_sum - result)


solution()
