## 11659번: 구간 합 구하기 4

# input() 쓰면 적용이 되지 않음
import sys

N, M = map(int, sys.stdin.readline().split())

num = list(map(int, sys.stdin.readline().split()))

sum_value = 0
prefix_sum = [0]
for n in num:
    sum_value += n
    prefix_sum.append(sum_value)


for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    print(prefix_sum[j] - prefix_sum[i-1])


## 11660번: 구간 합 구하기 5
import sys

N, M = map(int, input().split())
graph = []
for _ in range(N):
    num = list(map(int, sys.stdin.readline().split()))
    graph.append(num)

print(graph)

sum_value = 0
prefix_sum = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        sum_value += graph[i][j]
        prefix_sum[i][j] = sum_value

print(prefix_sum)

for _ in range(M):
    total_sum = 0
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())

    for i in range(x1-1, x2):
        if y1 != 1:
            sum = prefix_sum[i][y2-1] - prefix_sum[i][y1-2]
            total_sum += sum
        else:
            sum = prefix_sum[i][y2-1] - prefix_sum[i-1][N-1]
            if i == 0:
                sum = prefix_sum[i][y2 - 1]
            total_sum += sum
    print(total_sum)