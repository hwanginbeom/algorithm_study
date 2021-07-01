# 2xn 타일링
# https://www.acmicpc.net/problem/11726


def solution() :
    n = int(input())

    if n == 1 :
        answer = 1
    elif n == 2 :
        answer = 2
    else :
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2

        for i in range(3, n + 1) :
            dp[i] = dp[i - 1] + dp[i - 2]

        answer = dp[n]

    print(answer % 10007)


solution()
