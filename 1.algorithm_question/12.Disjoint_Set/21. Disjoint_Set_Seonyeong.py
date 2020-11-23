## 1717번: 집합의 표현

def find_parent(parent, x):
    # 루트 노드를 찾을 때까지 재귀 호출
    if parent[x] == x:
        return x

    parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split())
parent = [0] * (n+1)

for i in range(0, n+1):
    parent[i] = i

for i in range(m):
    k, a, b = map(int, input().split())

    if k == 0:
        union_parent(parent, a, b)
    else:
        if find_parent(parent, a) == find_parent(parent, b):
            print('YES')
        else:
            print('NO')


## 1976번: 여행 가자

n = int(input())
m = int(input())

cities = []
for _ in range(n):
    cities.append(list(map(int, input().split())))

wish_cities = list(map(int, input().split()))

parent = [0]*(n+1)

for i in range(1, n+1):
    parent[i] = i

def find_parent(parent, x):
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


for i in range(n):
    for j in range(n):
        if cities[i][j] == 1:
            union_parent(parent, i+1, j+1)

for i in range(m-1):
    if find_parent(parent, wish_cities[i]) != find_parent(parent, wish_cities[i+1]):
        print('NO')
        break
else:
    print('YES')