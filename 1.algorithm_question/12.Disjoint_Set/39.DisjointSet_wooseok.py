# 친구비
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


def solution() :
    n, m, k = map(int, input().split())

    dict = {}
    cost = list(map(int, input().split()))

    for i in range(n) :
        dict[i + 1] = cost[i]

    friend_cost = sorted(dict.items(), key=lambda x : x[1])

    # 부모 테이블 초기화
    parent = [0] * (n + 1)

    # 부모 테이블상에서 부모를 자기 자신으로 초기화
    for i in range(1, n + 1):
        parent[i] = i

    # 연결된 친구관계 합치기
    for _ in range(m) :
        v, w = map(int, input().split())

        if find_parent(parent, v) != find_parent(parent, w) :
            union_parent(parent, v, w)

    answer = 0

    for i in range(len(friend_cost)) :
        # 부모 노드 찾기
        p = find_parent(parent, friend_cost[i][0])

        # 부모 노드가 0이라면 (아래에서 부모노드 같으면 0으로 처리할 것임)
        if p == 0 :
            continue
        else :
            # 친구의 친구인, 즉 연결된 모든 친구를 찾기
            for j in range(1, n + 1) :
                if p == parent[j] :
                    parent[j] = 0

            answer += friend_cost[i][1]

        if sum(parent) == 0 :
            break

    if answer > k or sum(parent) != 0:
        return 'Oh no'
    else :
        return answer


print(solution())
