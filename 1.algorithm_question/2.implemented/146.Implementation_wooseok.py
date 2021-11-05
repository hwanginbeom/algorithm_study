# OX퀴즈
# https://www.acmicpc.net/problem/8958


def solution() :
    t = int(input())
    answer = []

    for _ in range(t) :
        score = input()
        count = 0
        total = 0

        for s in score :
            if s == 'O' :
                count += 1
            else :
                count = 0

            total += count

        answer.append(total)

    for i in answer :
        print(i)


solution()
