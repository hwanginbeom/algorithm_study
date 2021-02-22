# 공항
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
    g = int(input())
    p = int(input())

    plane_list = []
    for _ in range(p) :
        plane_list.append(int(input()))

    gate = [i for i in range(g + 1)]
    count = 0

    for i in plane_list :
        a = find_parent(gate, i)

        if a == 0 :
            break

        # a와 a - 1을 union 하는 이유
        # 이미 도킹된 게이트가 입력될 경우, 번호를 내리면서 순차적으로 확인해야되는데
        # 마지막에는 도킹된 게이트의 부모노드가 0으로 다 통일이 되기 때문에
        # 빠르게 도킹 여부 확인이 가능하다.
        union_parent(gate, a, a - 1)
        count += 1

    print(count)


solution()
