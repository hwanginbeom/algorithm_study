# 1. 피보나치 수2
def fibo1(n) :
    dp = [0 for _ in range(n + 1)]
    dp[0] = 0
    dp[1] = 1

    for i in range(2, n + 1) :
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


def solution1() :
    n = int(input())

    print(fibo1(n))


# solution1()



# 2. 피보나치 함수
def solution2() :
    n = int(input())
    n_list = []

    for _ in range(n) :
        n_list.append(int(input()))

    for i in n_list :
        count_0 = [0 for _ in range(i + 1)]
        count_0[0] = 1
        if i >= 1 :
            count_0[1] = 0

        count_1 = [0 for _ in range(i + 1)]
        count_1[0] = 0
        if i >= 1 :
            count_1[1] = 1

        for j in range(2, i + 1) :
            count_0[j] = count_0[j - 1] + count_0[j - 2]
            count_1[j] = count_1[j - 1] + count_1[j - 2]

        print(count_0[i], end = ' ')
        print(count_1[i])


solution2()
