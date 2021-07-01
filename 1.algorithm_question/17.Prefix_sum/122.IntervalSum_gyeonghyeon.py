import sys

input = sys.stdin.readline

n, m = map(int, input().split())

t = list(map(int, input().split()))

result = []
for idx in range(n - m + 1):
    result.append(sum(t[idx:idx + m]))

print(max(result))
