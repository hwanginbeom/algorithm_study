n, s = list(map(int, input().split()))
data = list(map(int, input().split()))

start, end = 0, 0
answer = data[0]
min_val = float('-inf')
count = 1

while start < n:
    if answer >= n:
        min_val = min(min_val, count)

    if answer >= s or end == n-1:
        answer -= data[start]
        start += 1
        count -= 1

    else:
        end += 1
        answer += data[end]
        count += 1

if min_val == float('-inf'):
    print(0)
else:
    print(min_val)

