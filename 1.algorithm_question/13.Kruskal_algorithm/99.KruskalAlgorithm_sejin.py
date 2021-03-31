import sys
input = sys.stdin.readline

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

    if a == b:
        return False

    if a < b:
        parent[b] = a
    else:
        parent[a] = b
    return True


def kruskal():
    answer = 0
    count = 0
    for x, y, z in edges:
        if union_parent(parent, y, z):
            if count == n - 2:
                break

            answer += x
            count += 1
    return answer


n, m = map(int, input().split()) # n:집개수, m:길개수

# 모든 간선을 담을 리스트와, 최종 비용을 담을 변수
edges = []

parent = [i for i in range(n + 1)] # 부모 테이블 초기화
for _ in range(m):
    a, b, c = map(int, input().split()) # a집과 b 연결하는 유지비 c
    edges.append((c, a, b))
    edges.append((c, b, a))

# 간선을 비용순으로 오름차순 정렬
edges.sort()

print(kruskal())

