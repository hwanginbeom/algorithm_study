# 1. 상근이의 여행
# 특정 원소가 속한 집합을 찾기
def find_parent1(parent, x):
    # 루트 노드를 찾을 때까지 재귀 호출
    if parent[x] != x:
        parent[x] = find_parent1(parent, parent[x])
    return parent[x]


# 두 원소가 속한 집합을 합치기
def union_parent1(parent, a, b):
    a = find_parent1(parent, a)
    b = find_parent1(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def solution1() :
    t = int(input())

    for _ in range(t) :
        n, m = map(int, input().split())
        edges = []
        result = 0

        for _ in range(m) :
            a, b = map(int, input().split())
            edges.append([a, b])

        parent = [i for i in range(n + 1)]

        for edge in edges :
            a, b = edge

            # 부모 노드가 같지 않다면 서로 다른 집합에 있는것으로
            # 연결을 해주어도 사이클이 발생하지 않는다.
            if find_parent1(parent, a) != find_parent1(parent, b) :
                union_parent1(parent, a, b)
                result += 1

        print(result)


# solution1()



# 2. 최소 스패닝 트리
# 특정 원소가 속한 집합을 찾기
def find_parent2(parent, x):
    # 루트 노드를 찾을 때까지 재귀 호출
    if parent[x] != x:
        parent[x] = find_parent2(parent, parent[x])
    return parent[x]


# 두 원소가 속한 집합을 합치기
def union_parent2(parent, a, b):
    a = find_parent2(parent, a)
    b = find_parent2(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def solution2() :
    v, e = map(int, input().split())
    edges = []
    result = 0

    for _ in range(e) :
        a, b, c = map(int, input().split())
        edges.append((c, a, b))

    edges.sort()

    parent = [i for i in range(v + 1)]

    for edge in edges :
        c, a, b = edge

        if find_parent2(parent, a) != find_parent2(parent, b) :
            union_parent2(parent, a, b)
            result += c

    print(result)


solution2()
