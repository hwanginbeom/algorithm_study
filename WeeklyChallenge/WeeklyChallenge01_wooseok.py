# 부족한 금액 계산하기
# https://programmers.co.kr/learn/courses/30/lessons/82612


def solution(price, money, count):
    answer = -1

    charge = 0
    for i in range(1, count + 1):
        charge += price * i

    answer = charge - money
    if answer <= 0:
        answer = 0

    return answer


price = 3
money = 20
count = 4
print(solution(price, money, count))
