def solution(price, money, count):
    require = sum([ price * i for i in range(1, count + 1)]) - money
    return require if require > 0 else 0


price, money, count = 3, 20, 4
solution(price, money, count)
