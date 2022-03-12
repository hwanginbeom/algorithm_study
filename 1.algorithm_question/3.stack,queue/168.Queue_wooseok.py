# 카드 문자열
# https://www.acmicpc.net/problem/13417


def solution() :
    t = int(input())
    answer = []

    for _ in range(t) :
        n = int(input())
        card_list = list(input().split())
        new_string = card_list[0]

        for i in range(1, n) :
            if card_list[i] <= new_string[0] :
                new_string = ''.join([card_list[i], new_string])
            else :
                new_string = ''.join([new_string, card_list[i]])

        answer.append(new_string)

    for i in answer :
        print(i)


solution()
