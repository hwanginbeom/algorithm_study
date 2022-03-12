# 트리 순회
# https://www.acmicpc.net/problem/1991


# 전위 순회
def pre_order(start, tree_dict) :
    if start == '.' :
        return

    print(start, end = '')

    # 왼쪽 자식 노드로 이동
    pre_order(tree_dict[start][0], tree_dict)
    # 오른쪽 자식 노드로 이동
    pre_order(tree_dict[start][1], tree_dict)


# 중위 순회
def in_order(start, tree_dict) :
    if start == '.':
        return

    # 왼쪽 자식 노드로 이동
    in_order(tree_dict[start][0], tree_dict)

    print(start, end = '')

    # 오른쪽 자식 노드로 이동
    in_order(tree_dict[start][1], tree_dict)


# 후위 순회
def post_order(start, tree_dict) :
    if start == '.':
        return

    # 왼쪽 자식 노드로 이동
    post_order(tree_dict[start][0], tree_dict)
    # 오른쪽 자식 노드로 이동
    post_order(tree_dict[start][1], tree_dict)

    print(start, end = '')


def solution() :
    n = int(input())
    tree_dict = {}
    start = 0

    for i in range(n) :
        root, left, right = input().split()
        if i == 0 :
            start = root

        tree_dict[root] = [left, right]

    pre_order(start, tree_dict)
    print()
    in_order(start, tree_dict)
    print()
    post_order(start, tree_dict)


solution()
