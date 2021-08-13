from bisect import bisect_left

n = int(input())
data = list(map(int, input().split()))

result = []
for i in data:
    if not result or result[-1] < i:
        result.append(i)
    else:
        result[bisect_left(result, i)] = i
print(len(result))
