# 9. 기타 알고리즘
# 소수 부분 문자열
# https://www.acmicpc.net/problem/5636

import math

# 소수 판별 함수를 정의 (강의 참고)
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
    data = str(input())
    if data == '0':
        break
    else:
        answer(data)