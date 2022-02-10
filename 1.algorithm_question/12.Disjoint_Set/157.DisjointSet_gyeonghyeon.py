import sys

inpyt = sys.stdin.readline


def find_parent(parent, x):
    if parent[x] == x:
        return x
    parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a != b:
        parent[b] = a


def solution():
    n = int(input())
    m = int(input())

    parent = {i: i for i in range(n + 1)}

    for i in range(1, n + 1):
        maps = list(map(int, input().split()))
        for j in range(1, len(maps) + 1):
            if maps[j - 1] == 1:
                union_parent(parent, i, j)
    tour = list(map(int, input().split()))
    result = set([find_parent(parent, i) for i in tour])

    if len(result) != 1:
        print("NO")
    else:
        print("YES")

solution()