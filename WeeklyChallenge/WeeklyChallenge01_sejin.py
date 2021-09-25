def solution(price, money, count):
    fee = 0
    for i in range(1, count+1):
        fee += price*i

    if money >= fee:
        return 0
    else:
        return fee-money


# 다른 사람 풀이
def solution(price, money, count):
    answer = max(sum([price*i for i in range(1, count+1)]) - money, 0)
    return answer
