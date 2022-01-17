# 설탕 배달
# https://www.acmicpc.net/problem/2839


def solution() :
    n = int(input())
    count = 0

    while True :
        if n % 5 == 0 :
            count += n // 5
            break
        else :
            n = n - 3
            count += 1

        if n == 1 or n == 2 :
            count = -1
            break

    print(count)


solution()
