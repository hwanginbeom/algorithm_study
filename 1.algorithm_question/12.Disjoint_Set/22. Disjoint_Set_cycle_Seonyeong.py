## 4195번: 친구 네트워크

def find_parent(parent, x):
    # 루트 노드를 찾을 때까지 재귀 호출
    if parent[x] == x:
        return x

    parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, count, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a != b:
        parent[b] = a
        count[a] += count[b]


T = int(input())

for t in range(T):

    F = int(input())
    parent = {}
    count = {}


    for f in range(F):
        a, b = input().split()
        if a not in parent:
            parent[a] = a
            count[a] = 1
        if b not in parent:
            parent[b] = b
            count[b] = 1

        union_parent(parent, count, a, b)

        print(count[find_parent(parent, a)])