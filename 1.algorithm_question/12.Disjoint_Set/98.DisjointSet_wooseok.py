# 여행 가자
# https://www.acmicpc.net/problem/1976


# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x) :
    # 루트 노드를 찾을 때까지 재귀 호출
    if parent[x] == x:
        return x

    parent[x] = find_parent(parent, parent[x])
    return parent[x]


# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b) :
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b :
        parent[b] = a
    else :
        parent[a] = b


def solution() :
    n = int(input())
    m = int(input())

    graph = []
    for _ in range(n) :
        graph.append(list(map(int, input().split())))

    d = list(map(int, input().split()))

    parent = [i for i in range(n + 1)]

    for i in range(len(graph)) :
        for j in range(len(graph[i])) :
            if graph[i][j] == 1 :
                union_parent(parent, i + 1, j + 1)

    for i in range(m - 1) :
        if find_parent(parent, d[i]) != find_parent(parent, d[i + 1]):
            print('NO')
            break
    else :
        print('YES')


solution()
