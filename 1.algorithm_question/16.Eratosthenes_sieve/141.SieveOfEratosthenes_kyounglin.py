# 2021-09-08

# 출처 : https://www.acmicpc.net/problem/1929

M,N=map(int,input().split())

# 소수 구하기 함수
def prime_number(x):
    if x==1:
        return False
    else:
        # 에라토스테네스 체
        for i in range(2, int(x ** 0.5) + 1):  # 2부터 n제곱근까지 확인
            if x%i==0:
                return False
        return True

for i in range(M,N+1):
    if prime_number(i):
        print(i)

