# 거스름돈
# https://www.acmicpc.net/problem/5585


def solution() :
    n = int(input())

    money_list = [500, 100, 50, 10, 5, 1]
    change = 1000 - n
    count = 0

    for money in money_list :
        count += change // money
        change = change % money

    print(count)


solution()
