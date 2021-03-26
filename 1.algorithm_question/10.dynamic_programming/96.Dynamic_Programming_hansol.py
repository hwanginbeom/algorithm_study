# 다이나믹 프로그래밍
# 2xn 타일링
# https://www.acmicpc.net/problem/11726

# n = 1일 때부터 확인해보면 피보나치 수열의 2번째 항부터 나열한 수라는 것을 알 수 있다.
n = int(input())
# 피보나치 수열의 n + 1항 값을 구하는 알고리즘
fibonacci = [0] * 1002
fibonacci[1] = 1
for i in range(n):
    fibonacci[i + 2] += fibonacci[i + 1] + fibonacci[i]

print(fibonacci[n + 1] % 10007)