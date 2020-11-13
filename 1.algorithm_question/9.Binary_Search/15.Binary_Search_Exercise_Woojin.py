### 랜선 자르기

k, n = map(int, input().split())
rope_list = list()

for i in range(k):
    rope_list.append(int(input()))

start = 1
end = max(rope_list)

# 이진탐색 수행
while (start <= end):
    total = 0
    mid = (start + end) // 2

    for i in rope_list:
        total += i // mid
    if total < n:
        end = mid - 1
    else:
        start = mid + 1

print(end)

### 나무 자르기

n, m = map(int, input().split())
wood_list = list(map(int, input().split()))

start = 0
end = max(wood_list)

result = 0

while (start <= end):
    total = 0
    mid = (start + end) // 2
    for i in wood_list:
        if i > mid:
            total += i - mid
    if total < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)