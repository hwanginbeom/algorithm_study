# 2021-09-27

# 출처 : https://www.acmicpc.net/problem/1940

# 주몽

N = int(input())
M = int(input())

array = list(map(int, input().split()))

array.sort()

count = 0
start, end = 0, N - 1

while start < end:
    if array[start] + array[end] == M:
        count += 1
        start += 1
        end -= 1
    elif array[start] + array[end] < M:
        start += 1
    else:
        end -= 1

print(count)