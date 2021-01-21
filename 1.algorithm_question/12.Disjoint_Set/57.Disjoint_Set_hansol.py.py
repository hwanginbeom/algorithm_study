# 서로소 집합 자료 구조
# 서로소 집합을 활용한 사이클 판별
# 사이클 게임
# https://www.acmicpc.net/problem/2458

# 입력으로 점의 개수 n과 m 번째 차례까지의 게임 진행 상황이 주어지면 사이클이 완성 되었는지를 판단하고,
# 완성되었다면 몇 번째 차례에서 처음으로 사이클이 완성된 것인지를 출력하는 프로그램을 작성하시오.

# 풀이
# 강의의 사이클 판별 부분과 거의 모든 부분이 같다.

# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드를 찾을 때까지 재귀 호출
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


# 노드의 개수와 간선(Union 연산)의 개수 입력 받기
n, m = map(int, input().split())
parent = [0] * (n + 1)  # 부모 테이블 초기화하기

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, n + 1):
    parent[i] = i

cycle = False  # 사이클 발생 여부 초기화

for i in range(m):
    a, b = map(int, input().split())
    # 사이클이 발생한 경우
    if find_parent(parent, a) == find_parent(parent, b):
        cycle = True
        print(i + 1)
        break

    # 사이클이 발생하지 않았다면 합집합(Union) 연산 수행
    else:
        union_parent(parent, a, b)

if not cycle:
    print(0)

