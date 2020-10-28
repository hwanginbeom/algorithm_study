number = int(input())
for i in range(number):
    tree_num = int(input())
    data = list(map(int, input().split()))
    data.sort()
    result = 0
    for j in range(2, tree_num):
        c = data[j] - data[j - 2]
        result = max(c, result)
    print(result)
