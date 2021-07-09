# 2021=07-09

# 부분합

# 현재 부분합이 S보다 작으면 END 1 증가, S보다 크거나 같으면 START를 1증가


N, S = map(int, input().split())

array = list(map(int, input().split()))

length = float('inf')
intervalsum = 0
end = 0

for start in range(N):
    while intervalsum < S and end < N:
        intervalsum += array[end]
        end += 1
        if end == N:
            break

    if intervalsum >= S:
        length = min(length, end - start)
    intervalsum -= array[start]

if length == float('inf'):
    print(0)
else:
    print(length)