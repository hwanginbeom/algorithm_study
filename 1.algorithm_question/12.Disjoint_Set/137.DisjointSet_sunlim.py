#BAEKJOON 17352 '여러분의 다리가 되어드리겠습니다'
#UDFS 상호 배타적인 집합들의 모임을 모델링하는 자료구조
# 섬이라는 집합을 가지고 두섬이 연결되어 있는지 여부에 따라 다리를 놓는 문제이다.

# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드를 찾을 때까지 재귀 호출
    if parent[x] != x:   #부모노드가 아닐때
        parent[x] = find_parent(parent, parent[x])   #자신을 넣어 부모노드 찾기
    return parent[x]


# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)   #루트노드를 찾은 다음

    if a < b:                  #숫자가 더 큰쪽이 부모노드로 설정

        parent[b] = a
    else:
        parent[a] = b


def solution() :
    n = int(input())

    parent = [i for i in range(n + 1)]

    for _ in range(n - 2) :
        a, b = map(int, input().split())     #노드 개수와 간선의 개수 입력 받기
        union_parent(parent, a, b)

    parent_list = []
    for i in range(1, n + 1) :
        parent_list.append(find_parent(parent, i))

    answer = list(set(parent_list))
    print(answer[0], answer[1])


solution()