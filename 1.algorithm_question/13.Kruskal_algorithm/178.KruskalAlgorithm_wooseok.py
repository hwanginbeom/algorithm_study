# 행성 연결
# https://www.acmicpc.net/problem/16398


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
    n = int(input())

    parent = [i for i in range(n + 1)]
    edges = []
    result = 0
    row_num = 1

    for _ in range(n) :
        planet_list = list(map(int, input().split()))
        zeroFlag = False

        for i in range(n) :
            if planet_list[i] == 0 :
                zeroFlag = True
                continue

            if zeroFlag :
                edges.append((planet_list[i], row_num, i + 1))

        row_num += 1

    edges.sort()

    # 간선을 하나씩 확인
    for edge in edges:
        cost, a, b = edge

        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            result += cost

    print(result)


solution()
