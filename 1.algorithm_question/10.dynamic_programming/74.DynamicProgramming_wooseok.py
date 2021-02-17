# 계단 오르기
def solution() :
    n = int(input())
    stair_list = []

    for _ in range(n) :
        stair_list.append(int(input()))

    dp = [0] * (n + 1)

    if n == 1 :
        answer = stair_list[0]
    elif n == 2 :
        answer = stair_list[0] + stair_list[1]
    else :
        dp[1] = stair_list[0]
        dp[2] = dp[1] + stair_list[1]

        # 두 가지 경우 존재
        # 현재 계단에서 바라보았을 때 1) 바로 전 계단에서 올라온 경우와
        # 2) 전전 계단에서 올라온 경우
        # 1) 바로 전 계단에서 올라온 경우 전전 계단을 사용할 수 없으므로
        # 전전전 계단까지 기록된 최대 점수를 더한다.
        for i in range(3, n + 1) :
            dp[i] = max(stair_list[i - 2] + dp[i - 3] + stair_list[i - 1], dp[i - 2] + stair_list[i - 1])

        answer = dp[n]

    print(answer)


solution()

# IndexError 원인
# dp[1]과 dp[2]를 먼저 만들어놓는 로직이라면 n이 1일 때 dp는 [0], [1] 두가지밖에 없다.
# dp[2]에 대해서 IndexError 발생
# 경우를 나누어서 답을 저장하는 것으로 변경
