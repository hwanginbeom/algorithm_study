# 2021-04-08

# 출처 : https://www.acmicpc.net/problem/17103

# 골드바흐 파티션
#
# 골드바흐의 추측: 2보다 큰 짝수는 두 소수의 합으로 나타낼 수 있다.
# 짝수 N을 두 소수의 합으로 나타내는 표현을 골드바흐 파티션이라고 한다. 짝수 N이 주어졌을 때, 골드바흐 파티션의 개수를 구해보자. 두 소수의 순서만 다른 것은 같은 파티션이다.


import sys
input = sys.stdin.readline

n=int(input())
array=[int(input()) for _ in range(n)]
m=max(array)

# 소수의 리스트 구하기
prime_list = [False,False]+[True]*(m-1) # 앞에 false,false는 1,2 소수
for i in range(2,int(m**0.5)+1):
    if prime_list[i]:
        for j in range(i+i,m+1,i):
            if prime_list[j]:
                prime_list[j]=False

for k in array:
    cnt=0
    for i in range((k//2)+1):
        if prime_list[i] and prime_list[k-i]: # 소수끼리의 합
            cnt+=1
    print(cnt)