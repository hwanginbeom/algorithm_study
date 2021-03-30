# Disjoint Set
# 여행 가자
# https://www.acmicpc.net/problem/1976

# 특정 원소가 속한 집합을 찾는 함수
def find_parent(parent, x):
    # 루트 노드를 찾을 때까지 재귀 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치는 함수
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 도시의 수, 계획에 속한 도시들의 수 입력
N = int(input())
M = int(input())

# 부모 테이블 생성 후 부모를 자기 자신으로 초기화
parent = [0] * (N + 1)
for i in range(1, N + 1):
    parent[i] = i

# 연결 정보를 이중 리스트로 입력
connected = []
for _ in range(N):
    connected.append(list(map(int, input().split())))

# 연결 여부 방식에서 연결된 노드 번호를 표기하는 방식으로 변환
line = []
for i in range(N):
    for j in range(i, N): # 중복된 연결 정보를 피하기 위해 i부터 비교
        if connected[i][j] == 1:
            line.append([i + 1, j + 1]) # 노드 번호이기 때문에 + 1 해준다.

# 노드 연결 정보를 활용해 Union 연산을 수행
for j in line:
    union_parent(parent, j[0], j[1])

# 여행 계획 도시의 노드 번호를 입력
path = list(map(int, input().split()))
check = True
# 출발점부터 연결 여부를 확인
for i in path:
    # 부모 노드가 같으면 연결 처리하고 계속 진행
    if find_parent(parent, path[0]) == find_parent(parent, i):
        pass
    else:
        # 서로소 관계이면 중단하고 계획대로 방문 불가 판정
        check = False
        break

# 전부 연결되어 있으면 YES 출력
if check: print('YES')
else: print('NO')