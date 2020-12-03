## 1541번: 읿어버린 괄호

example = input().split('-')

result = 0
for i in example[0].split('+'):
    result += int(i)

for i in example[1:]:
    for j in i.split('+'):
        result -= int(j)
print(result)


## 11047번: 동전 0

n, k = map(int, input().split())

coin_list = []
for _ in range(n):
    coin = int(input())
    coin_list.append(coin)
    coin_list.sort(reverse=True)


count = 0
for coin in coin_list:
    count += k // coin
    k %= coin

print(count)