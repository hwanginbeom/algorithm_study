# 2021-08-27

# 출처 : https://www.acmicpc.net/problem/2887

# 행성터널

import sys


# 신장트리 -> 사이클이 존재하지 않는 경우

# 사이클이 발생하는지 찾기
def find_parent(parent, x):
    # 루프 노드를 찾을 때까지 재귀 호출
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x


# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


N = int(input())

parent = [0] * (N + 1)  # 부모테이블 초기화

# 모든 간선을 담을 리스트와, 최종 비용을 담을 변수
result = 0

x_list = []
y_list = []
z_list = []

# 부모테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, N + 1):
    parent[i] = i

# 모든 간선에 대한 정보 입력받기

for i in range(1, N + 1):
    x, y, z = map(int, input().split())
    x_list.append((x, i))
    y_list.append((y, i))
    z_list.append((z, i))

# 간선을 좌표로 정렬

x_list.sort()
y_list.sort()
z_list.sort()

dist_list = []

for i in range(1, N):
    dist_list.append((abs(x_list[i][0] - x_list[i - 1][0]), x_list[i][1], x_list[i - 1][1]))
    dist_list.append((abs(y_list[i][0] - y_list[i - 1][0]), y_list[i][1], y_list[i - 1][1]))
    dist_list.append((abs(z_list[i][0] - z_list[i - 1][0]), z_list[i][1], z_list[i - 1][1]))

# 거리별로 정렬

dist_list.sort()

# 간선을 하나씩 확인
for edge in dist_list:
    cost, x, y = edge
    # 사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parent(parent, x) != find_parent(parent, y):
        union_parent(parent, x, y)
        result += cost

print(result)