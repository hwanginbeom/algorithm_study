# 여러분의 다리가 되어 드리겠습니다!
# https://www.acmicpc.net/problem/17352


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

    parent = [i for i in range(n + 1)]

    for _ in range(n - 2) :
        a, b = map(int, input().split())
        union_parent(parent, a, b)

    parent_list = []
    for i in range(1, n + 1) :
        parent_list.append(find_parent(parent, i))

    answer = list(set(parent_list))
    print(answer[0], answer[1])


solution()
