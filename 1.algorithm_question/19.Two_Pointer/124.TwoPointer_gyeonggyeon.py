import sys
input = sys.stdin.readline

n,m = map(int, input().split())
data = list(map(int, input().split()))

start = end = interval_sum = 0
answer = 1000001
while end <= n:
    if interval_sum >= m:
        answer = min(answer, (end - start))
        interval_sum -= data[start]
        start += 1
        # print('start', interval_sum, start)
    elif interval_sum < m:
        if end != n:
            interval_sum += data[end]
            # print('end', interval_sum, end)
        end += 1

if answer == 1000001:
    print(0)
else:
    print(answer)
