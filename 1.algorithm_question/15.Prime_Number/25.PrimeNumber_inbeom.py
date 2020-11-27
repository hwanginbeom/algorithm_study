#2581 - 소수

import math


# 소수 판별 함수 ( 2이상의 자연수에 대하여)
def is_prime_number(x):
    # 2부터 x의 제곱근까지의 모든 수를 확인하며
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
    # x가 해당 수로 나누어 떨어진다면
            return False  # 소수가 아님
    return True  # 소수


m = int(input())
n = int(input())

decimal_list = []
for i in range(m,n+1):
    if i == 1:
        pass
    elif i == 2:
        decimal_list.append(i)
    else:
        if is_prime_number(i):
            decimal_list.append(i)
else:
    if len(decimal_list) == 0:
        print('-1')
    else:
        print(sum(decimal_list))
        print(min(decimal_list))


# 4948 - 베르트랑 공준
import math


# 소수 판별 함수 ( 2이상의 자연수에 대하여)
def is_prime_number(x):
    # 2부터 x의 제곱근까지의 모든 수를 확인하며
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
    # x가 해당 수로 나누어 떨어진다면
            return False  # 소수가 아님
    return True  # 소수



while(1):
    m = int(input())
    if m == 0 :
        break
    decimal_list = []

    for i in range(m+1,m*2+1):
        # print(i)
        if i == 2:
            decimal_list.append(i)
        else:
            if is_prime_number(i):
                decimal_list.append(i)
    else:
        if len(decimal_list) == 0:
            print('-1')
        else:
            print(len(decimal_list))
