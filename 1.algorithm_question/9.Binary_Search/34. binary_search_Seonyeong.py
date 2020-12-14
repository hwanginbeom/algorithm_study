## 2110번: 공유기 설치

n,c = map(int, input().split())
houses = [int(input()) for _ in range(n)]
houses = sorted(houses)


def binary_search(distance):
    count = 1
    current = houses[0]
    for i in range(1, n):
        if current + distance <= houses[i]:
            count += 1
            current = houses[i]
    return count

start, end = 1, houses[-1] - houses[0]

while start <= end:
    mid = (start + end)//2
    if binary_search(mid) >= c:
        answer = mid
        start = mid + 1
    else:
        end = mid - 1

print(answer)