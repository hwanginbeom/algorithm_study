import sys

input = sys.stdin.readline


class Node:
    def __init__(self, data, left_node, right_node):
        self.data = data
        self.left_node = left_node
        self.right_node = right_node


# 전위순회
def pre_order(node, tree):
    print(node.data, end='')
    if node.left_node != '.':
        pre_order(tree[node.left_node], tree)
    if node.right_node != '.':
        pre_order(tree[node.right_node], tree)


# 중위 순회
def in_order(node, tree):
    if node.left_node != '.':
        in_order(tree[node.left_node], tree)
    print(node.data, end='')
    if node.right_node != '.':
        in_order(tree[node.right_node], tree)


# 후위순회
def post_order(node, tree):
    if node.left_node != '.':
        post_order(tree[node.left_node], tree)
    if node.right_node != '.':
        post_order(tree[node.right_node], tree)
    print(node.data, end='')


def solution():
    n = int(input())
    tree = {}
    answer = []
    for _ in range(n):
        data, left_node, right_node = input().split()
        tree[data] = Node(data, left_node, right_node)
    pre_order(tree['A'], tree)
    print()
    in_order(tree['A'], tree)
    print()
    post_order(tree['A'], tree)


solution()