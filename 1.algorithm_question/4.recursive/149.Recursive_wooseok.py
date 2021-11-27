# 하노이 탑 이동 순서
# https://www.acmicpc.net/problem/11729


def hanoi(n, start, end, between, count, order) :
    if n == 1 :
        count += 1
        order.append(f'{start} {end}')

        return count, order

    # 원판 n - 1 개를 가운데 기둥으로 이동
    count, order = hanoi(n - 1, start, between, end, count, order)

    count += 1
    order.append(f'{start} {end}')

    # 가운데 기둥에 있는 원반 n - 1 개를 목적지로 이동
    count, order = hanoi(n - 1, between, end, start, count, order)

    return count, order


def solution() :
    n = int(input())

    count, order = hanoi(n, 1, 3, 2, 0, [])

    print(count)
    for i in order :
        print(i)


solution()
