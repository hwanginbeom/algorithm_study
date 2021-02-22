# 공항
# Disjoint Set
# https://www.acmicpc.net/problem/10775

G = int(input())
P = int(input())
plane = []
for _ in range(P):
    plane.append(int(input()))

def parent_find(x):
    if x == parent[x]:
        return x
    p = parent_find(parent[x])
    parent[x] = p
    return parent[x]


def union(x, y):
    x = parent_find(x)
    y = parent_find(y)
    parent[x] = y


parent = {i: i for i in range(G + 1)}
cnt = 0
for i in plane:
    x = parent_find(i)
    if x == 0:
        break
    union(x, x - 1)
    cnt += 1
print(cnt)
