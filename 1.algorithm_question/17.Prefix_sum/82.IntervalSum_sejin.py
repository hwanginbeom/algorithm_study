import sys
input = sys.stdin.readline

INF = int(1e9)

n, k = map(int, input().split()) # n:전체날짜의수, k:연속적인날짜의수
temp = list(map(int, input().split()))


# 접두사 합(Prefix Sum) 배열 계산
sum_value = 0
prefix_sum = [0]
for i in temp:
    sum_value += i
    prefix_sum.append(sum_value)

# print(prefix_sum) # 0,3,1,-1,-12,-12,-9,,,,

answer = -INF

for i in range(k, len(prefix_sum)) :
    answer = max(answer, prefix_sum[i] - prefix_sum[i-k])
print(answer)
