# 1, 2, 3 더하기
def solution() :
    t = int(input())
    answer = []

    for _ in range(t) :
        n = int(input())

        if n == 1 :
            answer.append(1)
            continue
        elif n == 2 :
            answer.append(2)
            continue

        dp = [0] * (n + 1)

        # 1, 2, 3을 각각 1, 2, 3의 합으로 나타낼 수 있는 방법의 수
        dp[1] = 1
        dp[2] = 2
        dp[3] = 4

        # 이전 3개의 숫자의 연산들에 특정 수만 더하게 되면
        # 해당 숫자의 연산이 되는 수학적 이론 이용
        # ex)
        # 1 : 1
        # 2 : 1 + 1, 2
        # 3 : 1 + 1 + 1, 2 + 1, 1 + 2, 3
        # 4는 1의 연산에 + 3, 2의 연산들에  + 2, 3의 연산들에 + 1을 해주게 되면
        # 4가 되는 방법들이므로 이전 3개의 숫자들의 연산방법 수의 합
        for i in range(4, n + 1) :
            dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

        answer.append(dp[n])

    for i in answer :
        print(i)


solution()
