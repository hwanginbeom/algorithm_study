# 1. 설탕 배달
def solution1() :
    n = int(input())
    count = 0

    # 5로 나누어 떨어질 경우
    if n % 5 == 0 :
        count = n // 5
    # 5로 나누어 떨어지지 않을 경우
    else :
        # 3을 뺀 후 5로 나누어보는 작업을 반복
        while n > 0 :
            n = n - 3
            count += 1

            if n % 5 == 0 :
                count += n // 5
                break

        # 반복 이후 n의 값이 0보다 작으면
        # 정확히 나누어 담지 못하는 것을 의미한다.
        if n < 0 :
            count = -1

    print(count)


# solution1()



# 2. 1로 만들기
def solution2() :
    n = int(input())

    # n보다 크기가 하나 큰 DP 리스트 생성
    dp = [0 for _ in range(n + 1)]

    # bottom-up 방식 사용
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + 1

        if i % 2 == 0 and dp[i] > dp[i // 2] + 1:
            dp[i] = dp[i // 2] + 1

        if i % 3 == 0 and dp[i] > dp[i // 3] + 1:
            dp[i] = dp[i // 3] + 1

    print(dp[n])


solution2()
