def max_sub():
    _ = int(input())
    data = list(map(int, input().split()))
    for i in range(1, len(data)):
        data[i] += data[i - 1] if data[i - 1] > 0 else 0
    return max(data)


def solution():
    t = int(input())
    for i in range(t):
        print(max_sub())

solution()
