# 스티커
# https://www.acmicpc.net/problem/9465


def solution() :
    t = int(input())
    answer = []

    for _ in range(t) :
        n = int(input())
        sticker = []

        for _ in range(2) :
            sticker.append(list(map(int, input().split())))

        # print(sticker)

        sticker[0][1] = sticker[1][0] + sticker[0][1]
        sticker[1][1] = sticker[0][0] + sticker[1][1]

        for i in range(2, n) :
            sticker[0][i] = max(sticker[1][i - 1], sticker[1][i - 2]) + sticker[0][i]
            sticker[1][i] = max(sticker[0][i - 1], sticker[0][i - 2]) + sticker[1][i]

        answer.append(max(sticker[0][-1], sticker[1][-1]))

    for i in answer :
        print(i)


solution()
