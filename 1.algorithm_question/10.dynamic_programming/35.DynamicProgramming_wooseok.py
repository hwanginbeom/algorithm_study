# RGB 거리
def solution() :
    n = int(input())
    cost = []

    for _ in range(n) :
        cost.append(list(map(int, input().split())))

    dp = [[0] * 3 for _ in range(n)]

    for i in range(n) :
        if i == 0 :
            dp[i][0] = cost[0][0]
            dp[i][1] = cost[0][1]
            dp[i][2] = cost[0][2]

        # 빨간색을 선택했을 경우
        # 이전 집 색 두 가지중 누적 합이 작은 것을 골라 더한다.
        dp[i][0] = cost[i][0] + min(dp[i - 1][1], dp[i - 1][2])

        # 초록색을 선택했을 경우
        # 똑같이
        dp[i][1] = cost[i][1] + min(dp[i - 1][0], dp[i - 1][2])

        # 파란색을 선택했을 경우
        # 똑같이
        dp[i][2] = cost[i][2] + min(dp[i - 1][0], dp[i - 1][1])

    min_cost = min(dp[n - 1][0], dp[n - 1][1], dp[n - 1][2])

    print(min_cost)


solution()
