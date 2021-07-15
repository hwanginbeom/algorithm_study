def solution(buy):
    money = 1000 - buy
    cnt = 0
    coin_list = [500, 100, 50, 10, 5, 1]
    for coin in coin_list:
        cnt += money // coin
        money %= coin
    return cnt


n = int(input())
print(solution(n))
