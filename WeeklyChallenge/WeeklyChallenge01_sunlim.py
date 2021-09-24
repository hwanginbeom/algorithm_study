#Weekely Challenge_1주차: 부족한 금액 계산하기

#Question
# 놀이기구 원래 이용료=Price, N번째 이용하면 Price의 N배 받음
# 놀이기구 count타면 현재 자신이 가지고 있는 금액에서 얼마가 모자라는지 return해라



#solution

def solution(price, money, count):
    answer = 0
    original_price = price

    for i in range(count):    #count번 만큼 반복문
        money -= price
        price += original_price   

    if money < 0:       #음수가 나오면 요금이 부족한것이기에 -1곱하여 처리
        answer = money * (-1)

    return answer

