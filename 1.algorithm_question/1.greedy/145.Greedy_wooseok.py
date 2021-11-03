# 동전 0
# https://www.acmicpc.net/problem/11047


def solution() :
    n, k = map(int, input().split())
    coin_list = []
    answer = 0

    for _ in range(n) :
        coin_list.append(int(input()))

    coin_list.reverse()

    for coin in coin_list :
        answer += k // coin
        k = k % coin

        if k == 0 :
            break

    print(answer)


solution()
