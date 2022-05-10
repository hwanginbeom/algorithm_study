# 슈퍼 마리오
# https://www.acmicpc.net/problem/2851


def solution() :
    mushroom = []
    sum_value = 0
    check = 0

    for _ in range(10) :
        mushroom.append(int(input()))

    for i in mushroom :
        sum_value += i

        if sum_value >= 100 :
            break

        check = sum_value

    sum_value_100 = abs(100 - sum_value)
    check_100 = abs(100 - check)

    if sum_value_100 < check_100 :
        print(sum_value)
    elif sum_value_100 > check_100 :
        print(check)
    else :
        print(max(sum_value, check))


solution()
