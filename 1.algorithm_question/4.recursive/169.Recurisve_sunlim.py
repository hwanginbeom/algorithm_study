# 전위순회 : 루트 -> 왼쪽 -> 오른쪽
def preorderTraversal(root):
    print(root, end="")
    if not data[root][0] == ".":
        preorderTraversal(data[root][0])

    if not data[root][1] == ".":
        preorderTraversal(data[root][1])


# 중위순회 : 왼쪽 -> 루트 -> 오른쪽
def inorderTraversal(root):
    if not data[root][0] == ".":
        inorderTraversal(data[root][0])
    print(root, end="")
    if not data[root][1] == ".":
        inorderTraversal(data[root][1])


# 후위순회 : 왼쪽 -> 오른쪽 -> 루트
def postorderTraversal(root):
    if not data[root][0] == ".":
        postorderTraversal(data[root][0])

    if not data[root][1] == ".":
        postorderTraversal(data[root][1])
    print(root, end="")


data = {}
for _ in range(int(input())):
    a, b, c = map(str, input().split())
    data[a] = [b, c]

preorderTraversal("A")
print()
inorderTraversal("A")
print()
postorderTraversal("A")