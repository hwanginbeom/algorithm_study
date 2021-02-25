# 2021-02-25

# 출처 : https://www.acmicpc.net/problem/5636

# 소수 부분 문자열

# 숫자로 이루어진 문자열이 주어진다. 이때, 부분 문자열 중에서 가장 큰 소수를 찾는 프로그램을 작성하시오.
# 이 문제에서는 2보다 크거나 같고, 100,000보다 작거나 같은 소수만 소수이다.

import math

# 소수 판별 알고리즘
def is_prime_number(x):
    if x==1:
        return False
    elif (2 <= x) and (x <= 100000) :
        for i in range(2,int(math.sqrt(x))+1):
            if x % i == 0:
                return False
        return True


def answer(array):
    check=[]
    for i in range(len(array)):
        for j in range(i+1,len(array)+1): # 순서에 맞게 문자열 조합 구하기
            check.append(int(array[i:j]))
    check=set(check) # 중복제거
    check=list(check)
    answer=[]
    for i in check:
        if is_prime_number(i):
            answer.append(i)

    print(max(answer)) # 소수 중 가장 큰 값



while (1):
    array = str(input())
    if array=='0':
        break
    else:
        answer(array)