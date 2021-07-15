n = int(input())
money = 1000 - n

coin = [500, 100, 50, 10, 5, 1]
cnt = 0

for i in coin:
    cnt += money // i # 몫 연산자
    money %= i # 나머지 연산자
print(cnt)