# 1. 친구 네트워크
# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드를 찾을 때까지 재귀 호출
    if parent[x] == x:
        return x

    parent[x] = find_parent(parent, parent[x])
    return parent[x]


# 두 원소가 속한 집합을 합치기
def union_parent(parent, count, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a != b :
        parent[b] = a
        count[a] += count[b]


def solution1() :
    t = int(input())

    for _ in range(t) :
        f = int(input())

        parent = {}
        count = {}

        # 불필요한 리스트 쓰면 시간초과
        # index 함수가 반복 하나 더 쓰는 효율을 내는듯
        for i in range(f) :
            f1, f2 = input().split()
            if f1 not in parent :
                parent[f1] = f1
                count[f1] = 1

            if f2 not in parent :
                parent[f2] = f2
                count[f2] = 1

            union_parent(parent, count, f1, f2)

            print(count[find_parent(parent, f1)])


solution1()
