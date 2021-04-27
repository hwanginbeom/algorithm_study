from collections import Counter

n = int(input())

extension = []
for _ in range(n):
    extension.append(input().split('.')[1])

list = sorted(Counter(extension).items(), key=lambda x: x[0])
for x, y in list:
    print(x, y)
