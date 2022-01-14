# 숫자 카드
# https://www.acmicpc.net/problem/10815


def solution() :
    answer = []
    n = int(input())
    card_list = list(map(int, input().split()))
    m = int(input())
    num_list = list(map(int, input().split()))

    card_list.sort()

    for num in num_list :
        check = 0
        start = 0
        end = n - 1

        while start <= end :
            middle = (start + end) // 2

            if card_list[middle] < num :
                start = middle + 1
            elif card_list[middle] > num :
                end = middle - 1
            else :
                check = 1
                break

        answer.append(check)

    for i in answer :
        print(i)


solution()
