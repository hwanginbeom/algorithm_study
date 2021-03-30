import sys
# sys.setrecursionlimit(10**5) # 런타임에러(recursionerror해결)
input = sys.stdin.readline

# 특정 원소가 속한 집합을 찾기
def find_parent(x):
    # 루트 노드를 찾을 때까지 재귀 호출
    if x == parent[x]:
        return x
    parent[x] = find_parent(parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


# 노드의 개수와 간선(Union 연산)의 개수 입력 받기
n = int(input()) # n:도시의수
m = int(input()) # m:여행계획에속한 도시의수

# 부모 테이블상에서 부모를 자기 자신으로 초기화
parent = [i for i in range(n+1)]

arr = []
for _ in range(n) :
    arr.append(list(map(int, input().split())))

for i in range(len(arr)) : #3 #012
    for j in range(n) : #3 #012
        if arr[i][j] == 1 :
            union_parent(i+1, j+1)


check_list = list(map(int,input().split()))
answer = []

for i in check_list :
    answer.append(find_parent(i))

if len(list(set(answer))) == 1:
    print('YES')
else :
    print('NO')
