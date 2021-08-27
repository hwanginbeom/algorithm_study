# 행성 터널
# https://www.acmicpc.net/problem/2887


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
    n = int(input())

    planet_dict = {}
    for i in range(n) :
        planet = list(map(int, input().split()))
        planet_dict[i] = planet

    dist_list = []

    # x, y, z 좌표로 각각 정렬을 수행하서
    # 한 행성과 가장 가까운 행성의 거리만을 구해서 Krustal 알고리즘 수행
    planet_list = sorted(planet_dict.items(), key = lambda x : x[1][0])
    for i in range(n - 1) :
        cost = abs(planet_list[i][1][0] - planet_list[i + 1][1][0])
        dist_list.append((cost, planet_list[i][0], planet_list[i + 1][0]))

    planet_list = sorted(planet_dict.items(), key=lambda x: x[1][1])
    for i in range(n - 1) :
        cost = abs(planet_list[i][1][1] - planet_list[i + 1][1][1])
        dist_list.append((cost, planet_list[i][0], planet_list[i + 1][0]))

    planet_list = sorted(planet_dict.items(), key=lambda x: x[1][2])
    for i in range(n - 1):
        cost = abs(planet_list[i][1][2] - planet_list[i + 1][1][2])
        dist_list.append((cost, planet_list[i][0], planet_list[i + 1][0]))

    dist_list.sort()
    parent = [i for i in range(n)]
    answer = 0

    for e in dist_list :
        cost, a, b = e

        if find_parent(parent, a) != find_parent(parent, b) :
            union_parent(parent, a, b)
            answer += cost

    print(answer)


solution()
