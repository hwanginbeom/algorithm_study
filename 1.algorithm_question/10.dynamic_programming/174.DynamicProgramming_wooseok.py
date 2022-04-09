# 정수 삼각형
# https://www.acmicpc.net/problem/1932


def solution() :
    n = int(input())
    dp = []

    for _ in range(n) :
        row = list(map(int, input().split()))
        dp.append(row)

    if n == 1 :
        print(dp[0][0])
    elif n == 2 :
        print(max(dp[0][0] + dp[1][0], dp[0][0] + dp[1][1]))
    else :
        dp[1][0] = dp[0][0] + dp[1][0]
        dp[1][1] = dp[0][0] + dp[1][1]

        for i in range(2, n) :
            for j in range(len(dp[i])) :
                if j == 0 :
                    dp[i][j] = dp[i - 1][j] + dp[i][j]
                elif j == len(dp[i]) - 1 :
                    dp[i][j] = dp[i - 1][j - 1] + dp[i][j]
                else :
                    dp[i][j] = max(dp[i - 1][j - 1] + dp[i][j], dp[i - 1][j] + dp[i][j])

        print(max(dp[-1]))


solution()
