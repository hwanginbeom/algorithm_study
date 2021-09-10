#백준 142

t = int(input())


def max_sub():
    n = int(input())
    data = list(map(int, input().split()))

    for i in range(1, len(data)):
        data[i] += data[i - 1] if data[i - 1] > 0 else 0

    return max(data)


p = []

for i in range(t):
    p.append(max_sub())

for i in range(t):
    print(p[i])