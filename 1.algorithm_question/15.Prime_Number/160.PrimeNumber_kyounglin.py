# 2022-02-08

# 출처 : https://www.acmicpc.net/problem/2023

# 신기한 소수

import math

N = int(input())

first = ['2', '3', '5', '7']
prime = ['1', '3', '7', '9']  # 뒷자리에 짝수는 소수가 될수 없음


# 소수 판별 함수
def is_prime_number(x):
    # 2부터 x의 제곱근까지의 모든 수를 확인하며
    for i in range(2, int(math.sqrt(int(x)) + 1)):
        # x가 해당 수로 나누어떨어진다면 pass
        if int(x) % i == 0:
            return False

    if len(x) == N:
        return print(x)  # 소수 출력

    for p in prime:
        is_prime_number(x + p)


for f in first:
    is_prime_number(f)
