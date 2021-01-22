# 별자리 만들기
import math


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

    star_list = []
    for _ in range(n) :
        star_list.append(list(map(float, input().split())))

    parent = [0] * (n + 1)

    # 부모 테이블상에서 부모를 자기 자신으로 초기화
    for i in range(1, n + 1):
        parent[i] = i

    edges = []
    result = 0

    # 별자리 좌표를 인덱스로 생각하여 이용
    for i in range(n) :
        for j in range(i + 1, n) :
            distance = math.sqrt((star_list[j][0] - star_list[i][0]) ** 2 + (star_list[j][1] - star_list[i][1]) ** 2)
            edges.append((distance, i + 1, j + 1))

    edges.sort()

    # 간선을 하나씩 확인
    for edge in edges:
        cost, a, b = edge

        # 사이클이 발생하지 않는 경우에만 집합에 포함
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            result += cost

    print(result)


solution()
