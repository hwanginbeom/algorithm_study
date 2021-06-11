from sys import stdin
import heapq

# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드를 찾을 때까지 재귀 호출
    if parent[x] == x:
        return x
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

while True:
    n, m = map(int, stdin.readline().split())
    if (n,m) == (0,0):
        break
    parent = [0] * n

    for i in range(n):
        parent[i] = i

    q = []
    heapq.heapify(q)
    tot = 0
    ans = 0

    for _ in range(m):
        a, b, c = map(int, stdin.readline().split())
        heapq.heappush(q, (c, a, b))

    while q:
        dist, s, e = heapq.heappop(q)
        tot += dist
        if find_parent(parent,s) != find_parent(parent,e):
            union_parent(parent,s, e)
            ans += dist
    print(tot - ans)