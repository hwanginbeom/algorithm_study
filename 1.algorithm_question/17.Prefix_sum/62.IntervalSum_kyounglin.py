# 2021-01-28

# 출처 : https://www.acmicpc.net/problem/11441

# 합 구하기

# N개의 수 A1, A2, ..., AN이 입력으로 주어진다. 총 M개의 구간 i, j가 주어졌을 때, i번째 수부터 j번째 수까지 합을 구하는 프로그램을 작성하시오.
import sys
input=sys.stdin.readline

n=int(input())
data=list(map(int,input().split()))

# 접두사 합 배열 계산

sum_value=0
prefix_sum=[0]
for i in data:
    sum_value+=i
    prefix_sum.append(sum_value)

# 구간 합 계산
m=int(input())

for _ in range(m):
    left,right = map(int,input().split())
    print(prefix_sum[right]-prefix_sum[left-1])
