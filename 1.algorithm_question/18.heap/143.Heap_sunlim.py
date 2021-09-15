from sys import stdin
import heapq


def check(data):
    left, right = [], []
    middle = data[0]
    result = [middle]
    for idx, val in enumerate(data[1:], 1):
        if val > middle:
            heapq.heappush(right, val)
        else:
            heapq.heappush(left, -val)
        if idx % 2 == 0:
            if len(left) < len(right):
                heapq.heappush(left, -middle)
                middle = heapq.heappop(right)
            elif len(left) > len(right):
                heapq.heappush(right, middle)
                middle = -heapq.heappop(left)
            result.append(middle)

    print(len(result))

    for i in range(len(result)):
        if (i + 1) != 1 and (i + 1) % 10 == 1:
            print()
        print(result[i], end=' ')
    print()


t = int(stdin.readline().rstrip())

for _ in range(t):
    m = int(input())
    data = []

    if m % 10 == 0:
        for _ in range(m // 10):
            data.extend(list(map(int, stdin.readline().rstrip().split())))
    else:
        for _ in range(m // 10 + 1):
            data.extend(list(map(int, stdin.readline().rstrip().split())))

    check(data)