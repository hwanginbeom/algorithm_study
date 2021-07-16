# 거스름돈
# https://www.acmicpc.net/problem/5585

n = 1000 - int(input())

currency = [500, 100, 50, 10, 5, 1]  # 동전의 가치 저장할 리스트 선언
count = 0   # 동전의 개수를 저장할 변수
i = 0       # 동전의 가치 리스트의 인덱스 변수

while n != 0:
  count += n//currency[i]   # 동전의 개수를 저장
  n %= currency[i]          # 동전의 가치로 나눈 나머지를 저장
  i += 1                    # 인덱스를 증가시킴

print(count)