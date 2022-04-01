import sys

input = sys.stdin.readline


def isValid(midValue):
    global result
    low = arr[0]
    high = arr[0]
    d = 1

    for i in arr:
        if high < i:
            high = i

        if low > i:
            low = i

        if high - low > midValue:
            d += 1
            low = i
            high = i

    return m >= d


n, m = map(int, input().split())
arr = list(map(int, input().split()))
r = max(arr)
l = 0
result = r
while l <= r:
    mid = (l + r) // 2
    if isValid(mid):
        r = mid - 1
        result = min(result, mid)
    else:
        l = mid + 1
print(result)
