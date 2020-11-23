# 1. 집합의 표현
# 특정 원소가 속한 집합을 찾기
def find_parent1(parent, x) :
    # 루트 노드를 찾을 때까지 재귀 호출
    if parent[x] == x :
        return x

    parent[x] = find_parent1(parent, parent[x])
    return parent[x]


# 두 원소가 속한 집합을 합치기
def union_parent1(parent, a, b) :
    a = find_parent1(parent, a)
    b = find_parent1(parent, b)

    if a < b:
        parent[b] = a
    else :
        parent[a] = b


def solution1() :
    n, m = map(int, input().split())

    # 부모 테이블 초기화
    parent = [0] * (n + 1)

    # 부모 테이블상에서 부모를 자기 자신으로 초기화
    for i in range(n + 1):
        parent[i] = i

    for _ in range(m) :
        op, a, b = map(int, input().split())

        if op == 0 :
            union_parent1(parent, a, b)
        else :
            if find_parent1(parent, a) == find_parent1(parent, b) :
                print('YES')
            else :
                print('NO')


# solution1()



# 2. 여행 가자
# 특정 원소가 속한 집합을 찾기
def find_parent2(parent, x) :
    # 루트 노드를 찾을 때까지 재귀 호출
    if parent[x] == x:
        return x

    parent[x] = find_parent2(parent, parent[x])
    return parent[x]


# 두 원소가 속한 집합을 합치기
def union_parent2(parent, a, b) :
    a = find_parent2(parent, a)
    b = find_parent2(parent, b)

    if a < b :
        parent[b] = a
    else :
        parent[a] = b


def solution2() :
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
                union_parent2(parent, i + 1, j + 1)

    for i in range(m - 1) :
        if find_parent2(parent, d[i]) != find_parent2(parent, d[i + 1]):
            print('NO')
            break
    else :
        print('YES')


solution2()
