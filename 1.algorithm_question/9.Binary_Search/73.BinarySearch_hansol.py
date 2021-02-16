# 예산
# 이진 탐색
# https://www.acmicpc.net/problem/2512

def binarySearch(budget, limit):
    start, end = 1, max(budget)
    ans = 0
    while start <= end:
        mid = (start + end) // 2
        total = 0
        for i in budget:
            if i > mid:
                total += mid
            else:
                total += i
        if total <= limit:
            start = mid + 1
            ans = mid
        else:
            end = mid - 1
    return ans


N = int(input())
budget = list(map(int, input().split()))
limit = int(input())
print(binarySearch(budget, limit))