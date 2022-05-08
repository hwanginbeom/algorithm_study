import sys

input = sys.stdin.readline


def find_parent(parent, x):
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def solution():
    n = int(input())
    parent = [i for i in range(n)]
    graph = [list(map(int, input().split())) for _ in range(n)]
    edges = []

    for a in range(n):
        for b in range(a + 1, n):
            edges.append((graph[a][b], a, b))
    edges.sort()
    answer = 0
    for cost, a, b in edges:
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            answer += cost
    return answer


print(solution())
