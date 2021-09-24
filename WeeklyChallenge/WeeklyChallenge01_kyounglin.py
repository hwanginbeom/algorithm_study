# 2021-09-24

# 출처 : https://programmers.co.kr/learn/courses/30/lessons/82612

# 위클리 챌린지 - 1주차_부족한 금액 계산하기

price=3
money=20
count=4

def solution(price, money, count):
    answer = 0
    for i in range(count + 1):
        answer += (price * i)

    if (answer - money) < 0:
        return 0

    return answer - money

print(solution(price,money,count))
