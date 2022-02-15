import sys

input = sys.stdin.readline


def solution():
    n, k = map(int, input().split())
    weather_list = list(map(int, input().split()))
    sum_value = 0
    prefix_sum = [0]
    for i in weather_list:
        sum_value += i
        prefix_sum.append(sum_value)
    answer = -2000
    for i in range(n):
        if i == n-k+1:
            break
        left = i
        right = i + k
        answer = max(answer, prefix_sum[right] - prefix_sum[left])
    print(answer)

solution()
