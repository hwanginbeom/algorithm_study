# 파도반 수열
# https://www.acmicpc.net/problem/9461


def solution() :
    t = int(input())
    answer = []

    for _ in range(t) :
        n = int(input())

        if n == 1 :
            answer.append(1)
            continue
        elif n == 2 :
            answer.append(1)
            continue
        elif n == 3 :
            answer.append(1)
            continue
        elif n == 4 :
            answer.append(2)
            continue

        dp = [0] * (n + 1)

        dp[1] = 1
        dp[2] = 1
        dp[3] = 1
        dp[4] = 2

        for i in range(5, n + 1) :
            dp[i] = dp[i - 1] + dp[i - 5]

        answer.append(dp[n])

    for i in answer:
        print(i)


solution()
