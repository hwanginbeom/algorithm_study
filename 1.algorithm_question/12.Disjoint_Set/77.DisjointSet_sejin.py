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


g = int(input()) # g:공항번호(1~)
p = int(input()) # p:비행기수

# 부모 테이블 초기화하기
parent = {i:i for i in range(g+1)}

array = []
for _ in range(p) :
    array.append(int(input()))


count = 0
for i in array :
    x = find_parent(parent, i)
    if x == 0 : # 도킹 가능한 gate가 없다면 종료
        break
    union_parent(parent, x, x-1) # 도킹하고자 하는 게이트와 이전 게이트 union
    count += 1

print(count)