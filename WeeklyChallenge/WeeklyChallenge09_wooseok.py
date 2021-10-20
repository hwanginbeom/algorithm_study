# 전력망을 둘로 나누기
# https://programmers.co.kr/learn/courses/30/lessons/86971


def find_parent(parent, x):
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


def solution(n, wires):
    answer = -1
    abs_list = []

    for i in range(len(wires)):
        parent = [x for x in range(0, n + 1)]

        for j in range(len(wires)):
            if j != i:
                union_parent(parent, wires[j][0], wires[j][1])

        # 한번 더 부모를 찾는 과정을 실행해주어야 한다.
        for j in range(n + 1) :
            parent[j] = find_parent(parent, j)

        parent = parent[1:]
        count = parent.count(parent[0])
        abs_list.append(abs((n - count) - count))

    answer = min(abs_list)

    return answer


n = 6
wires = [[1, 4], [6, 3], [2, 5], [5, 1], [5, 3]]
print(solution(n, wires))
